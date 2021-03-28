import tkinter as tk


class Application(tk.Frame):
    """Sample tkinter application class"""

    def __init__(self, master=None, title="<application>", **kwargs):
        """Create root window with frame, tune weight and resize"""
        super().__init__(master, **kwargs)
        self.master.title(title)
        self.master.columnconfigure(0, weight=1)
        self.master.rowconfigure(0, weight=1)
        self.grid(sticky="NEWS")
        self.create_widgets()
        for column in range(self.grid_size()[0]):
            self.columnconfigure(column, weight=1)
        for row in range(self.grid_size()[1]):
            self.rowconfigure(row, weight=1)

    def create_widgets(self):
        """Create all the widgets"""


class App(Application):
    def values_init(self):
        self.outline_list = ['black', 'blue', 'red', 'green', 'yellow', 'white', 'cyan', 'magenta']
        self.fill_list = ['green', 'blue', 'red', 'yellow', 'black', 'white', 'cyan', 'magenta']
        self.width_list = ['1.0', '2.0', '3.0', '4.0', '5.0']
        self.ids = []
        self.isoval = True
        self.newfig = False
        self.coords = [0, 0, 0, 0]
        self.cur_id = 0
        self.objects = ["oval", "rectangle"]

    def create_widgets(self):
        super().create_widgets()
        self.values_init()

        self.current_object = tk.StringVar()
        self.current_width = tk.StringVar()
        self.current_fill = tk.StringVar()
        self.current_outline = tk.StringVar()

        self.current_object.set(self.objects[0])
        self.current_width.set(self.width_list[0])
        self.current_fill.set(self.fill_list[0])
        self.current_outline.set(self.outline_list[0])

        self.text_space = tk.Text(self)
        self.paint = tk.Canvas(self)

        self.from_text = tk.Button(self, text="from text", command=self.from_text_handler)
        self.from_image = tk.Button(self, text="from image", command=self.from_image_handler)
        self.Q = tk.Button(self, text="QUIT", command=self.master.quit)

        self.object_label = tk.Label(self, text="object")
        self.width_label = tk.Label(self, text="width")
        self.fill_label = tk.Label(self, text="fill")
        self.outline_label = tk.Label(self, text="outline")

        self.object_menu = tk.OptionMenu(self, self.current_object, *self.objects)
        self.width_menu = tk.OptionMenu(self, self.current_width, *self.width_list)
        self.fill_menu = tk.OptionMenu(self, self.current_fill, *self.fill_list)
        self.outline_menu = tk.OptionMenu(self, self.current_outline, *self.outline_list)

        self.text_space.grid(row=0, column=0, sticky="news")
        self.paint.grid(row=0, column=1, columnspan=4, sticky="news")

        self.object_label.grid(row=2, column=1, sticky="w")
        self.object_menu.grid(row=1, column=1, sticky="w")

        self.width_label.grid(row=2, column=2, sticky="w")
        self.width_menu.grid(row=1, column=2, sticky="w")

        self.outline_label.grid(row=2, column=3, sticky="w")
        self.outline_menu.grid(row=1, column=3, sticky="w")

        self.fill_label.grid(row=2, column=4, sticky="w")
        self.fill_menu.grid(row=1, column=4, sticky="w")

        self.from_text.grid(row=1, column=0)
        self.from_image.grid(row=2, column=0)
        self.Q.grid(row=3, column=0, columnspan=5)

        self.text_space.tag_config("incorrect", background="red")
        self.text_space.tag_config("correct", background="white")

        self.paint.bind("<Button-1>", self.mouse_handler)
        self.paint.bind("<Motion>", self.motion_handler)
        self.paint.bind("<ButtonRelease>", self.button_release_handler)

    def mouse_handler(self, event):
        pass

    def motion_handler(self, event):
        pass

    def button_release_handler(self, event):
        pass

    def draw_shapes(self):
        pass

    def from_text_handler(self):
        pass

    def from_image_handler(self):
        pass


app = App(title="CCL interpreter v2")
app.mainloop()
