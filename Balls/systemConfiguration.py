import numpy as np
import matplotlib.pyplot as plt

def point_motion(initial_position, initial_velocity, box_length, time_steps):
    positions = np.zeros(time_steps)
    positions[0] = initial_position

    dt = 1.0

    for i in range(1, time_steps):
        positions[i] = positions[i-1] + initial_velocity * dt

        if positions[i] < 0:
            positions[i] = -positions[i]
            initial_velocity = -initial_velocity

        elif positions[i] > box_length:
            positions[i] = 2 * box_length - positions[i]
            initial_velocity = -initial_velocity

    return positions

initial_position1 = 0.0
initial_velocity1 = 1.0
initial_position2 = 0.0
initial_velocity2 = 2.0
initial_position3 = 0.0
initial_velocity3 = 3.0
box_length = 50.0
time_steps = 181

positions1 = point_motion(initial_position1, initial_velocity1, box_length, time_steps)
positions2 = point_motion(initial_position2, initial_velocity2, box_length, time_steps)
positions3 = point_motion(initial_position3, initial_velocity3, box_length, time_steps)

data = np.vstack([np.arange(time_steps), positions1, positions2, positions3]).T

np.savetxt("point_motion_data.dat", data, delimiter="\t", header="time\tposition1\tposition2\tposition3")

print("Data saved to point_motion_data.dat")

data = np.vstack([np.arange(time_steps), positions1, positions2, positions3]).T

# Extract data for each point
time = data[:, 0]
positions1 = data[:, 1]
positions2 = data[:, 2]
positions3 = data[:, 3]

# Create the 3D plot
fig = plt.figure(figsize=(8, 6))
ax = fig.add_subplot(111, projection='3d')

# Plot each point as a separate line
ax.scatter(positions1, positions2, positions3)

# Set labels and title
ax.set_xlabel('q_1')
ax.set_ylabel('q_2')
ax.set_zlabel('q_3')  # Modify as needed based on the data

# Add legend
ax.legend()

# Show the plot
plt.show()
