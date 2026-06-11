# 🐍 Snake Game  
A classic Snake game recreated in Python using the **turtle** module, with separate classes for organization: **Snake**, **Food**, and **Scoreboard**.  
The goal is simple: eat food, grow, and avoid hitting the walls or your own tail.

---

## 🎯 Purpose  
Create a modular, object‑oriented version of the Snake game, featuring smooth animations, collision detection, and a scoring system.

---

## 🧩 Project Structure  
- **Snake** — controls the snake’s movement, direction, and growth  
- **Food** — generates food in random positions  
- **Scoreboard** — displays and updates the score  
- **main.py** — contains the main game loop and collision logic  

---

## 🚀 Features  
- Smooth snake movement using `screen.tracer(0)`  
- Randomly generated food  
- Dynamic score updates  
- Snake growth after eating  
- Wall collision detection  
- Tail collision detection  
- Game over message  
- Simple high‑score storage using a `.txt` file  

---

## 🎮 Controls  
- **Up Arrow** → move up  
- **Down Arrow** → move down  
- **Left Arrow** → move left  
- **Right Arrow** → move right  

---

## 🧠 Concepts Practiced  
- Object‑oriented programming (OOP)  
- Class inheritance (`Food` and `Scoreboard` inherit from `Turtle`)  
- Animation with `screen.tracer()`  
- Collision detection  
- Lists and coordinate manipulation  
- Game loops  
- Code modularization  
- File reading and writing (I/O)  
