# main.py
import numpy as np
import matplotlib.pyplot as plt
from sklearn.linear_model import LinearRegression
import os

def generate_dataset(n=800, seed=42):
    np.random.seed(seed)
    g = 9.8
    angles = np.random.uniform(15, 75, n)         # degrees
    velocities = np.random.uniform(10, 50, n)     # m/s
    X = np.column_stack((angles, velocities))
    y_range = (velocities**2 * np.sin(np.radians(2*angles))) / g
    y_height = (velocities**2 * (np.sin(np.radians(angles))**2)) / (2*g)
    return X, y_range, y_height

def train_models(X, y_range, y_height):
    range_model = LinearRegression().fit(X, y_range)
    height_model = LinearRegression().fit(X, y_height)
    return range_model, height_model

def predict(range_model, height_model, angle, velocity):
    features = np.array([[angle, velocity]])
    pred_range = float(range_model.predict(features)[0])
    pred_height = float(height_model.predict(features)[0])
    return pred_range, pred_height

def plot_projectile(angle, velocity, save_path=None):
    g = 9.8
    theta = np.radians(angle)
    t_flight = 2 * velocity * np.sin(theta) / g
    t = np.linspace(0, t_flight, 200)
    x = velocity * np.cos(theta) * t
    y = velocity * np.sin(theta) * t - 0.5 * g * t**2

    plt.figure(figsize=(8,4.5))
    plt.plot(x, y)
    plt.title(f"Projectile Motion (angle={angle}°, velocity={velocity} m/s)")
    plt.xlabel("Distance (m)")
    plt.ylabel("Height (m)")
    plt.grid(True)
    if save_path:
        plt.tight_layout()
        plt.savefig(save_path, dpi=150)
        print(f"Saved plot to {save_path}")
    plt.show()

def main():
    X, y_range, y_height = generate_dataset()
    range_model, height_model = train_models(X, y_range, y_height)

    try:
        angle = float(input("Enter launch angle (degrees): ").strip())
        velocity = float(input("Enter initial velocity (m/s): ").strip())
    except Exception:
        print("Invalid input — using defaults: angle=45°, velocity=30 m/s")
        angle, velocity = 45.0, 30.0

    pred_range, pred_height = predict(range_model, height_model, angle, velocity)

    print(f"\nPredicted Range: {pred_range:.2f} m")
    print(f"Predicted Max Height: {pred_height:.2f} m\n")

    # create assets folder and save example plot (this will also give you an image for README)
    os.makedirs("assets", exist_ok=True)
    save_path = os.path.join("assets", "trajectory_example.png")
    plot_projectile(angle, velocity, save_path)

if __name__ == "__main__":
    main()
