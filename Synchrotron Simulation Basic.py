# Import the essentials for our intergalactic adventure
import numpy as np
import astropy.units as u
from astropy.constants import m_e
from astropy.coordinates import Distance
from agnpy.spectra import PowerLaw
from agnpy.emission_regions import Blob
from agnpy.synchrotron import Synchrotron
from agnpy.utils.plot import load_mpl_rc, plot_sed
import matplotlib.pyplot as plt

# Set the stage with quantities defining our cosmic blob
R_b = 1e16 * u.cm  # Behold the mighty Blob's radius, an astronomical scale basketball
V_b = 4 / 3 * np.pi * R_b ** 3  # The Blob's volume, where the cosmic party unfolds
z = Distance(1e27, unit=u.cm).z  # Redshift, the VIP pass to the AGN shenanigans
delta_D = 10  # Doppler factor, because we're all about that fast life
Gamma = 10  # Bulk Lorentz factor, defining the Blob's swagger
B = 1 * u.G  # Magnetic field strength, the cosmic DJ's beat intensity

# Electron distribution - our cosmic dance party attendees
W_e = 1e48 * u.erg  # Total energy in electrons, powering the party

# Let's create a Power-Law for our electron distribution - the cool kids at the dance
n_e = PowerLaw.from_total_energy(
    W_e,
    V_b,
    p=2.8,
    gamma_min=1e2,
    gamma_max=1e7,
    mass=m_e,
)

# Now, introducing our main act - the Blob and the Synchrotron dance master
blob = Blob(R_b, z, delta_D, Gamma, B, n_e=n_e)  # Behold the mighty Blob, the cosmic dance floor
synch = Synchrotron(blob)  # Our Synchrotron dance master, orchestrating the cosmic rhythms

# Brace yourself as we compute the Spectral Energy Distribution (SED) over a cosmic playlist of frequencies
nu = np.logspace(8, 23) * u.Hz  # Frequencies, the beats of our cosmic dance
sed = synch.sed_flux(nu)

# Ready your telescopes and load the cosmic disco lights for our SED presentation 
load_mpl_rc()

# Let's plot the cosmic spectacle - the Synchrotron dance on the AGN stage
plot_sed(nu, sed, label="synchrotron")
plt.show()
