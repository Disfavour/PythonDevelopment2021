import tkinter as tk


SYMBOL_SIZE = 8


class Application(tk.Frame):
    def __init__(self, master=None, title="InputLabel", **kwargs):
        super().__init__(master, **kwargs)
        self.master.title(title)
        self.master.columnconfigure(0, weight=1)
        self.master.rowconfigure(0, weight=1)
        self.grid(sticky="news")
        self.create_widgets()
        for column in range(self.grid_size()[0]):
            self.columnconfigure(column, weight=1)
        for row in range(self.grid_size()[1]):
            self.rowconfigure(row, weight=1)

    def create_widgets(self):
        self.labelText = InputLabel(self)
        self.labelText.grid(sticky="we")

        self.buttonQuit = tk.Button(self, text="Quit", command=self.master.quit)
        self.buttonQuit.grid(sticky="e")


class InputLabel(tk.Label):
    def __init__(self, master=None):
        self.text = tk.StringVar()
        super().__init__(master, textvariable=self.text, takefocus=1, highlightthickness=2, cursor="xterm",
                         font="TkFixedFont", relief=tk.SUNKEN, anchor="w", state=tk.NORMAL)

        self.palochka = tk.Frame(self, background="black", height=16, width=1)
        self.pos = 0
        self.palochka.place(x=self.pos, y=1)

        self.bind("<Any-KeyPress>", self.key_input)
        self.bind("<Button-1>", self.lkm)

    def key_input(self, event):
        if event.keysym == "KP_Left" or event.keysym == "Left":
            new_pos = self.pos - SYMBOL_SIZE
            self.change_pos(new_pos)
        elif event.keysym == "KP_Right" or event.keysym == "Right":
            new_pos = self.pos + SYMBOL_SIZE
            self.change_pos(new_pos)
        elif event.keysym == "BackSpace" and self.pos >= SYMBOL_SIZE:
            index = self.pos // SYMBOL_SIZE
            tmp_text = self.text.get()
            self.text.set(tmp_text[:index - 1] + tmp_text[index:])

            new_pos = self.pos - SYMBOL_SIZE
            self.change_pos(new_pos)
        else:
            symbol = event.char
            if symbol.isprintable():
                index = self.pos // SYMBOL_SIZE
                tmp_text = self.text.get()
                self.text.set(tmp_text[:index] + symbol + tmp_text[index:])
                new_pos = self.pos + SYMBOL_SIZE
                self.change_pos(new_pos)

    def lkm(self, event):
        self.focus()
        newpos = event.x // SYMBOL_SIZE * SYMBOL_SIZE
        self.change_pos(newpos)

    def change_pos(self, newpos):
        maxlen_in_symbols = len(self.text.get())
        if newpos > maxlen_in_symbols * SYMBOL_SIZE:
            newpos = maxlen_in_symbols * SYMBOL_SIZE
        if newpos >= 0:
            self.pos = newpos
            self.palochka.place(x=self.pos, y=1)


app = Application()
app.mainloop()
