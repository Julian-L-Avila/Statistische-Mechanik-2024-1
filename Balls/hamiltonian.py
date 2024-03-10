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

def momentum(mass, velocity):
    momenta = np.zeros(time_steps)
    momenta[0] = mass * velocity[0]

    for i in range(1, time_steps):
        momenta[i] = mass * velocity[i]

    return momenta

def time(time_steps, dt):
    times = np.zeros(time_steps)
    times[0] = 0
    
    for i in range(1, time_steps):
        times[i] = times[i - 1] + dt

    return times

mass1 = 0.02
initial_positionx1 = 0.0
initial_positiony1 = 10.0
initial_velocityy1 = 30.0
initial_velocityx1 = 10.0
g = -980.7
box_length = 50.0
time_steps = 1000
dt = 0.0001

velocityx = np.zeros(time_steps)
velocityx[0] = initial_velocityx1
velocityy = np.zeros(time_steps)
velocityy[0] = initial_velocityy1

positionsy1 = point_motion(initial_positiony1, initial_velocityy1, velocityy, g, box_length, time_steps, dt)
positionsx1 = point_motion(initial_positionx1, initial_velocityx1, velocityx, 0.0, box_length, time_steps, dt)
time_t = time(time_steps, dt)
momentax1 = momentum(mass1, velocityx)
momentay1 = momentum(mass1, velocityy)

data = np.vstack([time_t, positionsx1, positionsy1, velocityx, velocityy, momentax1, momentay1]).T
position_data = np.vstack([time_t, positionsx1, positionsy1]).T 
momentum_data = np.vstack([time_t, positionsx1, positionsy1, momentax1, momentay1]).T

np.savetxt("global.dat", data, delimiter="\t", header="time\tx\ty\tvx\tvy\tpx\tpy")
np.savetxt("position.dat", position_data, delimiter="\t", header="time\tx\ty")
np.savetxt("momentum.dat", momentum_data, delimiter="\t", header="time\tx\ty\tpx\tpy")

print("Data saved")
