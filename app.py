import streamlit as st
import numpy as np
import plotly.graph_objects as go
import plotly.express as px
from plotly.subplots import make_subplots
import math

# Set page configuration
st.set_page_config(
    page_title="Simone Attractor Visualizer",
    page_icon="🌀",
    layout="wide"
)

# Title and description
st.title("🌀 Simone Attractor Visualizer")
st.markdown("""
This application visualizes the **Simone attractor**, a dynamical system inspired by Simone Conradi.
The system is defined by the following equations:
""")

# Display the mathematical equations
st.latex(r"""
\begin{cases}
x_{n+1} = \sin\bigl(x_n^2 - y_n^2 + a\bigr)\\
y_{n+1} = \cos\bigl(2\,x_n y_n + b\bigr)
\end{cases}
""")

# Create sidebar for controls
st.sidebar.header("System Parameters")

# Parameter controls
a = st.sidebar.slider(
    "Parameter a", 
    min_value=-5.0, 
    max_value=5.0, 
    value=0.0, 
    step=0.1,
    help="Adjusts the first equation: sin(x²-y²+a)"
)

b = st.sidebar.slider(
    "Parameter b", 
    min_value=-5.0, 
    max_value=5.0, 
    value=0.0, 
    step=0.1,
    help="Adjusts the second equation: cos(2xy+b)"
)

st.sidebar.header("Initial Curve Settings")

# Curve type selection
curve_type = st.sidebar.selectbox(
    "Initial curve type",
    ["Circle", "Horizontal Line", "Vertical Line", "Diagonal Line", "Ellipse"],
    help="Choose the type of initial curve to iterate"
)

# Initialize default values for all curve parameters
center_x = center_y = radius = 0.0
line_y = line_x = line_start = line_end = 0.0
line_start_x = line_start_y = line_end_x = line_end_y = 0.0
radius_x = radius_y = 0.0

# Curve parameters
if curve_type == "Circle":
    center_x = st.sidebar.number_input("Circle center x", value=0.0, step=0.1)
    center_y = st.sidebar.number_input("Circle center y", value=0.0, step=0.1)
    radius = st.sidebar.number_input("Circle radius", value=0.5, min_value=0.1, step=0.1)
elif curve_type == "Horizontal Line":
    line_y = st.sidebar.number_input("Line y-coordinate", value=0.0, step=0.1)
    line_start = st.sidebar.number_input("Line start x", value=-1.0, step=0.1)
    line_end = st.sidebar.number_input("Line end x", value=1.0, step=0.1)
elif curve_type == "Vertical Line":
    line_x = st.sidebar.number_input("Line x-coordinate", value=0.0, step=0.1)
    line_start = st.sidebar.number_input("Line start y", value=-1.0, step=0.1)
    line_end = st.sidebar.number_input("Line end y", value=1.0, step=0.1)
elif curve_type == "Diagonal Line":
    line_start_x = st.sidebar.number_input("Start x", value=-1.0, step=0.1)
    line_start_y = st.sidebar.number_input("Start y", value=-1.0, step=0.1)
    line_end_x = st.sidebar.number_input("End x", value=1.0, step=0.1)
    line_end_y = st.sidebar.number_input("End y", value=1.0, step=0.1)
elif curve_type == "Ellipse":
    center_x = st.sidebar.number_input("Ellipse center x", value=0.0, step=0.1)
    center_y = st.sidebar.number_input("Ellipse center y", value=0.0, step=0.1)
    radius_x = st.sidebar.number_input("Ellipse radius x", value=0.8, min_value=0.1, step=0.1)
    radius_y = st.sidebar.number_input("Ellipse radius y", value=0.4, min_value=0.1, step=0.1)

# Number of points on the curve
n_points = st.sidebar.slider(
    "Points on curve", 
    min_value=20, 
    max_value=200, 
    value=50, 
    step=10,
    help="Number of points to sample along the initial curve"
)

# Number of iterations
n_iterations = st.sidebar.slider(
    "Number of iterations", 
    min_value=1, 
    max_value=20, 
    value=5, 
    step=1,
    help="How many iterations to compute and display"
)

# Reset button
if st.sidebar.button("Reset to Default Values"):
    st.rerun()

def generate_initial_curve(curve_type, n_points, **kwargs):
    """
    Generate points along the initial curve.
    
    Parameters:
    curve_type: Type of curve to generate
    n_points: Number of points on the curve
    **kwargs: Additional parameters specific to each curve type
    
    Returns:
    x_curve, y_curve: Arrays of x and y coordinates of the initial curve
    """
    if curve_type == "Circle":
        center_x = kwargs.get('center_x', 0.0)
        center_y = kwargs.get('center_y', 0.0)
        radius = kwargs.get('radius', 0.5)
        t = np.linspace(0, 2*np.pi, n_points)
        x_curve = center_x + radius * np.cos(t)
        y_curve = center_y + radius * np.sin(t)
        
    elif curve_type == "Horizontal Line":
        line_y = kwargs.get('line_y', 0.0)
        line_start = kwargs.get('line_start', -1.0)
        line_end = kwargs.get('line_end', 1.0)
        x_curve = np.linspace(line_start, line_end, n_points)
        y_curve = np.full(n_points, line_y)
        
    elif curve_type == "Vertical Line":
        line_x = kwargs.get('line_x', 0.0)
        line_start = kwargs.get('line_start', -1.0)
        line_end = kwargs.get('line_end', 1.0)
        x_curve = np.full(n_points, line_x)
        y_curve = np.linspace(line_start, line_end, n_points)
        
    elif curve_type == "Diagonal Line":
        line_start_x = kwargs.get('line_start_x', -1.0)
        line_start_y = kwargs.get('line_start_y', -1.0)
        line_end_x = kwargs.get('line_end_x', 1.0)
        line_end_y = kwargs.get('line_end_y', 1.0)
        x_curve = np.linspace(line_start_x, line_end_x, n_points)
        y_curve = np.linspace(line_start_y, line_end_y, n_points)
        
    elif curve_type == "Ellipse":
        center_x = kwargs.get('center_x', 0.0)
        center_y = kwargs.get('center_y', 0.0)
        radius_x = kwargs.get('radius_x', 0.8)
        radius_y = kwargs.get('radius_y', 0.4)
        t = np.linspace(0, 2*np.pi, n_points)
        x_curve = center_x + radius_x * np.cos(t)
        y_curve = center_y + radius_y * np.sin(t)
    else:
        # Default fallback - create a small circle
        t = np.linspace(0, 2*np.pi, n_points)
        x_curve = 0.5 * np.cos(t)
        y_curve = 0.5 * np.sin(t)
    
    return x_curve, y_curve

def iterate_curve(x_curve, y_curve, a, b, n_iterations):
    """
    Apply the dynamical system to all points on a curve for multiple iterations.
    
    Parameters:
    x_curve, y_curve: Initial curve points
    a, b: System parameters
    n_iterations: Number of iterations to apply
    
    Returns:
    curves: List of (x_values, y_values) for each iteration
    """
    curves = [(x_curve.copy(), y_curve.copy())]  # Store initial curve
    
    current_x = x_curve.copy()
    current_y = y_curve.copy()
    
    for iteration in range(n_iterations):
        # Apply the dynamical system to each point
        new_x = np.sin(current_x**2 - current_y**2 + a)
        new_y = np.cos(2 * current_x * current_y + b)
        
        current_x = new_x
        current_y = new_y
        
        curves.append((current_x.copy(), current_y.copy()))
    
    return curves

# Generate initial curve and compute iterations
try:
    # Gather curve parameters based on type
    curve_params = {}
    if curve_type == "Circle":
        curve_params = {'center_x': center_x, 'center_y': center_y, 'radius': radius}
    elif curve_type == "Horizontal Line":
        curve_params = {'line_y': line_y, 'line_start': line_start, 'line_end': line_end}
    elif curve_type == "Vertical Line":
        curve_params = {'line_x': line_x, 'line_start': line_start, 'line_end': line_end}
    elif curve_type == "Diagonal Line":
        curve_params = {'line_start_x': line_start_x, 'line_start_y': line_start_y, 
                       'line_end_x': line_end_x, 'line_end_y': line_end_y}
    elif curve_type == "Ellipse":
        curve_params = {'center_x': center_x, 'center_y': center_y, 
                       'radius_x': radius_x, 'radius_y': radius_y}
    
    # Generate initial curve
    initial_x, initial_y = generate_initial_curve(curve_type, n_points, **curve_params)
    
    # Compute all curve iterations
    all_curves = iterate_curve(initial_x, initial_y, a, b, n_iterations)
    
    # Create main visualization
    st.subheader("Curve Evolution Through Dynamical System")
    
    # Create the main plot
    fig = go.Figure()
    
    # Color palette for different iterations
    colors = px.colors.qualitative.Set3[:n_iterations+1]
    if len(colors) < n_iterations + 1:
        colors = colors * ((n_iterations + 1) // len(colors) + 1)
    
    # Add each iteration as a separate trace
    for i, (x_curve, y_curve) in enumerate(all_curves):
        fig.add_trace(go.Scatter(
            x=x_curve,
            y=y_curve,
            mode='lines+markers',
            name=f'Iteration {i}',
            line=dict(color=colors[i], width=2 if i == 0 else 1.5),
            marker=dict(size=3 if i == 0 else 2),
            opacity=1.0 if i == 0 else 0.8,
            hovertemplate=f'Iteration {i}<br>x: %{{x:.4f}}<br>y: %{{y:.4f}}<extra></extra>'
        ))
    
    fig.update_layout(
        xaxis_title="x",
        yaxis_title="y",
        showlegend=True,
        height=600,
        hovermode='closest',
        title=f"Evolution of {curve_type} through {n_iterations} iterations"
    )
    
    st.plotly_chart(fig, use_container_width=True)
    
    # Create animated view option
    if st.checkbox("Show Animation", help="Animate the curve evolution step by step"):
        st.subheader("Animated Evolution")
        
        # Create frames for animation
        frames = []
        for i in range(len(all_curves)):
            frame_data = []
            for j in range(i + 1):
                x_curve, y_curve = all_curves[j]
                frame_data.append(go.Scatter(
                    x=x_curve,
                    y=y_curve,
                    mode='lines+markers',
                    name=f'Iteration {j}',
                    line=dict(color=colors[j], width=2 if j == 0 else 1.5),
                    marker=dict(size=3 if j == 0 else 2),
                    opacity=1.0 if j == i else 0.5
                ))
            frames.append(go.Frame(data=frame_data, name=str(i)))
        
        # Create initial figure for animation
        fig_anim = go.Figure(
            data=frames[0].data,
            frames=frames
        )
        
        # Add animation controls
        fig_anim.update_layout(
            xaxis_title="x",
            yaxis_title="y",
            height=500,
            updatemenus=[{
                "buttons": [
                    {
                        "args": [None, {"frame": {"duration": 800, "redraw": True},
                                      "fromcurrent": True, "transition": {"duration": 300}}],
                        "label": "Play",
                        "method": "animate"
                    },
                    {
                        "args": [[None], {"frame": {"duration": 0, "redraw": True},
                                        "mode": "immediate", "transition": {"duration": 0}}],
                        "label": "Pause",
                        "method": "animate"
                    }
                ],
                "direction": "left",
                "pad": {"r": 10, "t": 87},
                "showactive": False,
                "type": "buttons",
                "x": 0.1,
                "xanchor": "right",
                "y": 0,
                "yanchor": "top"
            }],
            sliders=[{
                "active": 0,
                "yanchor": "top",
                "xanchor": "left",
                "currentvalue": {
                    "font": {"size": 20},
                    "prefix": "Iteration:",
                    "visible": True,
                    "xanchor": "right"
                },
                "transition": {"duration": 300, "easing": "cubic-in-out"},
                "pad": {"b": 10, "t": 50},
                "len": 0.9,
                "x": 0.1,
                "y": 0,
                "steps": [
                    {
                        "args": [[f.name], {
                            "frame": {"duration": 300, "redraw": True},
                            "mode": "immediate",
                            "transition": {"duration": 300}
                        }],
                        "label": str(k),
                        "method": "animate"
                    }
                    for k, f in enumerate(frames)
                ]
            }]
        )
        
        st.plotly_chart(fig_anim, use_container_width=True)
    
    # Display system information
    st.subheader("System Information")
    
    col1, col2, col3, col4 = st.columns(4)
    
    with col1:
        st.metric("Parameter a", f"{a:.2f}")
    
    with col2:
        st.metric("Parameter b", f"{b:.2f}")
    
    with col3:
        st.metric("Curve Type", curve_type)
        
    with col4:
        st.metric("Points on Curve", n_points)
    
    # Analysis of curve deformation
    st.subheader("Curve Analysis")
    
    col1, col2, col3 = st.columns(3)
    
    with col1:
        # Calculate total area covered by all iterations
        all_x = np.concatenate([curve[0] for curve in all_curves])
        all_y = np.concatenate([curve[1] for curve in all_curves])
        x_span = np.max(all_x) - np.min(all_x)
        y_span = np.max(all_y) - np.min(all_y)
        st.metric("Total X Span", f"{x_span:.4f}")
    
    with col2:
        st.metric("Total Y Span", f"{y_span:.4f}")
    
    with col3:
        # Calculate how much the curve has "spread" from initial to final
        initial_x_span = np.max(initial_x) - np.min(initial_x)
        initial_y_span = np.max(initial_y) - np.min(initial_y)
        final_x, final_y = all_curves[-1]
        final_x_span = np.max(final_x) - np.min(final_x)
        final_y_span = np.max(final_y) - np.min(final_y)
        
        if initial_x_span > 0 and initial_y_span > 0:
            expansion_factor = ((final_x_span / initial_x_span) + (final_y_span / initial_y_span)) / 2
            st.metric("Expansion Factor", f"{expansion_factor:.2f}x")
        else:
            st.metric("Expansion Factor", "N/A")
    
    # Show current equations with parameter values
    st.subheader("Current System Equations")
    st.latex(f"""
    \\begin{{cases}}
    x_{{n+1}} = \\sin\\bigl(x_n^2 - y_n^2 + {a}\\bigr)\\\\
    y_{{n+1}} = \\cos\\bigl(2\\,x_n y_n + {b}\\bigr)
    \\end{{cases}}
    """)

except Exception as e:
    st.error(f"An error occurred while computing the curve evolution: {str(e)}")
    st.info("Try adjusting the parameters, curve settings, or reducing the number of iterations.")

# Citation and Credits
st.markdown("---")
st.markdown("### References & Credits")

col1, col2 = st.columns(2)

with col1:
    st.markdown("""
    **Simone Attractor**  
    Inspired by Simone Conradi  
    Reference: [Paul Bourke - Simone Orbits](https://paulbourke.net/fractals/simone_orbits/)
    """)

with col2:
    st.markdown("""
    **Application Developer**  
    Created by: **Mina BH Arsanious**
    """)

# Footer with instructions
st.markdown("---")
st.markdown("### Instructions")
st.markdown("""
- Use the sidebar sliders to adjust parameters `a` and `b` in real-time
- Choose different initial curve types (Circle, Lines, Ellipse) to see how they evolve
- Adjust curve parameters to change the shape and position of the initial curve
- Change the number of iterations to see longer evolution sequences
- Enable animation to see step-by-step curve transformation
- Hover over points to see exact coordinate values
- Each color represents a different iteration of the dynamical system
""")
