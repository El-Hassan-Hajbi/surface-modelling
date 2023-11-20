import tkinter as tk
import triangle as tr

class Application:
    def __init__(self, master, filename):
        self.master = master
        self.master.title("Interface Graphique 2D")
        
        self.filename = filename

        self.canvas = tk.Canvas(self.master, width=500, height=500, bg="white")
        self.canvas.pack(expand=tk.YES, fill=tk.BOTH)
        
        self.canvas.bind("<B1-Motion>", self.draw_contour)
        self.canvas.bind("<Button-1>", self.handle_click)
        self.canvas.bind("<ButtonRelease-1>", self.handle_release)
        
        self.points = []
        self.fixe_edges = []
        self.handles = []
        self.current_mode = "draw"  # Initial mode is drawing

        # Ajouter un bouton pour changer le mode
        mode_button = tk.Button(self.master, text="Changer Mode", command=self.toggle_mode)
        mode_button.pack()

        # Ajouter un bouton pour charger une polyligne depuis un fichier
        load_button = tk.Button(self.master, text="Charger Polyligne", command=self.load_polyline)
        load_button.pack()

        # Ajouter un bouton pour enregistrer une polyligne dans un fichier
        save_button = tk.Button(self.master, text="Save", command=self.save_coordinates)
        save_button.pack()

        # Visualisation du triangular mesh
        # Ajouter un bouton pour changer le mode
        mesh_button = tk.Button(self.master, text=" Triangular Mesh", command=self.visualize_mesh)
        mesh_button.pack()
    def draw_contour(self, event):
        if self.current_mode == "draw":
            x, y = event.x, event.y
            self.points.append((x, y))
            self.canvas.create_oval(x-2, y-2, x+2, y+2, fill="black", tags="point")
            if len(self.points) > 1:
                self.canvas.create_line(self.points[-2], x, y, fill="black")
        elif self.current_mode == "select":
            # Implement logic for moving the selected point in select mode
            self.move_selected_point(event.x, event.y)

    def handle_click(self, event):
        #print("handle click",event.x, event.y)
        if self.current_mode == "select":
            # Find the selected point in select mode
            size = 5
            self.canvas.create_oval(event.x-size, event.y-size, event.x+size, event.y+size, fill="black")
            self.fixe_edges.append((event.x, event.y))

    def handle_release(self, event):
        #print("handle release",event.x, event.y)
        if self.current_mode == "move":
            # Clear the selected point after releasing the mouse button
            size = 5
            self.canvas.create_oval(event.x-size, event.y-size, event.x+size, event.y+size, fill="green")
            self.handles.append((event.x, event.y))

    def move_selected_point(self, x, y):
        if hasattr(self, 'selected_point') and self.selected_point is not None:
            dx = x - self.drag_data["x"]
            dy = y - self.drag_data["y"]
            self.canvas.move(self.selected_point, dx, dy)
            self.drag_data["x"] = x
            self.drag_data["y"] = y

    def toggle_mode(self):
        # Toggle between draw and select modes
        if self.current_mode == "draw":
            self.current_mode = "select"
        elif self.current_mode == "select":
            self.current_mode = "move"
        else:
            self.current_mode = "draw"

    def save_coordinates(self):
        with open(self.filename, "w") as file:
            for point in self.points:
                file.write(f"{point[0]}, {point[1]}\n")

        # Fermer la fenêtre
        self.master.destroy()

    def load_polyline(self):
        filename = self.filename
        self.points = []
        if filename:
            with open(filename, "r") as file:
                polyline_points = [tuple(map(float, line.strip().split(','))) for line in file]
                self.points.append(polyline_points)
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

    def get_selected_point(self, x, y):
        # Retourne l'ID du point si (x, y) est à proximité d'un point, sinon retourne None
        for point_id in self.points:
            point_id = point_id[0]
            #point_coords = self.canvas.coords(point_id)
            dist = self.point_distance(x, y, point_id[0], point_id[1])
            if dist < 5:  # Ajustez la tolérance selon vos besoins
                return point_id
        return None

    def point_distance(self, x1, y1, x2, y2):
        return ((x1 - x2)**2 + (y1 - y2)**2)**0.5
    
    def visualize_mesh(self):
        # Load polyline points and segments from the file
        with open(self.filename, "r") as file:
            polyline_points = [tuple(map(float, line.strip().split(','))) for line in file]
        segments = [(i, i+1) for i in range(len(polyline_points)-1)] + [(len(polyline_points)-1, 0)]

        # Triangulate
        B = tr.triangulate({'vertices': polyline_points, 'segments': segments}, opts='qa100000')

        # Draw the triangular mesh on the canvas
        for triangle in B['triangles']:
            for i in range(3):
                x1, y1 = polyline_points[triangle[i % 3]% len(polyline_points)]
                x2, y2 = polyline_points[triangle[(i + 1) % 3]% len(polyline_points)]
                self.canvas.create_line(x1, y1, x2, y2, fill="blue")

if __name__ == "__main__":
    root = tk.Tk()
    app = Application(root, "coordinates.txt")
    root.mainloop()
