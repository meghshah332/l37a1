from tkinter import *

root = Tk()
root.title('Number Pad')
root.geometry('450x500')


nums = [[9, 8, 7], [6, 5, 4], [3, 2, 1], ['#', 0, '*']]

for i in range(4):
	root.columnconfigure(i, weight=1, minsize=125)
	root.rowconfigure(i, weight=1, minsize=100)
	for j in range(0, 3):
		frame = Frame(
			master=root,
			relief=SUNKEN,
			borderwidth=1
		)
		frame.grid(row=i, column=j)
		label = Label(master=frame, text=nums[i][j], fg="#00aaff", font=('algerian', 18, "bold"))
		label.pack(padx=4, pady=4)

root.mainloop()