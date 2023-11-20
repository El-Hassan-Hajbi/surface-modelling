import matplotlib.pyplot as plt
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg
import tkinter as tk

class Application:
    def __init__(self, master):
        self.master = master
        self.master.title("Matplotlib Application")

        # Create a Matplotlib figure
        self.fig, self.ax = plt.subplots()
        self.canvas = FigureCanvasTkAgg(self.fig, master=self.master)
        self.canvas.get_tk_widget().pack(expand=tk.YES, fill=tk.BOTH)

        # Bind the mouse click event to the function
        self.canvas.mpl_connect("button_press_event", self.on_click)

        # Use protocol to bind the method to the window close event
        self.master.protocol("WM_DELETE_WINDOW", self.on_close)

        # List to store the points
        self.points = []

        # Flag to check if the limits have been set
        self.limits_set = False

    def on_click(self, event):
        # Get the coordinates of the mouse click
        x, y = event.xdata, event.ydata

        # Check if the click is within the plot area
        if x is not None and y is not None:
            # Plot a point at the clicked coordinates
            self.ax.plot(x, y, 'ro')  # 'ro' means red color, round marker
            self.canvas.draw()

            # Save the point to the list
            self.points.append((x, y))

            # Set fixed limits only once
            if not self.limits_set:
                self.set_fixed_limits()
                self.limits_set = True

    def set_fixed_limits(self):
        # Set fixed limits for the x and y axes
        self.ax.set_xlim([0, 10])  # Adjust these values according to your needs
        self.ax.set_ylim([0, 10])
        self.canvas.draw()

    def on_close(self):
        # Save the points to a file when the window is closed
        self.save_to_file()
        self.master.destroy()

    def save_to_file(self):
        # Save the points to a file (e.g., points.txt)
        with open("points.txt", "w") as file:
            for point in self.points:
                file.write(f"{point[0]}, {point[1]}\n")

if __name__ == "__main__":
    root = tk.Tk()
    app = Application(root)
    root.mainloop()
