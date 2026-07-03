# CodSoft AI Internship - Task 2: Tic-Tac-Toe AI

An implementation of an unbeatable Artificial Intelligence agent that plays the classic game of Tic-Tac-Toe against a human player. Built as part of the CodSoft Artificial Intelligence internship curriculum, this project focuses on foundational game theory, decision trees, and adversarial search algorithms.

## Project Objective
As outlined in `1000139373.jpg`, the goal of this task is to implement an AI agent utilizing algorithms like **Minimax** (optionally optimized with **Alpha-Beta Pruning**) to ensure the AI plays optimally, making it completely unbeatable by a human opponent.

##  Core Concepts & Algorithms

### 1. Adversarial Search & Game Theory
Tic-Tac-Toe is a zero-sum, perfect information game. The AI evaluates possible future board states to select the move that maximizes its chances of winning while minimizing the human player's chances.

### 2. The Minimax Algorithm
The core decision-making engine simulates all possible moves in the game tree recursively:
*   **Maximizer (AI):** Tries to get the highest score possible.
*   **Minimizer (Human):** Tries to get the lowest score possible.

The algorithm scores terminal states:
*   `+10` if the AI wins.
*   `-10` if the human wins.
*   `0` for a draw/tie.

> **Note:** *(Optional)* Alpha-Beta Pruning was implemented to cut down the search space, reducing computation time by stopping the evaluation of a move when at least one possibility has been found that proves the move to be worse than a previously examined choice.

##  Features
*   **Unbeatable AI Opponent:** Play against an agent running the Minimax algorithm. The best a human player can achieve is a draw.
*   **Smooth Interactivity:** Easy-to-use command-line interface (CLI) or graphical user interface (GUI).
*   **Real-time Move Evaluation:** Demonstrates basic search algorithms in AI development.

## Tech Stack
*   **Language:** Python 3.x *(or substitute with C++ / Java depending on your choice)*
*   **Libraries:** `Tkinter` / `pygame` (for GUI) or standard library (for CLI)

## Project Structure
```text
├── main.py             # Main entry point for the game
├── tic_tac_toe_ai.py   # AI Agent logic containing the Minimax function
├── game_engine.py      # Board state management and win-condition validations
└── README.md           # Project documentation

# Author

* Name: Vedha
* **Role: Artificial Intelligence Intern
* Organization: CodSoft
* LinkedIn:https:https://www.linkedin.com/in/vedhamithrasri-kadali-72b244378
