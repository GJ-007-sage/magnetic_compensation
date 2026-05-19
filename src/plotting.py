import matplotlib.pyplot as plt

def plot_field_component(field, x_vals, y_vals, title):

    plt.figure(figsize=(7,6))

    plt.imshow(
        field,
        extent=[x_vals.min(), x_vals.max(),
                y_vals.min(), y_vals.max()],
        origin='lower',
        aspect='equal'
    )

    plt.colorbar(label='Tesla')

    plt.xlabel('x (m)')
    plt.ylabel('y (m)')
    plt.title(title)

    plt.show()