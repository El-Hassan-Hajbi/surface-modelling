import triangle as tr
import matplotlib.tri as mtri
import matplotlib.pyplot as plt
import numpy as np
from scipy.spatial import ConvexHull

from utils import convert_coordinates_tkinter_to_matplotlib

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
    polyline_points = convert_coordinates_tkinter_to_matplotlib(polyline_points, 506/2)
    segments = [[i, i+1] for i in range(len(polyline_points)-1)] + [[len(polyline_points)-1, 0]] # (0, 1), (1, 2), ..., (len-1, 0)
    i = np.arange(len(polyline_points))
    segments = np.stack([i, i + 1], axis=1) % len(polyline_points)
    print(segments)
    polyline_points = np.array(polyline_points)
    B = tr.triangulate({'vertices':polyline_points, "segments": segments}, opts='qa1000')
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

def test4(filename):
    # Extract x and y coordinates from the list of points
    with open(filename, "r") as file:
        polyline_points = [tuple(map(float, line.strip().split(','))) for line in file]
    polyline_points = convert_coordinates_tkinter_to_matplotlib(polyline_points, 506/2)
    polyline_points = np.array(polyline_points)

    # Extract x and y coordinates from the list of points
    x, y = polyline_points[:, 0], polyline_points[:, 1]

    # Create a triangulation from the points
    triang = mtri.Triangulation(x, y)

    # Get the convex hull of the points
    hull = ConvexHull(polyline_points)

    # Mask triangles outside the convex hull
    triang.set_mask(np.any(np.isin(triang.triangles, hull.simplices), axis=1))

    # Plot the triangulation
    plt.triplot(triang, 'bo-')
    plt.plot(x, y, 'ro')  # Plot the original points in red

    # Plot the convex hull
    plt.plot(x[hull.vertices], y[hull.vertices], 'k-', linewidth=2)

    plt.title('Triangular Mesh Inside Contour')
    plt.xlabel('X-axis')
    plt.ylabel('Y-axis')
    plt.show()

def test5():
    def circle(N, R):
        i = np.arange(N)
        theta = i * 2 * np.pi / N
        pts = np.stack([np.cos(theta), np.sin(theta)], axis=1) * R
        seg = np.stack([i, i + 1], axis=1) % N
        return pts, seg


    pts0, seg0 = circle(30, 1.4)
    pts1, seg1 = circle(16, 0.6)
    pts = np.vstack([pts0, pts1])
    seg = np.vstack([seg0, seg1 + seg0.shape[0]])
    print(pts)

    A = dict(vertices=pts, segments=seg, holes=[[0, 0]])
    B = tr.triangulate(A, 'qpa0.05')
    tr.compare(plt, A, B)
    plt.show()
    
def test6():
    pts = np.loadtxt("img.txt")
    segments = [[i, i+1] for i in range(len(pts)-1)] + [[len(pts)-1, 0]] # (0, 1), (1, 2), ..., (len-1, 0)
    i = np.arange(len(pts))
    segments = np.stack([i, i + 1], axis=1) % len(pts)
    B = tr.triangulate({'vertices':pts, 'segments':segments}, 'qpa400')
    tr.compare(plt, {'vertices':pts}, B)
    plt.show()  
def mesh(points, contour, option):
    return tr.triangulate({'vertices': points, 'segments': contour}, opts=option)

if __name__ == "__main__":
 
    #test1()
    #test2("coordinates.txt")
    #test3()
    #test4("square.txt")
    #test5()    
    test6()