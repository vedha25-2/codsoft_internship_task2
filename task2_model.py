import os
import os
import math
import random

class TicTacToeGame:
    def __init__(self):
        self.HUMAN = 'X'
        self.AI = 'O'
        self.EMPTY = ' '
        self.board = [self.EMPTY] * 9
        self.WIN_LINES = [
            [0, 1, 2], [3, 4, 5], [6, 7, 8], # Rows
            [0, 3, 6], [1, 4, 7], [2, 5, 8], # Columns
            [0, 4, 8], [2, 4, 6]             # Diagonals
        ]

    def print_board(self):
        os.system('cls' if os.name == 'nt' else 'clear')
        print("\n=== UNBEATABLE MINIMAX AI ARCHITECTURE ===")
        print(f"       {self.board[0]} | {self.board[1]} | {self.board[2]} ")
        print("      -----------")
        print(f"       {self.board[3]} | {self.board[4]} | {self.board[5]} ")
        print("      -----------")
        print(f"       {self.board[6]} | {self.board[7]} | {self.board[8]} ")
        print("==========================================\n")
        print("Map Input -> Positions: 1 to 9")

    def is_winner(self, player):
        return any(all(self.board[cell] == player for cell in line) for line in self.WIN_LINES)

    def is_draw(self):
        return self.EMPTY not in self.board

    def get_available_moves(self):
        return [i for i, cell in enumerate(self.board) if cell == self.EMPTY]


class MinimaxAI:
    def __init__(self, game_engine):
        self.game = game_engine

    def evaluate_state(self):
        if self.game.is_winner(self.game.AI):
            return 10
        if self.game.is_winner(self.game.HUMAN):
            return -10
        return 0

    def compute_minimax(self, depth, is_maximizing):
        score = self.evaluate_state()
        
        # Terminal condition check
        if score == 10 or score == -10:
            return score - depth if score == 10 else score + depth
        if self.game.is_draw():
            return 0

        if is_maximizing:
            best_val = -math.inf
            for move in self.game.get_available_moves():
                self.game.board[move] = self.game.AI
                value = self.compute_minimax(depth + 1, False)
                self.game.board[move] = self.game.EMPTY
                best_val = max(best_val, value)
            return best_val
        else:
            best_val = math.inf
            for move in self.game.get_available_moves():
                self.game.board[move] = self.game.HUMAN
                value = self.compute_minimax(depth + 1, True)
                self.game.board[move] = self.game.EMPTY
                best_val = min(best_val, value)
            return best_val

    def select_optimal_move(self):
        available = self.game.get_available_moves()
        
        # Unique Trick: If it's the very first move of the game and AI goes first, 
        # choose a random corner to make the game variation unique every run.
        if len(available) == 9:
            return random.choice([0, 2, 6, 8])

        best_score = -math.inf
        optimal_move = -1
        
        for move in available:
            self.game.board[move] = self.game.AI
            move_score = self.compute_minimax(0, False)
            self.game.board[move] = self.game.EMPTY
            
            if move_score > best_score:
                best_score = move_score
                optimal_move = move
                
        return optimal_move


def main():
    engine = TicTacToeGame()
    ai_agent = MinimaxAI(engine)
    
    engine.print_board()
    choice = input("Do you want the first move? (y/n): ").strip().lower()
    human_turn = True if choice == 'y' else False

    while True:
        engine.print_board()
        
        if engine.is_winner(engine.AI):
            print("🤖 Status: AI completely locked and won the match.")
            break
        elif engine.is_winner(engine.HUMAN):
            print("🎉 Status: Impossible victory reached!")
            break
        elif engine.is_draw():
            print("🤝 Status: Match drawn! Perfect game play from both sides.")
            break

        if human_turn:
            try:
                move = int(input(f"\nYour turn ({engine.HUMAN}). Pick [1-9]: ")) - 1
                if move not in range(9) or engine.board[move] != engine.EMPTY:
                    print("⚠️ Position filled or out of bounds! Try again.")
                    input("Press Enter to continue...")
                    continue
                engine.board[move] = engine.HUMAN
                human_turn = False
            except ValueError:
                input("⚠️ Type a valid digit. Press Enter...")
        else:
            print("\n🤖 AI thinking via recursive minimax optimization matrix...")
            ai_choice = ai_agent.select_optimal_move()
            if ai_choice != -1:
                engine.board[ai_choice] = engine.AI
            human_turn = True

if __name__ == "__main__":
    main()