import plotly.graph_objects as go
import numpy as np

def plot_3d_rotating_cube():
    # Create a 3D cube
    vertices = np.array([
        [-1, -1, -1],
        [1, -1, -1],
        [1, 1, -1],
        [-1, 1, -1],
        [-1, -1, 1],
        [1, -1, 1],
        [1, 1, 1],
        [-1, 1, 1]
    ])

    edges = np.array([
        [0, 1], [1, 2], [2, 3], [3, 0],
        [0, 4], [1, 5], [2, 6], [3, 7],
        [4, 5], [5, 6], [6, 7], [7, 4]
    ])

    # Create a figure
    fig = go.Figure()

    # Initial cube plot
    fig.add_trace(go.Scatter3d(
        x=vertices[:, 0], y=vertices[:, 1], z=vertices[:, 2],
        line=dict(color='blue', width=3),
        mode='lines'
    ))

    # Set axis labels and range
    axis_length = 2
    fig.update_layout(scene=dict(
        xaxis_title='X-axis',
        yaxis_title='Y-axis',
        zaxis_title='Z-axis',
        xaxis_range=[-axis_length, axis_length],
        yaxis_range=[-axis_length, axis_length],
        zaxis_range=[-axis_length, axis_length]
    ))

    # Set the aspect ratio to equal
    fig.update_layout(scene_aspectmode='cube')

    # Hide axes ticks and grid lines
    fig.update_layout(scene_xaxis=dict(showticklabels=False, showgrid=False),
                      scene_yaxis=dict(showticklabels=False, showgrid=False),
                      scene_zaxis=dict(showticklabels=False, showgrid=False))

    # Animation frames for rotating the cube
    frames = []
    num_frames = 36
    for i in range(num_frames + 1):
        theta = (i / num_frames) * 2 * np.pi
        rotation_matrix = np.array([[np.cos(theta), -np.sin(theta), 0],
                                    [np.sin(theta), np.cos(theta), 0],
                                    [0, 0, 1]])
        rotated_vertices = np.dot(vertices, rotation_matrix)

        frame = go.Frame(data=[go.Scatter3d(x=rotated_vertices[:, 0], y=rotated_vertices[:, 1], z=rotated_vertices[:, 2])],
                         name=f"frame{i}")
        frames.append(frame)

    # Add animation
    fig.update(frames=frames, updatemenus=[dict(type='buttons', showactive=False, buttons=[dict(label='Play',
                                                                                              method='animate',
                                                                                              args=[None,
                                                                                                    dict(frame=dict(duration=50, redraw=True),
                                                                                                         fromcurrent=True,
                                                                                                         mode='immediate')]
                                                                                              )
                                                                                     )
                                                                                    ]
                                               )
                                          ]
               )

    # Set the default frame to the last frame
    last_frame = go.Frame(data=[go.Scatter3d(x=frames[-1].data[0].x, y=frames[-1].data[0].y, z=frames[-1].data[0].z)],
                          name=frames[-1].name)
    fig.update_layout(updatemenus=[dict(type='buttons', showactive=False, buttons=[dict(label='Play',
                                                                                       method='animate',
                                                                                       args=[None,
                                                                                             dict(frame=dict(duration=50, redraw=True),
                                                                                                  fromcurrent=True,
                                                                                                  to=last_frame.name,
                                                                                                  mode='immediate')]
                                                                                       )
                                                                              ]
                                         )
                                    ]
                      )

    # Set the initial frame
    fig.update_layout(updatemenus=[dict(type='buttons', showactive=False, buttons=[dict(label='Play',
                                                                                       method='animate',
                                                                                       args=[None,
                                                                                             dict(frame=dict(duration=50, redraw=True),
                                                                                                  fromcurrent=True,
                                                                                                  to=frames[0].name,
                                                                                                  mode='immediate')]
                                                                                       )
                                                                              ]
                                         )
                                    ]
                      )

    # Show the plot
    fig.show()

# Call the function to create and display the rotating cube
plot_3d_rotating_cube()
