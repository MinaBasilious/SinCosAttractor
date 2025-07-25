
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

1. **Clone the repo**

   ```bash
   git clone https://github.com/<your-username>/SinCosAttractor.git
   cd SinCosAttractor
   ```

2. **Install dependencies**

   ```bash
   pip install -r requirements.txt
   ```

3. **Configure Streamlit** (optional but recommended for cloud)
   Create `./.streamlit/config.toml` with:

   ```toml
   [server]
   headless = true
   enableCORS = false
   port = $PORT
   address = "0.0.0.0"
   ```

4. **Run locally**

   ```bash
   streamlit run app.py
   ```

---

## ☁️ Deployment

* **Streamlit Cloud**

  1. Push to GitHub.
  2. Connect your repo at [https://streamlit.io/cloud](https://streamlit.io/cloud).
  3. Set main file to `app.py` and deploy.

* **Heroku**

  1. Add a `Procfile`:

     ```Procfile
     web: streamlit run app.py --server.port $PORT --server.address 0.0.0.0
     ```
  2. `pip freeze > requirements.txt`
  3. `git push heroku main`

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

```

