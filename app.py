import streamlit as st
import numpy as np
import plotly.graph_objects as go
import plotly.express as px
from plotly.subplots import make_subplots
import math

# Set page configuration
st.set_page_config(
    page_title="Dynamical System Visualizer",
    page_icon="🌀",
    layout="wide"
)

# Title and description
st.title("🌀 Interactive Dynamical System Visualizer")
st.markdown("""
This application visualizes the following dynamical system:
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

st.sidebar.header("Initial Conditions")

# Initial conditions
x0 = st.sidebar.number_input(
    "Initial x₀", 
    value=0.1, 
    step=0.1,
    help="Starting x coordinate"
)

y0 = st.sidebar.number_input(
    "Initial y₀", 
    value=0.1, 
    step=0.1,
    help="Starting y coordinate"
)

# Number of iterations
n_iterations = st.sidebar.slider(
    "Number of iterations", 
    min_value=10, 
    max_value=1000, 
    value=100, 
    step=10,
    help="How many iterations to compute and display"
)

# Reset button
if st.sidebar.button("Reset to Default Values"):
    st.rerun()

def compute_trajectory(x0, y0, a, b, n_iterations):
    """
    Compute the trajectory of the dynamical system.
    
    Parameters:
    x0, y0: Initial conditions
    a, b: System parameters
    n_iterations: Number of iterations to compute
    
    Returns:
    x_values, y_values: Arrays of x and y coordinates over time
    """
    x_values = np.zeros(n_iterations + 1)
    y_values = np.zeros(n_iterations + 1)
    
    # Set initial conditions
    x_values[0] = x0
    y_values[0] = y0
    
    # Iterate through the system
    for n in range(n_iterations):
        x_n = x_values[n]
        y_n = y_values[n]
        
        # Apply the dynamical system equations
        x_values[n + 1] = math.sin(x_n**2 - y_n**2 + a)
        y_values[n + 1] = math.cos(2 * x_n * y_n + b)
    
    return x_values, y_values

# Compute trajectory
try:
    x_trajectory, y_trajectory = compute_trajectory(x0, y0, a, b, n_iterations)
    
    # Create two columns for plots
    col1, col2 = st.columns(2)
    
    with col1:
        st.subheader("Phase Space Trajectory")
        
        # Create trajectory plot
        fig_trajectory = go.Figure()
        
        # Add trajectory line
        fig_trajectory.add_trace(go.Scatter(
            x=x_trajectory,
            y=y_trajectory,
            mode='lines+markers',
            name='Trajectory',
            line=dict(color='blue', width=2),
            marker=dict(size=3, color='blue'),
            hovertemplate='x: %{x:.4f}<br>y: %{y:.4f}<extra></extra>'
        ))
        
        # Highlight starting point
        fig_trajectory.add_trace(go.Scatter(
            x=[x0],
            y=[y0],
            mode='markers',
            name='Start',
            marker=dict(size=10, color='green', symbol='star'),
            hovertemplate='Start: (%{x:.4f}, %{y:.4f})<extra></extra>'
        ))
        
        # Highlight ending point
        fig_trajectory.add_trace(go.Scatter(
            x=[x_trajectory[-1]],
            y=[y_trajectory[-1]],
            mode='markers',
            name='End',
            marker=dict(size=10, color='red', symbol='x'),
            hovertemplate='End: (%{x:.4f}, %{y:.4f})<extra></extra>'
        ))
        
        fig_trajectory.update_layout(
            xaxis_title="x",
            yaxis_title="y",
            showlegend=True,
            height=400,
            hovermode='closest'
        )
        
        st.plotly_chart(fig_trajectory, use_container_width=True)
    
    with col2:
        st.subheader("Time Series")
        
        # Create time series plot
        iterations = np.arange(n_iterations + 1)
        
        fig_timeseries = make_subplots(
            rows=2, cols=1,
            subplot_titles=('x(n) vs iteration', 'y(n) vs iteration'),
            vertical_spacing=0.12
        )
        
        # Add x time series
        fig_timeseries.add_trace(
            go.Scatter(
                x=iterations,
                y=x_trajectory,
                mode='lines+markers',
                name='x(n)',
                line=dict(color='blue', width=2),
                marker=dict(size=3),
                hovertemplate='Iteration: %{x}<br>x: %{y:.4f}<extra></extra>'
            ),
            row=1, col=1
        )
        
        # Add y time series
        fig_timeseries.add_trace(
            go.Scatter(
                x=iterations,
                y=y_trajectory,
                mode='lines+markers',
                name='y(n)',
                line=dict(color='red', width=2),
                marker=dict(size=3),
                hovertemplate='Iteration: %{x}<br>y: %{y:.4f}<extra></extra>'
            ),
            row=2, col=1
        )
        
        fig_timeseries.update_layout(
            height=400,
            showlegend=True,
            hovermode='x unified'
        )
        
        fig_timeseries.update_xaxes(title_text="Iteration", row=2, col=1)
        fig_timeseries.update_yaxes(title_text="x", row=1, col=1)
        fig_timeseries.update_yaxes(title_text="y", row=2, col=1)
        
        st.plotly_chart(fig_timeseries, use_container_width=True)
    
    # Display current parameter values and statistics
    st.subheader("System Information")
    
    col1, col2, col3, col4 = st.columns(4)
    
    with col1:
        st.metric("Parameter a", f"{a:.2f}")
    
    with col2:
        st.metric("Parameter b", f"{b:.2f}")
    
    with col3:
        st.metric("Final x", f"{x_trajectory[-1]:.4f}")
    
    with col4:
        st.metric("Final y", f"{y_trajectory[-1]:.4f}")
    
    # Additional analysis
    st.subheader("Trajectory Analysis")
    
    col1, col2, col3 = st.columns(3)
    
    with col1:
        # Calculate trajectory length
        distances = np.sqrt(np.diff(x_trajectory)**2 + np.diff(y_trajectory)**2)
        total_length = np.sum(distances)
        st.metric("Total Path Length", f"{total_length:.4f}")
    
    with col2:
        # Calculate bounding box
        x_range = np.max(x_trajectory) - np.min(x_trajectory)
        y_range = np.max(y_trajectory) - np.min(y_trajectory)
        st.metric("X Range", f"{x_range:.4f}")
    
    with col3:
        st.metric("Y Range", f"{y_range:.4f}")
    
    # Show current equations with parameter values
    st.subheader("Current System Equations")
    st.latex(f"""
    \\begin{{cases}}
    x_{{n+1}} = \\sin\\bigl(x_n^2 - y_n^2 + {a}\\bigr)\\\\
    y_{{n+1}} = \\cos\\bigl(2\\,x_n y_n + {b}\\bigr)
    \\end{{cases}}
    """)
    
    # Optionally show raw data
    if st.expander("Show Raw Data"):
        import pandas as pd
        
        df = pd.DataFrame({
            'Iteration': np.arange(n_iterations + 1),
            'x': x_trajectory,
            'y': y_trajectory
        })
        
        st.dataframe(df, use_container_width=True)
        
        # Download button for data
        csv = df.to_csv(index=False)
        st.download_button(
            label="Download trajectory data as CSV",
            data=csv,
            file_name=f"trajectory_a{a}_b{b}.csv",
            mime="text/csv"
        )

except Exception as e:
    st.error(f"An error occurred while computing the trajectory: {str(e)}")
    st.info("Try adjusting the parameters or initial conditions.")

# Footer with instructions
st.markdown("---")
st.markdown("""
**Instructions:**
- Use the sidebar sliders to adjust parameters `a` and `b` in real-time
- Change initial conditions `x₀` and `y₀` to explore different starting points
- Adjust the number of iterations to see longer or shorter trajectories
- The left plot shows the trajectory in phase space (x vs y)
- The right plot shows how x and y evolve over time
- Hover over points to see exact values
""")
