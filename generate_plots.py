"""Generate publication-quality sensor data visualizations.

This script creates synthetic temperature sensor data using NumPy
and produces scatter, histogram, and box plot visualizations saved
as PNG files.

Usage
-----
    python generate_plots.py
"""

import numpy as np


def generate_data(seed):
    """Generate synthetic temperature sensor readings.

    Parameters
    ----------
    seed : int or None
        Random seed passed to ``np.random.default_rng`` for reproducible
        synthetic data.

    Returns
    -------
    sensor_a : numpy.ndarray
        Array of 200 simulated Sensor A temperature readings in Celsius.
    sensor_b : numpy.ndarray
        Array of 200 simulated Sensor B temperature readings in Celsius.
    timestamps : numpy.ndarray
        Array of 200 timestamps uniformly sampled from 0 to 10 seconds,
        sorted in ascending order.
    """
    rng = np.random.default_rng(seed)

    timestamps = np.sort(rng.uniform(0, 10, 200))
    sensor_a = rng.normal(loc=25.0, scale=3.0, size=200)
    sensor_b = rng.normal(loc=27.0, scale=4.5, size=200)

    return sensor_a, sensor_b, timestamps


def plot_scatter(sensor_a, sensor_b, timestamps, ax):
    """Draw scatter points for two sensors on an existing Axes.

    Parameters
    ----------
    sensor_a : numpy.ndarray
        1D array of Sensor A temperature values in Celsius.
    sensor_b : numpy.ndarray
        1D array of Sensor B temperature values in Celsius.
    timestamps : numpy.ndarray
        1D array of time values in seconds corresponding to the readings.
    ax : matplotlib.axes.Axes
        Axes object on which to draw the scatter plot.

    Returns
    -------
    None
        The function modifies ``ax`` in place and returns nothing.
    """
    ax.scatter(timestamps, sensor_a, color='tab:blue', alpha=0.7, label='Sensor A')
    ax.scatter(timestamps, sensor_b, color='tab:orange', alpha=0.7, label='Sensor B')

    ax.set_title('Sensor Temperature vs Time')
    ax.set_xlabel('Time (s)')
    ax.set_ylabel('Temperature (°C)')
    ax.legend()
    ax.grid(alpha=0.3)
    return None


def plot_histogram(sensor_a, sensor_b, timestamps, ax):
    """Draw overlaid histograms for two sensor temperature distributions.

    Parameters
    ----------
    sensor_a : numpy.ndarray
        1D array of Sensor A temperature values in Celsius.
    sensor_b : numpy.ndarray
        1D array of Sensor B temperature values in Celsius.
    timestamps : numpy.ndarray
        1D array of time values in seconds corresponding to the readings.
        This parameter is included for compatibility but is not used in
        the histogram itself.
    ax : matplotlib.axes.Axes
        Axes object on which to draw the histogram.

    Returns
    -------
    None
        The function modifies ``ax`` in place and returns nothing.
    """
    ax.hist(sensor_a, bins=30, alpha=0.5, color='tab:blue', label='Sensor A')
    ax.hist(sensor_b, bins=30, alpha=0.5, color='tab:orange', label='Sensor B')

    mean_a = sensor_a.mean()
    mean_b = sensor_b.mean()
    ax.axvline(mean_a, color='tab:blue', linestyle='--', linewidth=1.5)
    ax.axvline(mean_b, color='tab:orange', linestyle='--', linewidth=1.5)

    ax.set_title('Sensor Temperature Distributions')
    ax.set_xlabel('Temperature (°C)')
    ax.set_ylabel('Count')
    ax.legend()
    ax.grid(alpha=0.3)
    return None