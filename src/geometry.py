import numpy as np

def generate_rectangular_loop(
    start_point,
    width,
    height,
    plane='xy',
    segments_per_side=100):

    x0, y0, z0 = start_point

    segment_centers = []
    dl_vectors = []

    if plane == 'xy':

        ys = np.linspace(y0, y0 - height, segments_per_side, endpoint=False)
        dy = -height / segments_per_side

        for y in ys:
            segment_centers.append([x0, y + dy/2, z0])
            dl_vectors.append([0, dy, 0])

        xs = np.linspace(x0, x0 + width, segments_per_side, endpoint=False)
        dx = width / segments_per_side

        for x in xs:
            segment_centers.append([x + dx/2, y0 - height , z0])
            dl_vectors.append([dx, 0, 0])

        ys = np.linspace(y0 - height, y0, segments_per_side, endpoint=False)

        for y in ys:
            segment_centers.append([x0 + width, y - dy/2, z0])
            dl_vectors.append([0, -dy, 0])

        xs = np.linspace(x0 + width, x0, segments_per_side, endpoint=False)

        for x in xs:
            segment_centers.append([x - dx/2, y0, z0])
            dl_vectors.append([-dx, 0, 0])



    elif plane == 'yz':

        ys = np.linspace(y0, y0 + width, segments_per_side, endpoint=False)
        dy = width / segments_per_side

        for y in ys:
            segment_centers.append([x0, y + dy/2, z0])
            dl_vectors.append([0, dy, 0])

        zs = np.linspace(z0, z0 + height, segments_per_side, endpoint=False)
        dz = height / segments_per_side

        for z in zs:
            segment_centers.append([x0, y0 + width, z + dz/2])
            dl_vectors.append([0, 0, dz])

        ys = np.linspace(y0 + width, y0, segments_per_side, endpoint=False)

        for y in ys:
            segment_centers.append([x0, y - dy/2, z0 + height])
            dl_vectors.append([0, -dy, 0])

        zs = np.linspace(z0 + height, z0, segments_per_side, endpoint=False)

        for z in zs:
            segment_centers.append([x0, y0, z - dz/2])
            dl_vectors.append([0, 0, -dz])

    elif plane == 'xz':

        zs = np.linspace(z0, z0 + height, segments_per_side, endpoint=False)
        dz = height / segments_per_side

        for z in zs:
            segment_centers.append([x0, y0, z + dz/2])
            dl_vectors.append([0, 0, dz])

        xs = np.linspace(x0, x0 + width, segments_per_side, endpoint=False)
        dx = width / segments_per_side

        for x in xs:
            segment_centers.append([x + dx/2, y0, z0 + height])
            dl_vectors.append([dx, 0, 0])

        zs = np.linspace(z0 + height, z0, segments_per_side, endpoint=False)

        for z in zs:
            segment_centers.append([x0 + width, y0, z - dz/2])
            dl_vectors.append([0, 0, -dz])

        xs = np.linspace(x0 + width, x0, segments_per_side, endpoint=False)

        for x in xs:
            segment_centers.append([x - dx/2, y0, z0])
            dl_vectors.append([-dx, 0, 0])

        

    return np.array(segment_centers), np.array(dl_vectors)