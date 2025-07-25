
# Simone Attractor Visualizer

🌀 **Interactive Streamlit app** to explore the Simone attractor—a beautiful 2D discrete dynamical system—by iterating continuous curves and watching how they evolve.

---

## 🚀 Live Demo

[![Open Live App](https://static.streamlit.io/badges/streamlit_badge_black_white.svg)](https://sincosattractor.streamlit.app/)

---

## 📖 Overview

This application visualizes curve evolution under the Simone attractor system:

```math
\begin{aligned}
 x_{n+1} &= \sin(x_n^2 - y_n^2 + a),\\
 y_{n+1} &= \cos(2\,x_n\,y_n + b).
\end{aligned}
````

Users choose an initial curve (circle, line, ellipse, etc.), set parameters \$a\$ and \$b\$, and watch how the entire curve deforms over multiple iterations—with optional animation controls.

---

## ⚙️ Features

* **Multiple Initial Curves**: Circle, horizontal/vertical/diagonal lines, ellipse.
* **Parameter Sliders**: Adjust \$a\$ and \$b\$ in real time (range: -5 to 5).
* **Interactive Plotting**: Powered by Plotly for hover, zoom, and pan.
* **Color‑coded Iterations**: See progression of each point.
* **Animation Mode**: Play/pause and slide through iterations.
* **Analysis Metrics**: Track curve span, expansion factors, and deformation.

---

## 📦 Tech Stack

* **Frontend**: [Streamlit](https://streamlit.io/)
* **Plotting**: [Plotly](https://plotly.com/) (graph\_objects & express)
* **Numerics**: [NumPy](https://numpy.org/)
* **Language**: Python 3.8+

---

## 💻 Installation & Local Run

You can install dependencies using either **poetry** (recommended if you’re using `pyproject.toml`) or **pip** (by exporting a requirements file).

**Option 1: Install via Poetry**

1. Install Poetry (if you don’t have it):

   ```bash
   pip install poetry
   ```
2. Install project dependencies:

   ```bash
   cd SinCosAttractor
   poetry install
   ```
3. Run the app:

   ```bash
   poetry run streamlit run app.py
   ```

**Option 2: Generate and install with pip**

1. Generate a `requirements.txt` from your lock file:

   ```bash
   cd SinCosAttractor
   pip install pip-tools            # if you don’t have pip-tools
   pip-compile --output-file=requirements.txt pyproject.toml
   ```
2. Install dependencies with pip:

   ```bash
   pip install -r requirements.txt
   ```
3. Run the app:

   ```bash
   streamlit run app.py
   ```

---

## ☁️ Deployment

* **Streamlit Cloud**

  1. Push to GitHub.
  2. Connect your repo at [https://streamlit.io/cloud](https://streamlit.io/cloud).
  3. Set main file to `app.py` and deploy.


> **Note:** GitHub Pages only serves static files—you’ll need a Python‑capable host for a live Streamlit app.

---

## 🖋 Credits

* **Simone Attractor**
  Inspired by Simone Conradi.
  Reference: [Paul Bourke – Simone Orbits](https://paulbourke.net/fractals/simone_orbits/)

* **Developer**
  Mina B.H. Arsanious

---

## 📜 License

This project is released under the MIT License. See [LICENSE](LICENSE) for details.


