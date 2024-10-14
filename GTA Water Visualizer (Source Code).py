import tkinter as tk
from tkinter import filedialog, messagebox, ttk
import matplotlib.pyplot as plt
import numpy as np
from threading import Thread
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg

class WaterEditorApp:
    def __init__(self, master):
        self.master = master
        self.master.title("Water Data Editor")
        self.data = []

        # Create main frame
        self.main_frame = tk.Frame(self.master, padx=10, pady=10)
        self.main_frame.pack(fill=tk.BOTH, expand=True)

        # Create initial panel
        self.create_initial_panel()

        # Bind the F11 key to toggle full screen
        self.master.bind("<F11>", self.toggle_fullscreen)

    def create_initial_panel(self):
        """Create and place the initial instruction panel."""
        instruction_label = tk.Label(self.main_frame, text="Load water.dat file to visualize the water shapes.")
        instruction_label.pack(pady=5)

        # Load button
        self.load_button = tk.Button(self.main_frame, text="Load water.dat", command=self.load_file)
        self.load_button.pack(pady=5)

        # Visualize button (hidden until file is loaded)
        self.visualize_button = tk.Button(self.main_frame, text="Visualize", command=self.visualize_data)
        self.visualize_button.pack(pady=5)
        self.visualize_button.config(state=tk.DISABLED)

    def load_file(self):
        """Load data from a .dat file."""
        filename = filedialog.askopenfilename(filetypes=[("Data Files", "*.dat")])
        if filename:
            try:
                with open(filename, 'r') as file:
                    self.data = [line.strip() for line in file if line.strip() and not line.startswith('#')]
                messagebox.showinfo("Load Success", "File loaded successfully!")
                # Enable the Visualize button
                self.visualize_button.config(state=tk.NORMAL)
            except Exception as e:
                messagebox.showerror("Load Error", f"Failed to load file: {e}")

    def visualize_data(self):
        """Visualize the water shapes in a separate window."""
        self.visualization_window = tk.Toplevel(self.master)
        self.visualization_window.title("Water Shapes Visualization")
        self.create_visualization_ui()
        
        Thread(target=self.visualize_data_thread).start()

    def create_visualization_ui(self):
        """Set up the visualization UI components."""
        # Create a frame for parameters
        param_frame = tk.Frame(self.visualization_window)
        param_frame.pack(side=tk.LEFT, fill=tk.Y, padx=5, pady=5)

        # Label for parameters
        param_label = tk.Label(param_frame, text="Select Parameter to Visualize:")
        param_label.pack(pady=5)

        # Listbox to display parameters
        self.param_listbox = tk.Listbox(param_frame)
        self.param_listbox.pack(fill=tk.Y, padx=5, pady=5, expand=True)

        # Populate the listbox with parameters
        unique_params = set(int(line.split()[-1]) for line in self.data if len(line.split()) > 8)
        for param in sorted(unique_params):
            self.param_listbox.insert(tk.END, param)

        # Create a button to visualize selected parameter
        visualize_param_button = tk.Button(param_frame, text="Visualize Selected Parameter", command=self.visualize_selected_param)
        visualize_param_button.pack(pady=5)

        # Create a frame for the plot
        self.plot_frame = tk.Frame(self.visualization_window)
        self.plot_frame.pack(side=tk.RIGHT, fill=tk.BOTH, expand=True)

        # Create a placeholder for the plot
        self.fig, self.ax = plt.subplots()
        self.canvas = FigureCanvasTkAgg(self.fig, master=self.plot_frame)
        self.canvas.get_tk_widget().pack(fill=tk.BOTH, expand=True)

    def visualize_selected_param(self):
        """Visualize the selected parameter from the listbox."""
        selected_param = self.param_listbox.get(self.param_listbox.curselection())
        self.ax.clear()  # Clear previous plots
        self.ax.set_title("Water Shapes Visualization")
        self.ax.set_xlabel("X Coordinate")
        self.ax.set_ylabel("Y Coordinate")
        self.ax.grid()

        for line in self.data:
            parts = line.split()
            if len(parts) < 8:  # Ensure there are enough parts for points and parameter
                continue
            
            param = int(parts[-1])  # Water type parameter
            if param != selected_param:
                continue  # Skip if it doesn't match the selected parameter

            points = np.array([list(map(float, parts[i:i + 7])) for i in range(0, len(parts) - 1, 7)])

            # Assign color based on the parameter value
            color = {0: 'blue', 1: 'green', 2: 'orange', 3: 'red'}.get(param, 'black')
            self.ax.fill(points[:, 0], points[:, 1], color=color, alpha=0.5, label=f'Param {param}')

        self.ax.legend()
        self.canvas.draw()

    def toggle_fullscreen(self, event=None):
        """Toggle full screen mode."""
        is_fullscreen = self.master.attributes("-fullscreen")
        self.master.attributes("-fullscreen", not is_fullscreen)
        self.master.bind("<Escape>", self.end_fullscreen)

    def end_fullscreen(self, event=None):
        """End full screen mode."""
        self.master.attributes("-fullscreen", False)

if __name__ == "__main__":
    root = tk.Tk()
    app = WaterEditorApp(root)
    root.mainloop()