#!/usr/bin/env python3
import random
import os

def clear_screen():

    os.system('cls' if os.name == 'nt' else 'clear')

class Minesweeper:
    def __init__(self, width=10, height=10, mines=10):
        self.width = width
        self.height = height
        self.mines = set(random.sample(range(width * height), mines))
        self.revealed = [[False for _ in range(width)] for _ in range(height)]

    def print_board(self, reveal=False):

        clear_screen()
        print('  ' + ' '.join(str(i) for i in range(self.width)))
        for y in range(self.height):
            print(y, end=' ')
            for x in range(self.width):
                if reveal or self.revealed[y][x]:
                    if (y * self.width + x) in self.mines:
                        print('*', end=' ')
                    else:
                        count = self.count_mines_nearby(x, y)
                        print(count if count > 0 else ' ', end=' ')
                else:
                    print('.', end=' ')
            print()

    def count_mines_nearby(self, x, y):

        count = 0
        for dx in [-1, 0, 1]:
            for dy in [-1, 0, 1]:
                if dx == 0 and dy == 0:  # no contar la propia celda
                    continue
                nx, ny = x + dx, y + dy
                if 0 <= nx < self.width and 0 <= ny < self.height:
                    if (ny * self.width + nx) in self.mines:
                        count += 1
        return count

    def reveal(self, x, y):

        # Validar coordenadas
        if not (0 <= x < self.width and 0 <= y < self.height):
            print("Out of range. Try again.")
            return True  # No detona, solo ignora la jugada

        if (y * self.width + x) in self.mines:
            return False  # Mina encontrada
        if self.revealed[y][x]:
            return True  # Ya revelada

        self.revealed[y][x] = True

        # Propagar si no hay minas alrededor
        if self.count_mines_nearby(x, y) == 0:
            for dx in [-1, 0, 1]:
                for dy in [-1, 0, 1]:
                    if dx == 0 and dy == 0:
                        continue
                    nx, ny = x + dx, y + dy
                    if 0 <= nx < self.width and 0 <= ny < self.height and not self.revealed[ny][nx]:
                        self.reveal(nx, ny)
        return True

    def play(self):

        while True:
            self.print_board()
            try:
                x = int(input("Enter x coordinate: "))
                y = int(input("Enter y coordinate: "))
            except ValueError:
                print("Invalid input. Please enter numbers only.")
                continue
            except KeyboardInterrupt:
                print("\nGame interrupted by user. Exiting...")
                break

            if not (0 <= x < self.width and 0 <= y < self.height):
                print("Out of range. Try again.")
                continue

            if not self.reveal(x, y):
                self.print_board(reveal=True)
                print("💥 Game Over! You hit a mine.")
                break

if __name__ == "__main__":
    game = Minesweeper()
    game.play()
