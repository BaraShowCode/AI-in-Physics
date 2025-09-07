AI in Physics: Projectile Motion Predictor

![Python](https://img.shields.io/badge/Python-3.8+-blue.svg)
![License](https://img.shields.io/badge/License-MIT-green.svg)
![Status](https://img.shields.io/badge/Project-Active-brightgreen.svg)

This project applies **Machine Learning** to classical **Physics** to predict and visualize projectile motion.

## Features
- Generates synthetic dataset (angle, velocity → range & max height).
- Trains Linear Regression models to predict range and max height.
- CLI input for angle and velocity.
- Visualization of trajectory and saved example image (`assets/trajectory_example.png`).

## Installation
```bash
git clone https://github.com/YOURUSERNAME/ai-physics-projectile-motion.git
cd ai-physics-projectile-motion
python -m venv venv
# activate venv:
# Windows: venv\Scripts\activate
# macOS/Linux: source venv/bin/activate
pip install -r requirements.txt
