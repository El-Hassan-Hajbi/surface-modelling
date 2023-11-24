import numpy as np

def laplacian_matrix(vertices, faces):
    num_vertices = len(vertices)
    L = np.zeros((num_vertices, num_vertices))

    for face in faces:
        i, j, k = face
        L[i, i] += 1
        L[j, j] += 1
        L[k, k] += 1
        L[i, j] = L[j, i] = -1
        L[i, k] = L[k, i] = -1
        L[j, k] = L[k, j] = -1

    return L

def params(vertices, triangles, handles, s):
    A, b, V, w = [], [], len(vertices), 100
    for t in triangles: # On parcours tous les triangles
        # t = [a, b, c]
        # On a 3 arretes e pour un triangle donnée t 

        # 1ere arrete :
        L, i, j = V*[0], t[0], t[1]
        L[i], L[j] = 1, -1
        A.append(L)
        b.append(vertices[i][s] - vertices[j][s] )

        # 2eme arrete :
        L, i, j = V*[0], t[1], t[2]
        L[i], L[j] = 1, -1
        A.append(L)
        b.append(vertices[i][s]  - vertices[j][s] )

        # 3eme arrete :
        L, i, j = V*[0], t[2], t[0]
        L[i], L[j] = 1, -1
        A.append(L)
        b.append(vertices[i][s]  - vertices[j][s] )

    C = [] # positions of the handles in vertices
    for i,v in enumerate(vertices):
        res = np.any([np.array_equal(v, row) for row in handles])
        if res:
            C.append(i)
    
    for i, Ci in enumerate(C): # i tel que Vi est un handle
        L = V*[0]
        L[i], Ci = w, vertices[Ci][s] 
        A.append(L)
        b.append(-w*Ci)

    return np.array(A), np.array(b)

def laplacian_surface_editing(vertices, triangles, handles):
    Ax, bx = params(vertices, triangles, handles, s=0)
    Ay, by = params(vertices, triangles, handles, s=1)

    # Solving for x coordinates
    Vx = np.linalg.lstsq(Ax, bx, rcond=None)[0]

    # Solving for y coordinates
    Vy = np.linalg.lstsq(Ay, by, rcond=None)[0]

    V = np.column_stack((Vx, Vy))

    return V

# Example usage:
vertices = np.array([[0, 0], [1, 0], [1, 1], [0, 1]])
handles = np.array([[0, 0]])
triangles = np.array([[0, 1, 2]])

deformed_vertices = laplacian_surface_editing(vertices, triangles, handles)

