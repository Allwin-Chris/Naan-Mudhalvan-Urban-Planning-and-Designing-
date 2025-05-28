import numpy as np
import matplotlib.pyplot as plt
import random

# Constants
CITY_SIZE = 20  # 20x20 grid
MAX_POPULATION = 1000  # Max population per grid cell

# Generate random population data
def generate_population_data(size):
    return np.random.randint(0, MAX_POPULATION, size=(size, size))

# Generate random green spaces (1 = green space, 0 = not)
def generate_green_spaces(size, num_parks):
    grid = np.zeros((size, size))
    for _ in range(num_parks):
        x, y = random.randint(0, size - 1), random.randint(0, size - 1)
        grid[x][y] = 1
    return grid

# Simulate public transport hub suggestion based on population density
def suggest_transport_hubs(population_data, top_n=3):
    flat = population_data.flatten()
    indices = np.argpartition(flat, -top_n)[-top_n:]
    return [divmod(idx, population_data.shape[1]) for idx in indices]

# Visualization
def visualize(city_data, green_spaces, transport_hubs):
    plt.figure(figsize=(10, 8))

    # Heatmap for population
    plt.subplot(1, 2, 1)
    plt.title("Population Density")
    plt.imshow(city_data, cmap='hot', interpolation='nearest')
    plt.colorbar(label='Population')

    # Overlay green spaces
    for x in range(CITY_SIZE):
        for y in range(CITY_SIZE):
            if green_spaces[x][y] == 1:
                plt.plot(y, x, 'go')  # green dot for park

    # Overlay transport hubs
    for (x, y) in transport_hubs:
        plt.plot(y, x, 'bs')  # blue square for hub

    # Legend
    plt.subplot(1, 2, 2)
    plt.axis('off')
    plt.title("Legend")
    plt.plot([], [], 'ro', label='High Population')
    plt.plot([], [], 'go', label='Green Space')
    plt.plot([], [], 'bs', label='Transport Hub')
    plt.legend()

    plt.tight_layout()
    plt.show()

# Main function
def main():
    city_population = generate_population_data(CITY_SIZE)
    green_spaces = generate_green_spaces(CITY_SIZE, num_parks=15)
    transport_hubs = suggest_transport_hubs(city_population, top_n=5)

    visualize(city_population, green_spaces, transport_hubs)

if __name__ == "__main__":
    main()