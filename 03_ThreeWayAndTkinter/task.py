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

        self.createWidgets()

    def createWidgets(self):
        self.newButton = tkinter.Button(self, text="New", command=self.generate)
        self.quitButton = tkinter.Button(self, text="Exit", command=self.quit)
        self.newButton.grid(row=0, column=0, columnspan=2)
        self.quitButton.grid(row=0, column=2, columnspan=2)

        self.bts = [tkinter.Button(self, text=str(p + 1), command=self.make_move(i)) for i, p in enumerate(cli_map)]
        for number, button in enumerate(self.bts):
            button.grid(row=number // 4 + 1, column=number % 4, sticky="NEWS")

    def generate(self):
        pass

    def make_move(self, g):
        pass

    def fix_win(self):
        pass


cli_map = [i for i in range(15)]
random.shuffle(cli_map)

app = Application()
app.master.title("15")
app.mainloop()
