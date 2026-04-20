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
