# Initiating the cosmic dance floor with the OG Synchrotron
synch = Synchrotron(blob)
# Introducing Synchrotron with a self-absorption vibe, 'cause we're edgy like that
synch_ssa = Synchrotron(blob, ssa=True)

# Now, let's set the stage by defining a lit grid of frequencies for the Synchrotron SED
nu_syn = np.logspace(8, 23) * u.Hz

# Time to drop the beats! Calculating the Synchrotron and the self-absorbed Synchrotron SED
synch_sed = synch.sed_flux(nu_syn)
synch_sed_ssa = synch_ssa.sed_flux(nu_syn)

# Plotting the cosmic spectacle in a dope visual
fig, ax = plt.subplots(figsize=(8, 6))
plot_sed(nu_syn, synch_sed, ax=ax, color="k", label="synchr.")
plot_sed(
    nu_syn, synch_sed_ssa, ax=ax, ls="--", color="gray", label="self-absorbed synchr."
)
plt.show()
