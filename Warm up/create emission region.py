# Setting the cosmic vibe with Blob properties
R_b = 1e16 * u.cm  # Blob radius, 'cause we like it grand
V_b = 4 / 3 * np.pi * R_b ** 3  # Blob volume, the cosmic playground
z = Distance(1e27, unit=u.cm).z  # Redshift, a glimpse into the cosmic past
delta_D = 10  # Doppler factor, bringing the cosmic speed
Gamma = 10  # Bulk Lorentz factor, defining the Blob's swagger
B = 1 * u.G  # Magnetic field strength, setting the cosmic mood

# Powering up the electron distribution for the Blob's dance party
W_e = 1e48 * u.Unit("erg")  # Total energy in electrons, the life of the cosmic party

# Creating a Power-Law for our electron distribution - the cool kids at the dance
n_e = PowerLaw.from_total_energy(
    W=W_e, V=V_b, p=2.8, gamma_min=1e2, gamma_max=1e7, mass=m_e
)

# Introducing the Blob - the epicenter of cosmic vibes
blob = Blob(R_b, z, delta_D, Gamma, B, n_e=n_e)

# The Blob object is print-ready, revealing a cosmic summary of its epic properties
print(blob)
