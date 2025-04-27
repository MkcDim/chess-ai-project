# Chess AI Project

![Work in Progress](https://img.shields.io/badge/status-work%20in%20progress-yellow)

Welcome to the **Chess AI Project**!

This project is a personal chess game developed in Python, featuring:
- A simple and clean graphical interface.
- Playable games against a basic AI.
- An evolving AI that learns exclusively from the user's games.

This project is mainly built to help me improve at chess by training against an AI that grows with my own level (currently around 600–1000 Elo).

---

## 🚀 Features
- Graphical chessboard with basic piece movement.
- Turn-based play: player vs AI.
- Game storage (to allow AI learning).
- AI starts naive and gets stronger based on played games.
- Project structured with virtual environments and Git versioning.

---

## 📦 Technologies
- Python 3.8+
- `python-chess`
- `tkinter` (GUI)
- [Optional future] `pygame`, `torch`, or `tensorflow` for more advanced AI features.

---

## 🛠️ How to run
1. Clone the repository:
   ```bash
   git clone https://github.com/dmikec/chess-ai-project.git
   cd chess-ai-project
    ```
2. Create and activate a virtual environment:
   ```bash
    python -m venv venv
    venv\Scripts\activate  # On Windows
    # or source venv/bin/activate  # On Linux/Mac
    ```
3. Install required packages:
   ```bash
    pip install -r requirements.txt
    ```
4. Launch the game
    ```bash
    python chess_game.py
    ```

## 📈 Project Roadmap
- [x] Setup project structure (venv, Git, basic GUI)
- [ ] Implement random-move AI
- [ ] Store games and build learning datasets
- [ ] Make the AI learn from its past games
- [ ] Add game review and stats interface
- [ ] Improve AI to reinforcement learning (bonus phase)