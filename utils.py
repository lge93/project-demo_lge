import numpy as np
from matplotlib import pyplot as plt


def plot_gaussian_dist(mean, std, bins=100, N=1000):
    fig = plt.figure(figsize=(10, 6))
    data = np.random.normal(mean, std, N)
    plt.hist(data, bins=bins, alpha=0.5)
    plt.title(f'Histogram with mean={mean} and std={std}')
    plt.xlabel('Value')
    plt.ylabel('Frequency')
    return fig


def plot_uniform_dist(a, b, bins=100, N=1000):
    fig = plt.figure(figsize=(10, 6))
    data = np.random.uniform(a, b, N)
    plt.hist(data, bins=bins, alpha=0.5)
    plt.title(f'Histogram with a={a} and b={b}')
    plt.xlabel('Value')
    plt.ylabel('Frequency')
    return fig
