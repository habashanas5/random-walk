import matplotlib.pyplot as plt
import random

def random_2d_walk(iterations, replaces):
    xs = []
    ys = []
    total_distances = [0] * iterations

    for j in range(replaces):
        x = 0
        y = 0
        distances = []

        for i in range(iterations):
            r = random.uniform(0, 100)

            if r < 25:
                y += 1
            elif r < 50:
                y -= 1
            elif r < 75:
                x += 1
            else:
                x -= 1

            distance = (x**2 + y**2)**0.5
            distances.append(distance)
            total_distances[i] += distance

            xs.append(x)
            ys.append(y)

        plt.plot(xs, ys)
        plt.plot(xs[-1], ys[-1], color="orange")

    return xs, ys, total_distances

# Parameters
iterations = 10000
replaces = 1

# Generate random 2D walk
xs, ys, total_distances = random_2d_walk(iterations, replaces)

# Plot the final result
plt.title('2D Random Walk')
plt.xlabel('X')
plt.ylabel('Y')
plt.show()

# Plot total distances over iterations
plt.plot(total_distances)
plt.title('Total Distance over Iterations')
plt.xlabel('Iterations')
plt.ylabel('Total Distance')
plt.show()
