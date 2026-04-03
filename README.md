# 2D Physics Simulation: Day 1 - Constant Acceleration & Impulse

A simple 2D physics simulation built with **Python** and **Pygame** to demonstrate the fundamental laws of kinematics and Newton's Second Law of Motion.

## 🚀 The Simulation
![Physics Demo](demo.gif) 

## 🧠 The Physics Behind the Code
This simulation implements **Semi-Implicit Euler Integration**. Instead of just moving pixels, the ball follows mathematical rules:

### 1. Newton's Second Law ($F = ma$)
Gravity acts as a constant force. Since mass is constant in this simulation, we apply a steady downward acceleration ($g$) to the vertical velocity ($v_y$) every frame:
$$v_{y_{new}} = v_{y_{old}} + g$$

### 2. Linear Kinematics
To update the ball's position on the screen, we use the displacement rule where change in position is determined by the current velocity:
$$y_{new} = y_{old} + v_{y_{new}}$$

### 3. The Impulse (The Jump)
When the jump is triggered, we apply an **instantaneous change in momentum**. We overwrite the vertical velocity with a negative upward force ($-u$):
$$v_y = -u$$

## 🛠️ How to Run
1. Install Pygame: `pip install pygame`
2. Run the script: `python main.py`
3. Press **[SPACE]** to jump!

---
*Part of a daily physics-graphics challenge.*
