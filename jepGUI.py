import tkinter as tk

LARGE_FONT = ("Verdana", 12)

class Window(tk.Tk):
	def __init__(self, *args, **kwargs):
		tk.Tk.__init__(self, *args, **kwargs) 
		container = tk.Frame(self) 
		container.pack(side="top", fill="both", expand = True)
 
		container.grid_rowconfigure(0, weight = 1)
		container.grid_columnconfigure(0, weight=1)

		self.frames = {}

		for F in (StartPage, PageOne, PageTwo):

			frame = F(container, self)

			self.frames[F] = frame

			frame.grid(row=0, column = 0, sticky="nsew")

		self.show_frame(StartPage)

	def show_frame(self, cont):

		frame = self.frames[cont]
		frame.tkraise()

class StartPage(tk.Frame):

	def __init__(self, parent, controller):
		tk.Frame.__init__(self, parent)
		label = tk.Label(self, text="Welcome", font=LARGE_FONT)
		label.pack(pady=10, padx=10)

		button = tk.Button(self, text="Start Game", command=lambda : controller.show_frame(PageOne))
		button.pack()
		button2 = tk.Button(self, text="Categories", command=lambda: controller.show_frame(PageTwo))
		button2.pack()


class PageOne(tk.Frame):

	def __init__(self, parent, controller):
		tk.Frame.__init__(self, parent)
		label = tk.Label(self, text="Jepoardy", font=LARGE_FONT)
		label.pack(pady=10, padx=10)

		button = tk.Button(self, text="Categories", command=lambda: controller.show_frame(PageTwo))
		button.pack()

		button2= tk.Button(self, text="Visiting page 2", command=lambda: controller.show_frame(PageTwo))

		button2.pack()

class PageTwo(tk.Frame):

	def __init__(self, parent, controller):
		tk.Frame.__init__(self, parent)
		label = tk.Label(self, text="Page 2", font=LARGE_FONT)
		label.pack(pady=10, padx=10)

		button1 = tk.Button(self, text="Play Again", command=lambda: controller.show_frame(StartPage)) 

		button1.pack()

		button2 = tk.Button(self, text="PageOne", command=lambda: controller.show_frame(PageOne))

		button2.pack()

app = Window()
app.geometry("900x700+450+150")
app.mainloop()

