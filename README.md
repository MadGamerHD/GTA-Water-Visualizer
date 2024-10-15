Certainly! Here's a version of the **GTA Water Visualizer (Source Code)** tool description and installation instructions tailored for GitHub, without mentioning cloning:

---

# GTA Water Visualizer (Source Code)

## Overview:
The **GTA Water Visualizer** is a Python-based tool designed to help visualize water data from `.dat` files, commonly used in the **Grand Theft Auto** series for modding and development purposes. It provides a user-friendly graphical interface to load `.dat` files, select water type parameters, and visualize water shapes in 2D plots.

With this tool, you can quickly load water data, filter it by parameter, and observe the corresponding water shapes in a plot. This is useful for modders and developers working with custom water areas in **GTA** environments.

## Features:
- **File Loader**: Easily load `.dat` files containing water data.
- **Water Shape Visualization**: View water shapes in a 2D plot.
- **Interactive Parameter Selection**: Filter and visualize shapes based on specific water type parameters.
- **Fullscreen Mode**: Press F11 to toggle fullscreen for easier viewing.
- **Previous File Memory**: Remembers the last opened file path for quick access.

## Prerequisites:
Before running the **GTA Water Visualizer**, ensure that you have Python installed. You can download it from the official Python website:
[Python Download](https://www.python.org/)

## Installation:

To get the tool working, follow these simple steps:

### 1. Install Required Libraries

The tool uses the following Python libraries:
- **Tkinter** (built-in with Python) for the graphical interface.
- **Matplotlib** for creating visualizations.
- **Numpy** for handling numerical operations.

You can install the required libraries via `pip`:

```bash
pip install matplotlib numpy
```

### 2. Download the Source Code

Download the `GTA Water Visualizer (Source Code)` as a ZIP file from the repository and extract it to a folder on your computer.

### 3. Running the Tool

Once the required libraries are installed and the source code is downloaded:
- Navigate to the folder where the source code is located.
- Open a terminal or command prompt and run the following command:

```bash
python "GTA Water Visualizer.py"
```

This will launch the graphical interface of the **GTA Water Visualizer**.

## Usage:

1. **Open the Tool**: Launch the application by running the script.
2. **Load a Water Data File**: Click the "Load water.dat" button to browse and load a `.dat` file containing water data.
3. **Visualize the Data**: Once the file is loaded, click "Visualize" to open the visualization window.
4. **Select Parameters**: Choose a parameter from the list to filter the water shapes you want to visualize.
5. **View Water Shapes**: The selected water shapes will be displayed in the plot area.

### Fullscreen Mode:
- Toggle fullscreen by pressing **F11**.
- Press **Escape** to exit fullscreen.

### File Path Memory:
- The tool automatically remembers the last file you loaded, making it easy to reopen your last session.
