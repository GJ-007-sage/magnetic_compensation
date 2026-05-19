# ============================================================
# MAGNETIC FIELD CONTROLLER
# ============================================================

import numpy as np
from pathlib import Path

# ============================================================
# LOAD A MATRIX
# ============================================================

project_root = Path(__file__).resolve().parent.parent

data_dir = project_root / "data"

A = np.load(data_dir / "A.npy")

# ============================================================
# BUILD REDUCED MATRIX
# ============================================================

A_red = np.column_stack([

    A[:,0],                  # X1
    A[:,1],                  # X2
    A[:,2],                  # X3

    A[:,3] + A[:,4],         # Y grouped

    A[:,5] + A[:,6]          # Z grouped
])

# ============================================================
# AMBIENT FIELD
# ============================================================

B_ambient = np.array([

    -283.38,
     106.79,
    -381.21
])

# ============================================================
# USER INPUT
# ============================================================

print("\n========================================")
print(" MAGNETIC FIELD CONTROLLER ")
print("========================================\n")

Bx_in = float(input("Desired Bx at PMTs (mG): "))
By_in = float(input("Desired By at PMTs (mG): "))
Bz_in = float(input("Desired Bz at PMTs (mG): "))

B_in = np.array([

    Bx_in,
    By_in,
    Bz_in
])

# ============================================================
# REQUIRED COIL FIELD
# ============================================================

target_single = B_in - B_ambient

# ============================================================
# BUILD TARGET VECTOR
# ============================================================

Bx_target = np.full(6, target_single[0])
By_target = np.full(6, target_single[1])
Bz_target = np.full(6, target_single[2])

B_target = np.concatenate([

    Bx_target,
    By_target,
    Bz_target
])

# ============================================================
# SOLVE LEAST SQUARES
# ============================================================

I_opt, residuals, rank, s = np.linalg.lstsq(

    A_red,
    B_target,

    rcond=None
)

# ============================================================
# PRINT RESULTS
# ============================================================

labels = [

    'X1',
    'X2',
    'X3',

    'Y_group',
    'Z_group'
]

print("\n========================================")
print(" OPTIMIZED CURRENTS ")
print("========================================\n")

for name, current in zip(labels, I_opt):

    print(f"{name:10s} : {current:8.2f} A")

# ============================================================
# VALIDATION
# ============================================================

B_coils = A_red @ I_opt

Bx_total = B_coils[0:6]   + B_ambient[0]
By_total = B_coils[6:12]  + B_ambient[1]
Bz_total = B_coils[12:18] + B_ambient[2]

print("\n========================================")
print(" RESULTING FIELD AT PMTs ")
print("========================================")

for i in range(6):

    Bmag = np.sqrt(

        Bx_total[i]**2 +
        By_total[i]**2 +
        Bz_total[i]**2
    )

    print(f"\nPMT{i+1}")

    print("-"*30)

    print(f"Bx   = {Bx_total[i]:8.2f} mG")
    print(f"By   = {By_total[i]:8.2f} mG")
    print(f"Bz   = {Bz_total[i]:8.2f} mG")

    print(f"|B|  = {Bmag:8.2f} mG")