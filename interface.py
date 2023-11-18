import tkinter as tk

class Application:
    def __init__(self, master):
        self.master = master
        self.master.title("Interface Graphique 2D")
        
        self.canvas = tk.Canvas(self.master, width=500, height=500, bg="white")
        self.canvas.pack(expand=tk.YES, fill=tk.BOTH)
        
        self.canvas.bind("<B1-Motion>", self.draw_contour)
        self.canvas.bind("<Button-1>", self.move_point)
        
        self.points = []

        # Ajouter un bouton pour charger une polyligne depuis un fichier
        load_button = tk.Button(self.master, text="Charger Polyligne", command=self.load_polyline)
        load_button.pack()

        # Ajouter un bouton pour enregistrer une polyligne dans un fichier
        save_button = tk.Button(self.master, text="Save", command=self.save_coordinates)
        save_button.pack()

    def draw_contour(self, event):
        x, y = event.x, event.y
        self.points.append((x, y))
        self.canvas.create_oval(x-2, y-2, x+2, y+2, fill="black")
        if len(self.points) > 1:
            self.canvas.create_line(self.points[-2], x, y, fill="black")

    def move_point(self, event):
        x, y = event.x, event.y
        # Implémentez ici la logique pour déplacer un point du maillage

    def save_coordinates(self):
        with open("coordinates.txt", "w") as file:
            for point in self.points:
                file.write(f"{point[0]}, {point[1]}\n")

        # Fermer la fenêtre
        self.master.destroy()

    def load_polyline(self):
        filename = "coordinates.txt"
        if filename:
            with open(filename, "r") as file:
                polyline_points = [tuple(map(float, line.strip().split(','))) for line in file]

            self.draw_polyline(polyline_points)

    def draw_polyline(self, points):
        # Dessiner la polyligne sur le canevas
        for point in points:
            x, y = point
            if point in self.points:
                self.canvas.create_oval(x-2, y-2, x+2, y+2, fill="green")
            else:
                self.canvas.create_oval(x-2, y-2, x+2, y+2, fill="red")

        self.canvas.create_line(points, points[0], fill="blue")

if __name__ == "__main__":
    root = tk.Tk()
    app = Application(root)
    root.mainloop()
