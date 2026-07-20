import numpy as np
rng = np.random.default_rng(7)

# ---------- parameters ----------
lam = 1.07e-6; k = 2*np.pi/lam
N = 512; L = 3.0                      # grid, window (m)
dx = L/N
D_tx = 1.0                            # beam director aperture (m)
site = 2000.0                         # site altitude
d_act = 0.10                          # AO actuator pitch (m)
n_mc = 8

x = (np.arange(N)-N//2)*dx
X, Y = np.meshgrid(x, x)
r = np.sqrt(X**2+Y**2)
aperture = (r <= D_tx/2).astype(float)
fx = np.fft.fftfreq(N, dx)
FX, FY = np.meshgrid(fx, fx)
F2 = FX**2+FY**2

def Cn2(h):
    return (0.00594*(21/27)**2*(h*1e-5)**10*np.exp(-h/1000)
            + 2.7e-16*np.exp(-h/1500) + 1.7e-14*np.exp(-h/100))

def r0_slab(h0,h1,zen):
    hs=np.linspace(h0,h1,200)
    J=np.trapezoid(Cn2(hs),hs)/np.cos(np.radians(zen))
    return (0.423*k**2*J)**(-3/5)

def phase_screen(r0):
    L0=25.0
    PSD = (F2+1/L0**2)**(-11/6); PSD[0,0]=0
    cn=(rng.normal(size=(N,N))+1j*rng.normal(size=(N,N)))*np.sqrt(PSD)
    phi=np.real(np.fft.ifft2(cn))
    # empirical normalization: enforce Kolmogorov structure function D(l)=6.88(l/r0)^(5/3)
    lag=min(max(int(round(r0/dx)),1), N//4)
    Dm=np.mean((phi-np.roll(phi,lag,axis=1))**2)
    Dt=6.88*((lag*dx)/r0)**(5/3)
    return phi*np.sqrt(Dt/Dm)

def lowpass(phi, cutoff):
    P=np.fft.fft2(phi); P[np.sqrt(F2)>cutoff]=0
    return np.real(np.fft.ifft2(P))

def run_case(zen, R, theta_pa, ao_on):
    slabs=np.array([2,3,4.5,6,8,10,12.5,15,18,22])*1e3
    layers=[(slabs[i],slabs[i+1]) for i in range(len(slabs)-1)]
    buckets=[]
    theta_b = 1.25/R                      # bucket half-angle for 2.5 m HX
    for _ in range(n_mc):
        screens=[phase_screen(r0_slab(a,b,zen)) for a,b in layers]
        hmid=[(a+b)/2-site for a,b in layers]
        # beacon path (on-axis) measurement, AO conjugation up to actuator cutoff
        if ao_on:
            meas=sum(screens)
            corr=-lowpass(meas, 1/(2*d_act))
        else:
            corr=0.0
        # target beam passes through screens SHIFTED by point-ahead offset
        field=aperture.astype(complex)*np.exp(1j*corr)
        for s,h in zip(screens,hmid):
            shift=int(round(theta_pa*h/dx))
            field*=np.exp(1j*np.roll(s,shift,axis=1))
        # far field (vacuum beyond atmosphere)
        ff=np.fft.fftshift(np.fft.fft2(field))
        I=np.abs(ff)**2; I/=I.sum()
        th=np.fft.fftshift(fx)*lam
        TH_X,TH_Y=np.meshgrid(th,th)
        buckets.append(I[np.sqrt(TH_X**2+TH_Y**2)<=theta_b].sum())
    return np.mean(buckets), np.std(buckets)

print("Power delivered into the 2.5 m heat exchanger (fraction of transmitted)")
print(f"{'case':<38}{'zen':>5}{'range':>8}{'pt-ahead':>9}{'AO':>4}{'bucket':>9}{'+/-':>6}")
cases=[("VERTICAL -> relay mirror",      0, 600e3,  2e-6, True),
       ("Slant mid-burn -> vehicle",    55, 350e3, 20e-6, True),
       ("Vertical, no AO (reference)",   0, 600e3,  2e-6, False),
       ("Slant, no AO (reference)",     55, 350e3, 20e-6, False)]
for name,zen,R,tpa,ao in cases:
    m,s=run_case(zen,R,tpa,ao)
    print(f"{name:<38}{zen:>4}deg{R/1e3:>6.0f}km{tpa*1e6:>7.0f}ur{('on' if ao else 'off'):>4}{m:>9.2f}{s:>6.2f}")

print("\nDiffraction-limited reference (no atmosphere): bucket fraction ~0.99 at these ranges")
print("Thermal blooming NOT in this wave model -- parametric bounds from prior scaling:")
print("  vertical/300m array N_D=28 (correctable) | slant end-of-burn N_D=270 (not)")
