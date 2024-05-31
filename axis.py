import plotly.graph_objects as go

def plot_3d_skull():
    # 2D ASCII representation of a skull
    skull_ascii = [
        " /\\_/\\",
        "( o.o )",
        " > ^ < "
    ]

    # Calculate the size of the skull to fit within the axis
    skull_size = 4
    scale_factor = 0.5

    # Create a figure
    fig = go.Figure()

    # Create a trace for each line in the ASCII representation
    for y, line in enumerate(skull_ascii):
        for x, char in enumerate(line):
            if char != ' ':
                fig.add_trace(go.Scatter3d(x=[x * scale_factor - skull_size/2], y=[skull_size/2 - y * scale_factor], z=[0],
                                          mode='text', text=[char], textfont=dict(size=10), name='Skull'))

    # Set axis labels and range
    fig.update_layout(scene=dict(
        xaxis_title='X-axis',
        yaxis_title='Y-axis',
        zaxis_title='Z-axis',
        xaxis_range=[-skull_size / 2, skull_size / 2],
        yaxis_range=[-skull_size / 2, skull_size / 2],
        zaxis_range=[-skull_size / 2, skull_size / 2]
    ))

    # Set the aspect ratio to equal
    fig.update_layout(scene_aspectmode='cube')

    # Hide axes ticks and grid lines
    fig.update_layout(scene_xaxis=dict(showticklabels=False, showgrid=False),
                      scene_yaxis=dict(showticklabels=False, showgrid=False),
                      scene_zaxis=dict(showticklabels=False, showgrid=False))

    # Show the plot
    fig.show()

# Call the function to create and display the 3D skull
plot_3d_skull()
