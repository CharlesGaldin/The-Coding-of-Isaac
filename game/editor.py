import tkinter as tk

class EditorSetUp:
	def __init__(self):
		self.master = tk.Tk()
		self.master.title("The Coding of Isaac")
		
		self.editor = tk.Frame(self.master)
		self.editor.pack(side = tk.RIGHT)

		self.label = tk.Label(self.editor, text="Your IA:")
		self.label.pack()

		self.text = tk.Text(self.editor)
		self.text.insert(tk.INSERT, """try editing !
Available functions: move('up'), move ('down'), move('left'), move('right) and  getPos().""")
		self.text.pack()
		
		self.close_button = tk.Button(self.editor, text="Submit", command=self.submit)
		self.close_button.pack()
		
		self.exit_requested = False
		def request_exit():
			self.exit_requested = True
		
		self.close_button = tk.Button(self.editor, text="Close", command=request_exit)
		self.close_button.pack()
		
		self.master.protocol("WM_DELETE_WINDOW", request_exit)

		self.userCode = ""

		self.isSubmitted = False

	def submit(self):
		self.userCode = self.text.get("1.0", tk.END)
		self.isSubmitted = True
		print("Submitted !")
	
	def update(self):
		self.master.update()
	
	def close(self):
		self.master.destroy()