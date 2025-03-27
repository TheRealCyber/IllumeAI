# IllumeAI - Lights Out Puzzle Solver  

Welcome to **IllumeAI**, an interactive **Lights Out puzzle game** with an AI solver. Your goal is to toggle lights strategically to turn them all off. The game features an **AI solver** powered by **Gaussian elimination mod 2**, allowing you to find optimal solutions effortlessly.  

Built with **Flask (Python) for the backend** and **JavaScript for the frontend**, IllumeAI delivers a smooth and intuitive gaming experience.  

---

## Features  
- **Dynamic 5x5 grid** with randomly generated solvable puzzles  
- Click on a cell to **toggle it and its adjacent lights**  
- **AI solver** to provide optimal solutions instantly  
- **Reset Level** to restore the grid to its starting state  
- **Next Level** to progress to a fresh challenge  
- **Reset Game** to restart from level 1  
- Responsive **Flask-based web interface**  

![image](https://github.com/user-attachments/assets/a7829dc4-5f00-466b-b13e-c8cdc421525b)

---

## Installation  

### Clone the Repository  
```bash
git clone https://github.com/YOUR-USERNAME/IllumeAI.git
cd IllumeAI
```

### Install Dependencies  
```bash
pip install flask numpy
```

### Run the Application  
```bash
python app.py
```
Now, open your browser and go to **http://127.0.0.1:5000/** to start playing.  

---

## How to Play  
1. Click on a **cell** to toggle it and its adjacent cells.  
2. Turn **all cells OFF (black)** to win.  
3. Need help? Click **"Show Solution Using AI"** for an optimal solution.  
4. Click **"Reset Level"** to restore the grid to its original state.  
5. Click **"Next Level"** to generate a fresh challenge.  
6. Click **"Reset Game"** to restart from Level 1.  

---

## Project Structure  
```
IllumeAI/
│── static/             # (Optional) CSS/JS for styling (if needed)
│── templates/
│   ├── index.html      # Frontend UI (grid, buttons, solution display)
│── app.py              # Backend Flask server handling game logic
│── README.md           # Project Documentation
```

---

## How the AI Solver Works  
The AI solver in **IllumeAI** uses **Gaussian elimination mod 2** to find the optimal moves:  
1. **Constructs a toggle matrix** representing the Lights Out rules.  
2. Uses **binary row operations** to simplify the problem mathematically.  
3. **Back-substitutes** to determine the most efficient button presses to solve the puzzle.  

![image](https://github.com/user-attachments/assets/08d9645f-a930-4c0b-878f-34146b5c1e5c)

---

## Future Enhancements  
- Add difficulty modes (**easy, medium, hard**)  
- Implement a **move counter** to track player efficiency  
- Improve UI with **animations and effects**  
- Convert to a **React/Flask hybrid app** for better performance  

---

## Contributing  
Want to contribute?  
- Fork the repository  
- Create a new branch  
- Submit a pull request  

---
