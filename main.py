import tkinter as tk
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg
import triangle
import matplotlib.pyplot as plt

class Application:
    def __init__(self, master):
        self.master = master
        self.master.title("Tkinter Application with Triangle Plot")

        # Example of points forming a rectangle
        self.points = [(0, 0), (0, 1), (1, 1), (1, 0)]

        # Example of segments defining part of the rectangle
        self.segments = [(0, 1), (1, 2)]

        # Perform triangulation
        self.mesh = triangle.triangulate({'vertices': self.points, 'segments': self.segments}, opts='qa0.05')

        # Create Matplotlib figure
        self.fig, self.ax = plt.subplots()

        # Embed Matplotlib plot into Tkinter
        self.canvas = FigureCanvasTkAgg(self.fig, master=self.master)
        self.canvas.get_tk_widget().pack(expand=tk.YES, fill=tk.BOTH)

        # Plot the mesh
        triangle.plot(self.ax, **self.mesh)

        # Bind the mouse click event to a function
        self.canvas.mpl_connect("button_press_event", self.on_click)

    def on_click(self, event):
        # Get the coordinates of the mouse click
        x, y = event.xdata, event.ydata

        # Check if the click is within the plot area
        if x is not None and y is not None:
            # Plot a point at the clicked coordinates
            self.ax.plot(x, y, 'ro')  # 'ro' means red color, round marker
            self.canvas.draw()

if __name__ == "__main__":
    root = tk.Tk()
    app = Application(root)
    root.mainloop()
