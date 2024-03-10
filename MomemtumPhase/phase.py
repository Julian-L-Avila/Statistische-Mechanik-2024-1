import math as m
import numpy as np

def harmonic(c1, c2, omega, time_steps, dt):
    solutions = np.zeros(time_steps)
    solutions[0] = c2
    o = np.sqrt(omega)
    
    for i in range(1, time_steps):
        solutions[i] = c1 * np.sin(i * dt * o) + c2 * np.cos(i * dt * o)

    return solutions

def time(time_steps, dt):
    times = np.zeros(time_steps)
    times[0] = 0

    for i in range(1, time_steps):
        times[i] = times[i - 1] + dt

    return times

m = 0.02
k = np.pi * np.pi * 4 * m
v1 = 0
omega = 2 * np.pi
Ax = 5
vx = 0
Ap = 0
Fp = -k * Ax
dt = 0.1
time_steps = 1000

times = time(time_steps, dt)
positions = harmonic(Ax, vx, omega, time_steps, dt)
momenta = harmonic(Ap, Fp, omega, time_steps, dt)

data = np.vstack([times, positions, momenta]).T

np.savetxt("phase.dat", data, delimiter="\t", header="t\tx\tp")

print("Data saved")
