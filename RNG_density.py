from matplotlib import pyplot as plt
import numpy as np
from numba import njit


mf = 200 # Magic find.
base = 1/968.47*(1+mf/100) # Drop chance of the RNG item.
mu = 500 # Set to 250 for vampire, 300 for dungeons, 500 for the rest.
epb = 1500 # Exp per boss or dungeon run.
n = int(mu/base/epb) # Tries required to fill up meter.
N = np.arange(1, n+1, 1)
simulations = 1000000 # Number of simulations to average.
density = np.zeros_like(N).astype(float)
P = lambda k: base*(1 + 2*(k-1)/n)

for i in range(simulations):
	if i/simulations*100%1 == 0:
		print(f"{round(i/simulations*100, 4)}%")
	last_drop = 0
	for k in N:
		if np.random.rand() <= P(k-last_drop): #If the RNG is dropped.
			last_drop = k
			density[k-1] = density[k-1] + 1 # Adds a drop to the density, this will be normalized later.
		else:
			continue # You got nothing, too bad!

plt.plot(N, density/sum(density))
plt.ylabel("Probability")
plt.xlabel("Tries")
plt.title("Density of a scythe blade with 200 magic find")
plt.savefig("density.pdf")
plt.show()