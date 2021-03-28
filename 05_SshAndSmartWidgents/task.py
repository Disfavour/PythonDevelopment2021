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
        self.coords = [event.x, event.y] * 2
        if len(self.paint.find_overlapping(*self.coords)) == 0:
            self.cur_id = self.paint.create_oval(*self.coords)
            self.newfig = True
        else:
            self.cur_id = self.paint.find_overlapping(*self.coords)[-1]
            self.newfig = False

    def motion_handler(self, event):
        if event.state == 256:
            if self.newfig:
                self.coords[2], self.coords[3] = event.x, event.y
                self.paint.delete(self.cur_id)
                obj = self.current_object.get()
                width = self.current_width.get()
                fill = self.current_fill.get()
                outline = self.current_outline.get()
                if obj == "oval":
                    self.isoval = True
                    self.cur_id = self.paint.create_oval(*self.coords, width=width, fill=fill, outline=outline)
                else:
                    self.isoval = False
                    self.cur_id = self.paint.create_rectangle(*self.coords, width=width, fill=fill, outline=outline)
            else:
                self.paint.move(self.cur_id, event.x - self.coords[0], event.y - self.coords[1])
                self.coords = [event.x, event.y] * 2

    def button_release_handler(self, event):
        if self.newfig:
            self.ids.append((self.cur_id, self.isoval))
        coords = self.paint.coords(self.cur_id)
        s, w, f, o = self.current_object.get(), self.current_width.get(), self.current_fill.get(), self.current_outline.get()
        for i, obj in enumerate(self.ids):
            if obj[0] == self.cur_id:
                index = i
        self.paint.delete(self.cur_id)
        if s == "oval":
            self.isoval = True
            self.cur_id = self.paint.create_oval(*coords, width=w, fill=f, outline=o)
        else:
            self.isoval = False
            self.cur_id = self.paint.create_rectangle(*coords, width=w, fill=f, outline=o)
        self.ids[index] = (self.cur_id, self.isoval)
        self.write_info((self.cur_id, self.isoval))

    def get_config(self, fid):
        options = self.paint.itemconfigure(fid)
        coords = self.paint.coords(fid)
        width, filling, outline = options['width'][-1], options['fill'][-1], options['outline'][-1]
        return width, filling, outline, coords

    def write_info(self, obj):
        index = self.ids.index(obj)
        fid = obj[0]
        width, filling, outline, coords = self.get_config(fid)
        string = f" {coords[0]} {coords[1]} {coords[2]} {coords[3]} " \
                 f"width='{width}' outline='{outline}' fill='{filling}'"
        self.text_space.delete(str(index + 1) + ".0", str(index + 1) + ".0 lineend")
        if self.ids[index][1]:
            self.text_space.insert(str(index + 1) + ".0", "oval")
        else:
            self.text_space.insert(str(index + 1) + ".0", "rectangle")
        self.text_space.insert(str(index + 1) + ".0 lineend", string)
        if len(self.text_space.get("1.0", tk.END).split("\n")) == index + 2:
            self.text_space.insert(tk.END, "\n")

    def set_tag(self, tag_rem, tag_set, ind):
        self.text_space.tag_remove(tag_rem, str(ind + 1) + ".0", str(ind + 1) + ".0 lineend")
        self.text_space.tag_add(tag_set, str(ind + 1) + ".0", str(ind + 1) + ".0 lineend")

    def draw_shapes(self):
        strings = self.text_space.get("1.0", tk.END).split("\n")
        self.ids.clear()
        for i, s in enumerate(strings):
            words = s.split(" ")
            if words[0] in self.objects:
                try:
                    fid = eval(f"self.paint.create_{words[0]}({','.join(words[1:])})")
                    if words[0] == "oval":
                        obj = (fid, True)
                    else:
                        obj = (fid, False)
                    self.ids.append(obj)
                    self.set_tag("incorrect", "correct", i)
                except:
                    self.set_tag("correct", "incorrect", i)
            else:
                self.set_tag("correct", "incorrect", i)

    def from_text_handler(self):
        for fid in self.paint.find_all():
            self.paint.delete(fid)
        self.draw_shapes()

    def from_image_handler(self):
        self.text_space.delete('1.0', tk.END)
        for obj in self.ids:
            self.write_info(obj)


app = App(title="CCL interpreter v2")
app.mainloop()
