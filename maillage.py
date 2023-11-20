import triangle as tr
import matplotlib.pyplot as plt
import numpy as np

def test1():
    # Exemple de points formant un rectangle
    points = [(0, 0), (0, 1), (1, 1), (1, 0)]

    # Exemple de segments contraints pour définir les bords du rectangle
    segments = [(0, 1), (1, 2), (2, 3), (3, 0)]

    # Réaliser la triangulation avec des segments contraints
    mesh = tr.triangulate({'vertices': points, 'segments': segments}, opts='p')

    # Afficher le maillage
    tr.plot(plt.axes(), **mesh)
    plt.show()

def test2(filename):
    with open(filename, "r") as file:
        polyline_points = [tuple(map(float, line.strip().split(','))) for line in file]
    segments = [(i, i+1) for i in range(len(polyline_points)-1)] + [(len(polyline_points)-1, 0)]
    polyline_points = np.array(polyline_points)
    B = tr.triangulate({'vertices':polyline_points, 'segments':segments}, opts='qa1000')
    tr.compare(plt, {'vertices':polyline_points}, B)
    plt.show()
    # Plot the mesh
    #tr.plot(plt.axes(), **B)
    

def test3():
    N = 112
    theta = np.linspace(0, 2 * np.pi, N, endpoint=False)
    pts = np.stack([np.cos(theta), np.sin(theta)], axis=1)
    A = dict(vertices=pts)
    B = tr.triangulate(A, 'qa0.05')
    tr.compare(plt, A, B)
    plt.show()
if __name__ == "__main__":
 
    test1()
    test2("coordinates.txt")
    test3()