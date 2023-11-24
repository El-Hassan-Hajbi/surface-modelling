from scipy.spatial import Delaunay
import numpy as np
import matplotlib.pyplot as plt
from matplotlib.patches import Polygon
from utils import convert_coordinates_tkinter_to_matplotlib

class DelaunayTriangulation:
    def __init__(self, points):
        self.points = points
        self.triangulation = Delaunay(points)

    def plot(self, edges=True, triangles=True, contour_points=None):
        plt.figure(figsize=(8, 8))
        plt.gca().set_aspect('equal', adjustable='box')
        
        if contour_points is not None:
            self.plot_contours(contour_points)

        if edges:
            self.plot_edges()

        if triangles:
            self.plot_triangles()

        plt.show()

    def plot_contours(self, contour_points):
        plt.plot(contour_points[:, 0], contour_points[:, 1], 'k-')

    def plot_edges(self):
        for simplex in self.triangulation.simplices:
            for i in range(3):
                plt.plot([self.points[simplex[i % 3], 0], self.points[simplex[(i + 1) % 3], 0]],
                         [self.points[simplex[i % 3], 1], self.points[simplex[(i + 1) % 3], 1]], 'k-')

    def plot_triangles(self):
        for simplex in self.triangulation.simplices:
            poly = Polygon(self.points[simplex])
            plt.gca().add_patch(poly)

# Exemple d'utilisation
if __name__ == "__main__":
    # Définir vos points ici
    with open("coordinates.txt", "r") as file:
        polyline_points = [tuple(map(float, line.strip().split(','))) for line in file]
    polyline_points = convert_coordinates_tkinter_to_matplotlib(polyline_points, 506/2)
    polyline_points = np.array(polyline_points)

    # Définir les points du contour (par exemple, un rectangle)
    contour_points = polyline_points

    # Créer une instance de la classe DelaunayTriangulation
    triangulation = DelaunayTriangulation(polyline_points)

    # Afficher le maillage avec les contours spécifiés
    triangulation.plot(contour_points=contour_points)
