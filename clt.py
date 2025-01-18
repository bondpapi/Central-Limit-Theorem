import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns

# Set the population parameters
population_mean = 70
population_std = 10
population_size = 100000

# Generate a population
population = np.random.normal(
    loc=population_mean, scale=population_std, size=population_size)

# Parameters for the simulation
sample_sizes = [5, 30, 100]  # Different sample sizes
num_samples = 1000  # Number of samples to draw for each sample size

# Prepare the figure
plt.figure(figsize=(15, 8))

for i, n in enumerate(sample_sizes):
    sample_means = []

    # Draw samples and calculate sample means
    for _ in range(num_samples):
        sample = np.random.choice(population, size=n, replace=False)
        sample_means.append(np.mean(sample))

    # Plot the distribution of sample means
    plt.subplot(1, len(sample_sizes), i + 1)
    sns.histplot(sample_means, kde=True, bins=30,
                 color='skyblue', stat='density')
    plt.title(f"Sample Size: {n}")
    plt.xlabel("Sample Mean")
    plt.ylabel("Density")
    plt.axvline(x=population_mean, color='red',
                linestyle='--', label='Population Mean')
    plt.legend()

plt.tight_layout()
plt.show()
