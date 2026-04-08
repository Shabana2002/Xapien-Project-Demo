import matplotlib.pyplot as plt
import numpy as np
from q1_mesh import calculate_circumference

# ✅ NEW: Generate a cylinder mesh
def generate_cylinder(radius=1, height=2, segments=40):
    vertices = []
    faces = []

    for i in range(segments):
        angle = 2 * np.pi * i / segments
        x = radius * np.cos(angle)
        y = radius * np.sin(angle)

        vertices.append([x, y, 0])       # bottom
        vertices.append([x, y, height])  # top

    for i in range(segments):
        next_i = (i + 1) % segments

        # Side faces (2 triangles per segment)
        faces.append([2*i, 2*i+1, 2*next_i])
        faces.append([2*i+1, 2*next_i+1, 2*next_i])

    return {"vertices": vertices, "faces": faces}


def visualize(mesh, height_z):
    circumference, points = calculate_circumference(mesh, height_z)

    fig = plt.figure()
    ax = fig.add_subplot(111, projection='3d')

    verts = np.array(mesh['vertices'])
    ax.scatter(verts[:, 0], verts[:, 1], verts[:, 2], alpha=0.2)

    z = height_z

    # ✅ Draw closed loop
    if len(points) > 0:
        for i in range(len(points)):
            x = [points[i][0], points[(i + 1) % len(points)][0]]
            y = [points[i][1], points[(i + 1) % len(points)][1]]
            ax.plot(x, y, [z, z], color='red', linewidth=2)

    plt.title(f"Circumference: {circumference:.2f}")
    plt.savefig("output.png")
    plt.show()


if __name__ == "__main__":
    # ✅ USE CYLINDER INSTEAD OF 2 TRIANGLES
    mesh = generate_cylinder(radius=1, height=2, segments=50)

    visualize(mesh, 1.0)