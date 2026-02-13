import tkinter as tk
import random

class tttGui:
    def __init__(self, root):
        self.root = root
        self.root.title("˙TIC-TAC-TOE˙")
        self.root.geometry("600x750")
        self.root.configure(bg="#ffffff")
        self.root.resizable(False, False)
        
        self.root.update_idletasks()
        width = self.root.winfo_width()
        height = self.root.winfo_height()
        x = (self.root.winfo_screenwidth() // 2) - (width // 2)
        y = (self.root.winfo_screenheight() // 2) - (height // 2)
        self.root.geometry(f'{width}x{height}+{x}+{y}')

        # ____________________"PLAYERS"____________________

        self.playerX = 'X'
        self.playerO = 'O'
        self.currentPlayer = self.playerX
        self.game_mode = None
        self.computer_thinking = False

        self.board = [[0, 0, 0] for _ in range(3)]

        # ____________________"COLORS :3 (Sunset inspired)"____________________

        self.color_dviolet = "#544883" 
        self.color_dpurple = "#9273a7"
        self.color_purppink = "#bd86a6"
        self.color_pink = "#eb7c9c"
        self.color_lpink = "#fff6f0"
        self.color_sunset = "#f59193"
        self.color_orange = "#f9ae91"
        self.color_lyellow = "#f8e1ae"
        self.color_white = "#ffffff"

        self.buttons = []
        self.main_container = None

        self.create_mode_screen()

        # ____________________"GRADIENT BG :3"____________________

    def draw_gradient_and_stars(self, canvas):
        gradients = [self.color_dviolet, self.color_dpurple, self.color_purppink, 
                     self.color_pink, self.color_sunset, self.color_orange, self.color_lyellow]
        
        for i in range(750):
            seg = i / (750 / (len(gradients)-1))
            idx = int(seg)
            f = seg - idx
            c1 = self.root.winfo_rgb(gradients[idx])
            c2 = self.root.winfo_rgb(gradients[min(idx+1, len(gradients)-1)])
            r = int((c1[0] + (c2[0]-c1[0])*f)/256)
            g = int((c1[1] + (c2[1]-c1[1])*f)/256)
            b = int((c1[2] + (c2[2]-c1[2])*f)/256)
            canvas.create_line(0, i, 600, i, fill=f'#{r:02x}{g:02x}{b:02x}')

        # ____________________"★ STARS ★"____________________

        star_chars = ["✧", "⋆", "✮", "★", "⊹", "⋆｡°✩"]
        placed_stars = []
        min_distance = 50
        max_attempts = 200

        while len(placed_stars) < 80 and max_attempts > 0:
            x = random.randint(25, 575)
            y = random.randint(25, 725)
            
            is_clumped = False
            for (sx, sy) in placed_stars:
                dist = ((x - sx)**2 + (y - sy)**2)**0.5
                if dist < min_distance:
                    is_clumped = True
                    break
            
            if not is_clumped:
                size = random.randint(10, 20)
                color = self.color_white
                canvas.create_text(x, y, text=random.choice(star_chars), 
                                   fill=color, font=("Arial", size))
                placed_stars.append((x, y))
            
            max_attempts -= 1

        # ____________________"GOOEY MAIN (GUI)"____________________

    def create_mode_screen(self):
        if self.main_container:
            self.main_container.destroy()
            
        self.main_container = tk.Canvas(self.root, width=600, height=750, highlightthickness= 5)
        self.main_container.pack(fill="both", expand=True)
        self.draw_gradient_and_stars(self.main_container)
        
        content_frame = tk.Frame(self.main_container, bg=self.color_lpink, 
                                 highlightbackground=self.color_dviolet, highlightthickness = 2)
        self.main_container.create_window(300, 375, window=content_frame, width=450, height=550)

        tk.Label(content_frame, text=' <(˶ˆ꒳ˆ˵)> ', font=("Courier New", 15, "bold"),
                 bg=self.color_lpink, fg = self.color_sunset).pack(pady=(50,0))

        tk.Label(content_frame, text='₊⊹ welcome to a simple game of- ⊹₊', font=("Impact", 20),
                 bg=self.color_lpink, fg = self.color_dpurple).pack(pady=(0,0))
        
        tk.Label(content_frame, text='۶ৎ𓂃"TIC-TAC-TOE!"𓂃۶ৎ', font=("Impact", 30, "bold"), 
                 bg=self.color_lpink, fg=self.color_dviolet,).pack(pady=2)

        cat_art = ("╱|、 \n"
                   "(˚ˎ 。7  \n"
                "|、 ˜ 〵 \n"
                   " じしˍ,)ノ")
        signature = "made by yours truly, lori <3!"
        
        tk.Label(content_frame, 
                 text=cat_art,
                 font=("Courier New", 15, "bold"),
                 bg = self.color_lpink, 
                 fg = self.color_sunset).pack(pady=(15, 0))
        
        tk.Label(content_frame, 
                 text = signature, 
                 font = ("Comic Sans MS", 10, "italic", "bold"), 
                 bg = self.color_lpink, 
                 fg = self.color_dpurple).pack(pady=(15, 15))

        for text, mode in [("'Player vs. Player'", 1), ("'Player vs. Computer'", 2)]:
            tk.Button(content_frame, text=text, font=("Comic Sans MS", 12, "bold"),
                      bg=self.color_sunset, fg=self.color_lpink, width= 30, height=1, relief = "raised",
                      activebackground=self.color_purppink, activeforeground="white",
                      cursor="hand2", command=lambda m=mode: self.start_game(m)).pack(pady=15)

        # ____________________"GAME WITH GOOEY (GUI)"____________________

    def start_game(self, mode):
        self.game_mode = mode
        self.currentPlayer = self.playerX
        self.board = [[0, 0, 0] for _ in range(3)]
        self.computer_thinking = False
        self.main_container.destroy()
        self.create_ui()

    def create_ui(self):
        self.main_container = tk.Canvas(self.root, width=600, height=750, highlightthickness=5)
        self.main_container.pack(fill="both", expand=True)
        self.draw_gradient_and_stars(self.main_container)

        self.buttons = []
        game_frame = tk.Frame(self.main_container, bg=self.color_lpink, padx=20, pady=20,
                              highlightbackground=self.color_dviolet, highlightthickness=2)
        self.main_container.create_window(300, 375, window=game_frame)

        self.turn_label = tk.Label(game_frame, text=f"≽^-⩊-^≼ Player '{self.currentPlayer}'s Turn",
                                   font=("Comic Sans MS", 18, "bold"), bg=self.color_lpink, fg=self.color_dpurple)
        self.turn_label.grid(row=0, column=0, columnspan=3, pady=10)

        board_frame = tk.Frame(game_frame, bg=self.color_sunset)
        board_frame.grid(row=1, column=0, columnspan=3)

        for row in range(3):
            row_buttons = []
            for col in range(3):
                btn = tk.Button(board_frame, text="", font=("Comic Sans MS", 28, "bold"), width=4, height=1,
                                bg=self.color_lyellow, activebackground=self.color_lpink,
                                command=lambda r=row, c=col: self.make_move(r, c))
                btn.grid(row=row, column=col, padx=3, pady=3)
                row_buttons.append(btn)
            self.buttons.append(row_buttons)

        self.play_again_btn = tk.Button(game_frame, text="PLAY AGAIN! :3", font=("Comic Sans MS", 12, "bold"),
                                        bg=self.color_dviolet, fg="white", activebackground=self.color_dpurple,
                                        command=self.reset_to_menu)
        self.play_again_btn.grid(row=2, column=0, columnspan=3, pady=15)
        self.play_again_btn.grid_remove()

    def make_move(self, row, col):
        if self.board[row][col] != 0 or self.computer_thinking: return
        self.board[row][col] = self.currentPlayer
        self.update_button_ui(row, col)
        if self.check_winner(): self.end_game(f"Player {self.currentPlayer} WINS! ദ്ദി´ ˘ `)✧")
        elif self.check_draw(): self.end_game("It's a draw! >:[")
        else:
            self.switch_player()
            if self.game_mode == 2 and self.currentPlayer == self.playerO:
                self.computer_thinking = True
                self.turn_label.config(text="waiting your turn...", fg=self.color_dviolet)
                self.root.after(800, self.computer_move)

    def update_button_ui(self, row, col):
        color = self.color_dviolet if self.currentPlayer == 'X' else self.color_dpurple
        self.buttons[row][col].config(text=self.currentPlayer, fg=color, state="disabled",
                                      disabledforeground=color, bg=self.color_white)

    def computer_move(self):
        best_score, best_move = -float('inf'), None
        for r in range(3):
            for c in range(3):
                if self.board[r][c] == 0:
                    self.board[r][c] = self.playerO
                    score = self.minimax(self.board, 0, False)
                    self.board[r][c] = 0
                    if score > best_score: best_score, best_move = score, (r, c)
        if best_move:
            r, c = best_move
            self.board[r][c] = self.playerO
            self.update_button_ui(r, c)
            if self.check_winner(): self.end_game("Computer Wins! :]")
            elif self.check_draw(): self.end_game("It's a draw! >:[")
            else: self.computer_thinking = False; self.switch_player()

    def minimax(self, board, depth, is_max):
        if self.check_winner_static(board, self.playerO): return 10 - depth
        if self.check_winner_static(board, self.playerX): return depth - 10
        if all(cell != 0 for row in board for cell in row): return 0
        
        if is_max:
            best = -float('inf')
            for r in range(3):
                for c in range(3):
                    if board[r][c] == 0:
                        board[r][c] = self.playerO
                        best = max(best, self.minimax(board, depth + 1, False))
                        board[r][c] = 0
            return best
        else:
            best = float('inf')
            for r in range(3):
                for c in range(3):
                    if board[r][c] == 0:
                        board[r][c] = self.playerX
                        best = min(best, self.minimax(board, depth + 1, True))
                        board[r][c] = 0
            return best

    def check_winner_static(self, b, p):
        for i in range(3):
            if (b[i][0]==b[i][1]==b[i][2]==p) or (b[0][i]==b[1][i]==b[2][i]==p): return True
        return (b[0][0]==b[1][1]==b[2][2]==p) or (b[0][2]==b[1][1]==b[2][0]==p)

    def switch_player(self):
        self.currentPlayer = self.playerO if self.currentPlayer == self.playerX else self.playerX
        self.turn_label.config(text=f"≽^-⩊-^≼ Player '{self.currentPlayer}'s Turn", fg= self.color_dpurple if self.currentPlayer == 'O' else self.color_dviolet)

    def check_winner(self): return self.check_winner_static(self.board, self.currentPlayer)
    def check_draw(self): return all(cell != 0 for row in self.board for cell in row)
    def end_game(self, msg):
        self.turn_label.config(text=msg, fg=self.color_dviolet); self.play_again_btn.grid(); self.computer_thinking = False
    def reset_to_menu(self): self.main_container.destroy(); self.create_mode_screen()

if __name__ == "__main__":
    root = tk.Tk()
    game = tttGui(root)
    root.mainloop()