import tkinter
import tkinter.messagebox
import random


class Application(tkinter.Frame):
    def __init__(self, master=None):
        super().__init__(master)
        self.grid(sticky="NEWS")

        top = self.winfo_toplevel()
        top.rowconfigure(0, weight=1)
        top.columnconfigure(0, weight=1)

        self.columnconfigure(0, weight=1)
        self.columnconfigure(1, weight=1)
        self.columnconfigure(2, weight=1)
        self.columnconfigure(3, weight=1)

        self.rowconfigure(1, weight=1)
        self.rowconfigure(2, weight=1)
        self.rowconfigure(3, weight=1)
        self.rowconfigure(4, weight=1)

        self.check_map()
        self.spot = {"row": 4, "column": 3}
        self.createWidgets()

    def createWidgets(self):
        self.newButton = tkinter.Button(self, text="New", command=self.generate)
        self.quitButton = tkinter.Button(self, text="Exit", command=self.quit)
        self.newButton.grid(row=0, column=0, columnspan=2)
        self.quitButton.grid(row=0, column=2, columnspan=2)
        self.create_numbers()

    def create_numbers(self):
        self.bts = [tkinter.Button(self, text=str(p + 1), command=self.make_move(i)) for i, p in enumerate(cli_map)]
        for number, button in enumerate(self.bts):
            button.grid(row=number // 4 + 1, column=number % 4, sticky="NEWS")

    def generate(self):
        random.shuffle(cli_map)
        self.check_map()
        self.spot = {"row": 4, "column": 3}
        for button in self.bts:
            button.destroy()
        self.createWidgets()

    def check_map(self):
        count = 0
        for i in range(0, len(cli_map)):
            for j in range(i, len(cli_map)):
                if cli_map[i] > cli_map[j]:
                    count += 1
        if count % 2 == 1:
            cli_map[0], cli_map[1] = cli_map[1], cli_map[0]

    def make_move(self, number):
        def move():
            grid_info = self.bts[number].grid_info()
            column = grid_info['column']
            row = grid_info['row']
            if row == self.spot['row'] and (column == self.spot['column'] - 1 or column == self.spot['column'] + 1):
                self.bts[number].grid(row=self.spot['row'], column=self.spot['column'])
                self.spot['column'] = column
                if self.fix_win():
                    tkinter.messagebox.showinfo(message="You win!")
                    self.generate()
            elif column == self.spot['column'] and (row == self.spot['row'] - 1 or row == self.spot['row'] + 1):
                self.bts[number].grid(row=self.spot['row'], column=self.spot['column'])
                self.spot['row'] = row
                if self.fix_win():
                    tkinter.messagebox.showinfo(message="You win!")
                    self.generate()

        return move

    def fix_win(self):
        for number, button in enumerate(self.bts):
            info = button.grid_info()
            col = info['column']
            row = info['row']
            if col != cli_map[number] % 4 or row != cli_map[number] // 4 + 1:
                return False
        return True


cli_map = [i for i in range(15)]
random.shuffle(cli_map)

app = Application()
app.master.title("15")
app.mainloop()
