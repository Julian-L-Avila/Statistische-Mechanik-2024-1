import numpy as np
import matplotlib.pyplot as plt

def point_motion(initial_position, initial_velocity, velocity, accelaration, box_length, time_steps, dt):
    t = 1
    positions = np.zeros(time_steps)
    positions[0] = initial_position

    for i in range(1, time_steps):
        positions[i] = initial_position + initial_velocity * t * dt + accelaration * t * t * dt * dt / 2
        velocity[i] = initial_velocity + accelaration * t * dt
        t += 1

        if positions[i] < 0 or box_length < positions[i]:
            initial_velocity = - initial_velocity - accelaration * t * dt
            velocity[i] = initial_velocity
            t = 0

            while positions[i] < 0 or box_length < positions[i]:
                initial_position = fix_position(positions[i], box_length)
                positions[i] = initial_position

    return positions

def fix_position(position, box_length):

    if position < 0:
        position = -position
        initial_position = position

    elif position > box_length:
        position = 2 * box_length - position
        initial_position = position

    return initial_position

def momentum(mass, velocity, time_steps):
    momenta = np.zeros(time_steps)
    momenta[0] = mass * velocity[0]

    for i in range(1, time_steps):
        momenta[i] = mass * velocity[i]

    return momenta

def potential(mass, position, accelaration, time_steps):
    potentialV = np.zeros(time_steps)
    potentialV[0] = mass * accelaration * position[0]

    for i in range(1, time_steps):
        potentialV[i] = mass * accelaration * position[i]

    return potentialV

def kinetic(mass, velocity, time_steps):
    kineticK = np.zeros(time_steps)
    kineticK[0] = mass * velocity[0] * velocity[0] / 2

    for i in range(1, time_steps):
        kineticK[i] = mass * velocity[i] * velocity[i] / 2

    return kineticK

def lagrangian(potential, kinetic, time_steps):
    lagrangian = np.zeros(time_steps)
    lagrangian[0] = kinetic[0] - potential[0]

    for i in range(1, time_steps):
        lagrangian[i] = kinetic[i] - potential[i]

    return lagrangian


def hamiltonian(potential, kinetic, time_steps):
    hamiltonian = np.zeros(time_steps)
    hamiltonian[0] = potential[0] + kinetic[0]

    for i in range(1, time_steps):
        hamiltonian[i] = potential[i] + kinetic[i]

    return hamiltonian

def time(time_steps, dt):
    times = np.zeros(time_steps)
    times[0] = 0
    
    for i in range(1, time_steps):
        times[i] = times[i - 1] + dt

    return times

mass1 = 0.02
initial_positionx1 = 0.0
initial_positiony1 = 10.0
initial_velocityx1 = 10.0
initial_velocityy1 = 30.0
g = -980.7
box_length = 50.0
time_steps = 1000
dt = 0.001

velocityx = np.zeros(time_steps)
velocityx[0] = initial_velocityx1
velocityy = np.zeros(time_steps)
velocityy[0] = initial_velocityy1

positionsy1 = point_motion(initial_positiony1, initial_velocityy1, velocityy, g, box_length, time_steps, dt)
positionsx1 = point_motion(initial_positionx1, initial_velocityx1, velocityx, 0.0, box_length, time_steps, dt)
time_t = time(time_steps, dt)
momentax1 = momentum(mass1, velocityx, time_steps)
momentay1 = momentum(mass1, velocityy, time_steps)

kineticEx = kinetic(mass1, velocityx, time_steps)
kineticEy = kinetic(mass1, velocityy, time_steps)
potentialVx = np.zeros(time_steps)
potentialVy = potential(mass1, positionsy1, -g, time_steps)

lagrangianx = lagrangian(potentialVx, kineticEx, time_steps)
lagrangiany = lagrangian(potentialVy, kineticEy, time_steps)
hamiltonx = hamiltonian(potentialVx, kineticEx, time_steps)
hamiltony = hamiltonian(potentialVy, kineticEy, time_steps)

data = np.vstack([time_t, positionsx1, positionsy1, velocityx, velocityy, momentax1, momentay1, kineticEx, kineticEy, potentialVx, potentialVy, hamiltonx, hamiltony]).T
position_data = np.vstack([time_t, positionsx1, positionsy1]).T 
momentum_data = np.vstack([time_t, positionsx1, positionsy1, momentax1, momentay1]).T
lagrangianx_data = np.vstack([time_t, positionsx1, velocityx, lagrangianx]).T
lagrangiany_data = np.vstack([time_t, positionsy1, velocityy, lagrangiany]).T
hamiltonx_data = np.vstack([positionsx1, momentax1, hamiltonx]).T
hamiltony_data = np.vstack([positionsy1, momentay1, hamiltony]).T

np.savetxt("global.dat", data, delimiter="\t", header="time\tx\ty\tvx\tvy\tpx\tpy")
np.savetxt("position.dat", position_data, delimiter="\t", header="time\tx\ty")
np.savetxt("momentum.dat", momentum_data, delimiter="\t", header="time\tx\ty\tpx\tpy")
np.savetxt("lagrangiax.dat", lagrangianx_data, delimiter="\t", header="time\tx\tv\tL")
np.savetxt("lagrangiay.dat", lagrangiany_data, delimiter="\t", header="time\ty\tv\tL")
np.savetxt("hamiltonx.dat", hamiltonx_data, delimiter="\t", header="x\tp\tH")
np.savetxt("hamiltony.dat", hamiltony_data, delimiter="\t", header="y\tp\tH")

print("Data saved")
