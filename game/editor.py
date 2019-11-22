import tkinter as tk
from tkinter import messagebox

class EditorSetUp:
	def __init__(self):
		self.master = tk.Tk()
		self.master.title("The Coding of Isaac")
		
		self.editor = tk.Frame(self.master)
		self.editor.pack(side = tk.RIGHT)

		self.label = tk.Label(self.editor, text="Your IA:")
		self.label.pack()

		self.text = tk.Text(self.editor)
		self.text.insert(tk.INSERT, """#try editing !
#Please use the folowing syntax : 

def turn(grid):
	#--- add your code...

#Available functions: move('*'), attack('*'), get_pos_player(), get_pos_exit(), get_pos_monster() where '*' can be :    'up', 'down', 'left' or 'right'.
#grid gives you the layout of the level
# 
# The code outside turn will be executed once so you can setup some variable
# turn will be executed every turn""")
		self.text.pack()
		
		self.close_button = tk.Button(self.editor, text="Submit", command=self.submit)
		self.close_button.pack()
		
		self.exit_requested = False
		def request_exit():
			self.exit_requested = True
		
		self.close_button = tk.Button(self.editor, text="Close", command=request_exit)
		self.close_button.pack()
		
		self.master.protocol("WM_DELETE_WINDOW", request_exit)

		self.user_code = ""

		self.is_submitted = False

	def submit(self):
		self.user_code = self.text.get("1.0", tk.END)
		self.is_submitted = True
		print("Submitted !")
	
	def update(self):
		self.master.update()
	
	def error_box(self, error):
		messagebox.showerror("Error", error)
	
	def close(self):
		self.master.destroy()