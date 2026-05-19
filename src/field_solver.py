import numpy as np

mu0 = 4 * np.pi * 1e-7
N_turns = 1

def compute_B_field(point, segment_centers, dl_vectors, current=1.0):

    B_total = np.zeros(3)

    for r0, dl in zip(segment_centers, dl_vectors):

        r_vec = point - r0
        r_mag = np.linalg.norm(r_vec)

        if r_mag < 1e-12:
            continue

        dB = (
            mu0 * N_turns * current / (4 * np.pi)
            * np.cross(dl, r_vec)
            / r_mag**3
        )

        B_total += dB

    return B_total


def total_field_at_point(point, coils, currents):

    B_total = np.zeros(3)

    for coil_name in coils:

        segment_centers, dl_vectors = coils[coil_name]

        I = currents[coil_name]

        B = compute_B_field(
            point,
            segment_centers,
            dl_vectors,
            current=I
        )

        B_total += B

    return B_total