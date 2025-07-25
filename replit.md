# Dynamical System Visualizer

## Overview

This is a Streamlit web application that visualizes an interactive dynamical system using mathematical equations. The application displays a specific 2D dynamical system with user-controllable parameters and creates visualizations using Plotly for interactive plotting.

## User Preferences

Preferred communication style: Simple, everyday language.

## System Architecture

### Frontend Architecture
- **Framework**: Streamlit - A Python web framework for data science applications
- **Visualization**: Plotly (graph_objects, express, subplots) for interactive plotting
- **Layout**: Wide layout configuration for better visualization space
- **UI Components**: Sidebar controls for parameter adjustment, LaTeX rendering for mathematical equations

### Backend Architecture
- **Language**: Python
- **Mathematical Computing**: NumPy for numerical operations
- **Core Logic**: Implements a 2D dynamical system with the equations:
  - x_{n+1} = sin(x_n² - y_n² + a)
  - y_{n+1} = cos(2*x_n*y_n + b)

## Key Components

### 1. User Interface
- **Page Configuration**: Custom title, icon (🌀), and wide layout
- **Parameter Controls**: Interactive sliders in sidebar for parameters 'a' and 'b'
- **Mathematical Display**: LaTeX rendering of the dynamical system equations
- **Visualization Area**: Main content area for plots (implementation appears incomplete)

### 2. Mathematical System
- **Dynamical System**: Two-dimensional discrete-time system
- **Parameters**: Two user-controllable parameters (a, b) with range -5.0 to 5.0
- **Step Size**: 0.1 increment for fine parameter control

### 3. Visualization Components
- **Plotting Library**: Plotly for interactive charts
- **Plot Types**: Prepared for multiple subplot configurations
- **Interactivity**: Real-time parameter adjustment through sliders

## Data Flow

1. **User Input**: Parameters 'a' and 'b' adjusted via sidebar sliders
2. **Mathematical Computation**: Values feed into the dynamical system equations
3. **Visualization**: Results displayed through Plotly interactive plots
4. **Real-time Updates**: Changes in parameters trigger immediate plot updates

Note: The current implementation appears incomplete - while the mathematical framework and UI controls are set up, the actual iteration computation and plotting logic are not yet implemented.

## External Dependencies

### Python Packages
- **streamlit**: Web application framework
- **numpy**: Numerical computing
- **plotly**: Interactive plotting (graph_objects, express, subplots)
- **math**: Standard mathematical functions

### No External Services
- No database connections
- No API integrations
- No authentication systems
- Runs entirely client-side through Streamlit

## Deployment Strategy

### Streamlit Deployment
- **Platform**: Designed for Streamlit sharing or local deployment
- **Requirements**: Python environment with specified dependencies
- **Execution**: Single-file application (`app.py`) with streamlit run command
- **Scalability**: Suitable for individual use or small-scale educational purposes

### Development Setup
- **Entry Point**: `app.py` - single file containing entire application
- **Local Development**: `streamlit run app.py`
- **Dependencies**: Install via pip (streamlit, numpy, plotly)

## Current State and Next Steps

The application framework is established but requires completion of:
1. Implementation of the iterative computation for the dynamical system
2. Generation of trajectory data points
3. Creation of the actual Plotly visualizations
4. Addition of visualization controls (number of iterations, initial conditions, etc.)