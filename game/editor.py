import tkinter as tk

userCode = ""

class EditorSetUp:
	def __init__(self, master):
		self.master = master
		master.title("A simple GUI")

		self.label = tk.Label(master, text="This is our first GUI!")
		self.label.pack()

		self.text = tk.Text(master)
		self.text.insert(tk.INSERT, "try editing")
		self.text.pack()
		
		self.close_button = tk.Button(master, text="Submit", command=self.submit)
		self.close_button.pack()

		self.close_button = tk.Button(master, text="Close", command=master.quit)
		self.close_button.pack()

	def submit(self):
		global userCode
		userCode = self.text.get("1.0", tk.END)
		print("Submited !")

root = tk.Tk()
editor = EditorSetUp(root)
root.mainloop()