import numpy as np

def calculate_circumference(mesh, height_z):
    vertices = np.array(mesh['vertices'])
    faces = mesh['faces']
    intersections = []

    for face in faces:
        tri = vertices[face]

        for i in range(3):
            p1 = tri[i]
            p2 = tri[(i + 1) % 3]

            z1, z2 = p1[2], p2[2]

            # Check if edge crosses the plane
            if (z1 - height_z) * (z2 - height_z) < 0:
                if z2 != z1:  # avoid division by zero
                    t = (height_z - z1) / (z2 - z1)
                    point = p1 + t * (p2 - p1)
                    intersections.append(point[:2])

    if len(intersections) < 3:
        return 0, []

    intersections = np.array(intersections)

    # Remove duplicate points (important for cleaner loop)
    intersections = np.unique(intersections, axis=0)

    center = intersections.mean(axis=0)

    angles = np.arctan2(
        intersections[:, 1] - center[1],
        intersections[:, 0] - center[0]
    )

    sorted_points = intersections[np.argsort(angles)]

    circumference = 0
    for i in range(len(sorted_points)):
        p1 = sorted_points[i]
        p2 = sorted_points[(i + 1) % len(sorted_points)]
        circumference += np.linalg.norm(p1 - p2)

    return circumference, sorted_points