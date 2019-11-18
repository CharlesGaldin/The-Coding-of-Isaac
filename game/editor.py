import tkinter as tk

userCode = ""

class EditorSetUp:
	def __init__(self):
		self.master = tk.Tk()
		self.master.title("The Coding of Isaac")

		self.label = tk.Label(self.master, text="Your IA:")
		self.label.pack()

		self.text = tk.Text(self.master)
		self.text.insert(tk.INSERT, "try editing")
		self.text.pack()
		
		self.close_button = tk.Button(self.master, text="Submit", command=self.submit)
		self.close_button.pack()

		self.close_button = tk.Button(self.master, text="Close", command=self.master.quit)
		self.close_button.pack()

	def submit(self):
		global userCode
		userCode = self.text.get("1.0", tk.END)
		print("Submited !")
	
	def run(self):
		self.master.mainloop()