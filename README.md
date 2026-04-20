# Sensor Plot Generator

A small Python script that generates synthetic temperature sensor data and saves a set of publication-style visualizations.

## Installation

1. Activate the `ece105` conda environment:

   ```bash
   conda activate ece105
   ```

2. Install the required dependencies:

   ```bash
   conda install numpy matplotlib
   ```

   Or, if you prefer `mamba`:

   ```bash
   mamba install numpy matplotlib
   ```

## Usage

Run the script from the project directory:

```bash
python generate_plots.py
```

This will generate the plots and save the output image to the current directory.

## Example output

The script produces a single PNG file containing three side-by-side subplots:

- A scatter plot of Sensor A and Sensor B temperature readings versus time.
- An overlaid histogram showing the temperature distributions of both sensors.
- A box plot comparing the distribution of Sensor A and Sensor B temperatures, with the overall mean indicated.

## AI tools used and disclosure

[Placeholder: describe any AI assistance used in creating this project and any relevant disclosure details.]
