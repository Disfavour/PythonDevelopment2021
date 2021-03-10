import tkinter
import tkinter.messagebox
import random


class Application(tkinter.Frame):
    def __init__(self, master=None):
        super().__init__(master)
        self.grid(sticky="news")

        top = self.winfo_toplevel()
        top.rowconfigure(0, weight=1)
        top.columnconfigure(0, weight=1)

        for i in range(4):
            self.columnconfigure(i, weight=1)
            self.rowconfigure(i + 1, weight=1)

        self.createWidgets()

    def createWidgets(self):
        self.newButton = tkinter.Button(self, text="New", command=self.new_fun)
        self.quitButton = tkinter.Button(self, text="Exit", command=self.quit)
        self.newButton.grid(row=0, column=0, columnspan=2)
        self.quitButton.grid(row=0, column=2, columnspan=2)

        self.logic_list = [i for i in range(15)]
        self.win_list = [i for i in range(16)]

        self.create_numbers()

    def new_fun(self):
        self.delete_buttons()
        self.create_numbers()

    def create_numbers(self):
        self.generate()
        self.logic_list_useful = [i for i in self.logic_list]+[15]

        self.buttons = [tkinter.Button(self, text=str(i + 1), command=self.play(i)) for i in range(15)]
        for i, number in enumerate(self.logic_list):
            self.buttons[number].grid(row=1 + i // 4, column=i % 4, sticky="news")

        self.empty_row = 4
        self.empty_col = 3

    def generate(self):
        random.shuffle(self.logic_list)
        self.check_generation()

    def check_generation(self):
        count = 0
        for i in range(len(self.logic_list)):
            for j in range(i, len(self.logic_list)):
                if self.logic_list[i] > self.logic_list[j]:
                    count += 1
        if count % 2 == 1:
            self.logic_list[0], self.logic_list[1] = self.logic_list[1], self.logic_list[0]

    def play(self, id):
        def real_func():
            current_button = self.buttons[id]
            current_row, current_column = current_button.grid_info()["row"], current_button.grid_info()["column"]

            if abs(current_row - self.empty_row) == 1 and current_column == self.empty_col:
                current_button.grid(row=self.empty_row)

                self.logic_list_useful[(self.empty_row - 1) * 4 + self.empty_col] = self.logic_list_useful[(current_row - 1) * 4 + current_column]
                self.logic_list_useful[(current_row - 1) * 4 + current_column] = 15

                self.empty_row = current_row

            elif abs(current_column - self.empty_col) == 1 and current_row == self.empty_row:
                current_button.grid(column=self.empty_col)

                self.logic_list_useful[(self.empty_row - 1) * 4 + self.empty_col] = self.logic_list_useful[(current_row - 1) * 4 + current_column]
                self.logic_list_useful[(current_row - 1) * 4 + current_column] = 15

                self.empty_col = current_column

            self.check_win()
        return real_func

    def check_win(self):
        if self.logic_list_useful == self.win_list:
            tkinter.messagebox.showinfo(message="You win!")
            self.delete_buttons()
            self.create_numbers()

    def delete_buttons(self):
        for button in self.buttons:
            button.destroy()


app = Application()
app.master.title("15")
app.mainloop()
