import numpy as np

from .geometry import generate_rectangular_loop
mm = 1e-3
segments = 150

coils = {}

# =========================
# X coils (yz plane)
# =========================

x_width = 3532 * mm
x_height = 2025 * mm

coils['X1'] = generate_rectangular_loop(
    start_point=(-1700*mm, -1598*mm, -1004.5*mm),
    width=x_width,
    height=x_height,
    plane='yz',
    segments_per_side=segments
)

coils['X2'] = generate_rectangular_loop(
    start_point=(0*mm, -1598*mm, -1004.5*mm),
    width=x_width,
    height=x_height,
    plane='yz',
    segments_per_side=segments
)

coils['X3'] = generate_rectangular_loop(
    start_point=(1700*mm, -1598*mm, -1004.5*mm),
    width=x_width,
    height=x_height,
    plane='yz',
    segments_per_side=segments
)

# =========================
# Y coils (xz plane)
# =========================

y_width = 3532 * mm #length
y_height = 1975 * mm #height

coils['Y1'] = generate_rectangular_loop(
    start_point=(-1766*mm, 648*mm, -979.5*mm),
    width=y_width,
    height=y_height,
    plane='xz',
    segments_per_side=segments
)

coils['Y2'] = generate_rectangular_loop(
    start_point=(-1766*mm, -1482*mm, -979.5*mm),
    width=y_width,
    height=y_height,
    plane='xz',
    segments_per_side=segments
)

# =========================
# Z coils (xy plane)
# =========================

z_width = 3582 * mm #length 
z_height = 3582 * mm #width

coils['Z1'] = generate_rectangular_loop(
    start_point=(-1791*mm, 1959*mm, 750*mm),
    width=z_width,
    height=z_height,
    plane='xy',
    segments_per_side=segments
)

coils['Z2'] = generate_rectangular_loop(
    start_point=(-1791*mm, 1959*mm, -750*mm),
    width=z_width,
    height=z_height,
    plane='xy',
    segments_per_side=segments
)