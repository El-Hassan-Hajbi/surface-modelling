def save_to_obj(filename, points):
    with open(filename, 'w') as obj_file:
        for point in points:
            obj_file.write(f"v {point[0]} {point[1]} 0.0\n")

def convert_coordinates_tkinter_to_matplotlib(tkinter_points, canvas_height):
    matplotlib_points = [(x, canvas_height - y) for x, y in tkinter_points]
    return matplotlib_points

if __name__ == "__main__":
    with open('coordinates.txt', "r") as file:
        coordinates = [tuple(map(float, line.strip().split(','))) for line in file]

    coordinates = convert_coordinates_tkinter_to_matplotlib(coordinates, 506/2)
    save_to_obj('output.obj', coordinates)