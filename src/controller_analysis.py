# ============================================================
# CONTROLLER ANALYSIS UTILITIES
# ============================================================

import numpy as np
import matplotlib.pyplot as plt

# ============================================================
# BUILD REDUCED MATRIX
# ============================================================

def build_reduced_matrix(A):

    A_red = np.column_stack([

        A[:,0],              # X1
        A[:,1],              # X2
        A[:,2],              # X3

        A[:,3] + A[:,4],     # Y grouped

        A[:,5] + A[:,6]      # Z grouped
    ])

    return A_red

# ============================================================
# RUN COMPONENT SCAN
# ============================================================

def run_component_scan(

    A,

    B_ambient,

    component='Bx',

    scan_values=np.arange(0,301,50)
):

    # --------------------------------------------------------
    # BUILD REDUCED MATRIX
    # --------------------------------------------------------

    A_red = build_reduced_matrix(A)

    # --------------------------------------------------------
    # STORAGE
    # --------------------------------------------------------

    actual_mean = []

    actual_rms = []

    currents_all = []

    # --------------------------------------------------------
    # COMPONENT INDEX
    # --------------------------------------------------------

    comp_index = {

        'Bx': 0,
        'By': 1,
        'Bz': 2
    }

    idx = comp_index[component]

    # --------------------------------------------------------
    # MAIN LOOP
    # --------------------------------------------------------

    for target in scan_values:

        # ----------------------------------------------------
        # USER TARGET FIELD
        # ----------------------------------------------------

        B_in = np.array([0.0, 0.0, 0.0])

        B_in[idx] = target

        # ----------------------------------------------------
        # FIELD REQUIRED FROM COILS
        # ----------------------------------------------------

        target_single = B_in - B_ambient

        # ----------------------------------------------------
        # BUILD TARGET VECTOR
        # ----------------------------------------------------

        Bx_vec = np.full(

            6,
            target_single[0]
        )

        By_vec = np.full(

            6,
            target_single[1]
        )

        Bz_vec = np.full(

            6,
            target_single[2]
        )

        B_target = np.concatenate([

            Bx_vec,
            By_vec,
            Bz_vec
        ])

        # ----------------------------------------------------
        # SOLVE LEAST-SQUARES
        # ----------------------------------------------------

        I_opt, residuals, rank, s = np.linalg.lstsq(

            A_red,
            B_target,
            rcond=None
        )

        currents_all.append(I_opt)

        # ----------------------------------------------------
        # COIL FIELD
        # ----------------------------------------------------

        B_coil = A_red @ I_opt

        # ----------------------------------------------------
        # AMBIENT VECTOR
        # ----------------------------------------------------

        B_ambient_vec = np.concatenate([

            np.full(6, B_ambient[0]),

            np.full(6, B_ambient[1]),

            np.full(6, B_ambient[2])
        ])

        # ----------------------------------------------------
        # TOTAL FIELD
        # ----------------------------------------------------

        B_actual = B_coil + B_ambient_vec

        # ----------------------------------------------------
        # EXTRACT COMPONENT
        # ----------------------------------------------------

        if component == 'Bx':

            values = B_actual[:6]

        elif component == 'By':

            values = B_actual[6:12]

        elif component == 'Bz':

            values = B_actual[12:18]

        # ----------------------------------------------------
        # STORE
        # ----------------------------------------------------

        actual_mean.append(

            np.mean(values)
        )

        actual_rms.append(

            np.std(values)
        )

        # ----------------------------------------------------
        # PRINT RESULTS
        # ----------------------------------------------------

        print("\n================================================")

        print(f"{component} target = {target:.1f} mG")

        print("\nOptimized currents:")

        print(f"X1 = {I_opt[0]:.2f} A")
        print(f"X2 = {I_opt[1]:.2f} A")
        print(f"X3 = {I_opt[2]:.2f} A")

        print(f"Y  = {I_opt[3]:.2f} A")
        print(f"Z  = {I_opt[4]:.2f} A")

        print(f"\n{component} at PMTs:")

        for i, val in enumerate(values):

            print(f"PMT{i+1}: {val:.2f} mG")

        print()

        print(f"Mean = {np.mean(values):.2f} mG")

        print(f"RMS  = {np.std(values):.2f} mG")

    # --------------------------------------------------------
    # CONVERT TO ARRAYS
    # --------------------------------------------------------

    actual_mean = np.array(actual_mean)

    actual_rms = np.array(actual_rms)

    # --------------------------------------------------------
    # PLOT
    # --------------------------------------------------------

    plt.figure(figsize=(8,6))

    plt.errorbar(

        scan_values,

        actual_mean,

        yerr=actual_rms,

        fmt='o',

        capsize=5,

        linewidth=2,

        label='Simulation'
    )

    # --------------------------------------------------------
    # IDEAL RESPONSE
    # --------------------------------------------------------

    plt.plot(

        scan_values,

        scan_values,

        '--',

        linewidth=2,

        label='Ideal response'
    )

    # --------------------------------------------------------
    # PRINT CENTRAL VALUES
    # --------------------------------------------------------

    for x, y in zip(scan_values, actual_mean):

        plt.text(

            x,

            y + 5,

            f'{y:.1f}',

            fontsize=9,

            ha='center'
        )

    # --------------------------------------------------------
    # LABELS
    # --------------------------------------------------------

    plt.xlabel(

        f'Target {component} (mG)',

        fontsize=13
    )

    plt.ylabel(

        f'Actual Mean {component} (mG)',

        fontsize=13
    )

    plt.title(

        f'Field Controller Response: {component}',

        fontsize=15
    )

    plt.grid(True)

    plt.legend()

    plt.tight_layout()

    plt.show()

    # --------------------------------------------------------
    # RETURN RESULTS
    # --------------------------------------------------------

    return {

        'targets': scan_values,

        'mean': actual_mean,

        'rms': actual_rms,

        'currents': currents_all
    }