# Dropping some mad science with Synchrotron Self-Compton (SSC)
ssc = SynchrotronSelfCompton(blob)

# Leveling up with SSC over a self-absorbed synchrotron spectrum
ssc_ssa = SynchrotronSelfCompton(blob, ssa=True)

# Setting the cosmic playlist frequencies for the SSC beats
nu_ssc = np.logspace(15, 30) * u.Hz

# Calculating the lit SSC and self-absorbed SSC SED
sed_ssc = ssc.sed_flux(nu_ssc)
sed_ssc_ssa = ssc_ssa.sed_flux(nu_ssc)

# Unveiling the cosmic spectacle in a dope visual
fig, ax = plt.subplots(figsize=(8, 6))
plot_sed(nu_ssc, sed_ssc, color="k", label="SSC")
plot_sed(nu_ssc, sed_ssc_ssa, ls="--", color="gray", label="SSC with SSA")
plt.show()
