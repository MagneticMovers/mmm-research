import numpy as np
rng = np.random.default_rng(11)

lam=1.07e-6; k=2*np.pi/lam
N=512; L=3.0; dx=L/N
D_tx=1.0; site=2000.0; d_act=0.10
tau_ao=1.0e-3                      # AO loop latency, s
n_mc=6; n_bloom_iter=4

x=(np.arange(N)-N//2)*dx
X,Y=np.meshgrid(x,x); r=np.sqrt(X**2+Y**2)
ap=(r<=D_tx/2).astype(float)
fx=np.fft.fftfreq(N,dx); FX,FY=np.meshgrid(fx,fx); F2=FX**2+FY**2

def Cn2(h): return (0.00594*(21/27)**2*(h*1e-5)**10*np.exp(-h/1000)
                    +2.7e-16*np.exp(-h/1500)+1.7e-14*np.exp(-h/100))
def r0_slab(h0,h1,zen):
    hs=np.linspace(h0,h1,200); J=np.trapezoid(Cn2(hs),hs)/np.cos(np.radians(zen))
    return (0.423*k**2*J)**(-3/5)
def wind(h):  # Bufton-like
    return 5.0+25.0*np.exp(-((h-9400)/4800)**2)
def screen(r0):
    PSD=(F2+1/25.0**2)**(-11/6); PSD[0,0]=0
    cn=(rng.normal(size=(N,N))+1j*rng.normal(size=(N,N)))*np.sqrt(PSD)
    phi=np.real(np.fft.ifft2(cn))
    lag=min(max(int(round(r0/dx)),1),N//4)
    Dm=np.mean((phi-np.roll(phi,lag,axis=1))**2)
    return phi*np.sqrt(6.88*((lag*dx)/r0)**(5/3)/Dm)
def lowpass(p,c):
    P=np.fft.fft2(p); P[np.sqrt(F2)>c]=0; return np.real(np.fft.ifft2(P))

slabs=np.array([2,3,4.5,6,8,10,12.5,15,18,22])*1e3
layers=[(slabs[i],slabs[i+1]) for i in range(len(slabs)-1)]

def bloom_phase(I_field, zen, ND_target):
    """Upwind-integral steady-state blooming per slab, similarity-scaled to ND_target."""
    phis=[]; raw=0.0
    for (a,b) in layers:
        hm=(a+b)/2; dz=(b-a)/np.cos(np.radians(zen))
        alpha=5e-6*np.exp(-(hm-site)/2000)            # aerosol absorption
        w=max(wind(hm),3.0)
        Cb=alpha*dz/w                                  # per-slab weight (units folded into scale)
        cum=np.cumsum(I_field,axis=1)*dx               # upwind integral of normalized intensity
        phis.append(Cb*cum); raw+=Cb*np.max(cum)
    s=ND_target/ (k*raw) if raw>0 else 0               # scale so peak bloom phase ~ ND_target rad
    return [k*s*p for p in phis]

def run(zen,R,tpa,ND,ao=True):
    theta_b=1.25/R; out=[]
    for _ in range(n_mc):
        scr=[screen(r0_slab(a,b,zen)) for a,b in layers]
        hm=[(a+b)/2-site for a,b in layers]
        bl=[np.zeros((N,N)) for _ in layers]
        for it in range(n_bloom_iter):
            # AO measures beacon column incl. current bloom, corrects below actuator cutoff,
            # but its knowledge is stale by tau (frozen-flow wind shift) and offset by point-ahead
            if ao:
                meas=sum(scr)+sum(bl)
                corr=-lowpass(meas,1/(2*d_act))
            else: corr=0.0
            f=ap.astype(complex)*np.exp(1j*corr)
            I_low=None
            for s,b,h,(a2,b2) in zip(scr,bl,hm,layers):
                off=int(round((tpa*h+wind((a2+b2)/2)*tau_ao)/dx))
                f*=np.exp(1j*(np.roll(s,off,axis=1)+np.roll(b,off,axis=1)))
                if I_low is None: I_low=np.abs(f)**2   # intensity entering lowest slabs
            bl=bloom_phase(np.abs(ap)**2*0+I_low/np.max(I_low+1e-30),zen,ND)
        ff=np.fft.fftshift(np.fft.fft2(f)); I=np.abs(ff)**2; I/=I.sum()
        th=np.fft.fftshift(fx)*lam; TX,TY=np.meshgrid(th,th)
        out.append(I[np.sqrt(TX**2+TY**2)<=theta_b].sum())
    return np.mean(out),np.std(out)

print("FULL GAUNTLET: turbulence + AO(fitting+point-ahead+temporal lag) + steady-state blooming")
print(f"{'case':<40}{'ND':>5}{'bucket':>9}{'+/-':>6}")
for name,zen,R,tpa,ND in [
    ("VERTICAL -> relay (baseline)",        0,600e3, 2e-6, 28),
    ("Slant early burn",                   30,150e3,20e-6, 96),
    ("Slant mid burn",                     55,350e3,20e-6,150),
    ("Slant END of burn (worst case)",     72,700e3,20e-6,270)]:
    m,s=run(zen,R,tpa,ND)
    print(f"{name:<40}{ND:>5}{m:>9.2f}{s:>6.2f}")
m,s=run(0,600e3,2e-6,0)
print(f"{'Vertical, blooming OFF (for delta)':<40}{'0':>5}{m:>9.2f}{s:>6.2f}")
