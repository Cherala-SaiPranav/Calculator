from tkinter import *

root = Tk()
root.title("Calculator")
root.geometry("300x400")
root.configure(bg="#2E2E2E")

display_frame = Frame(root, bg="black", height=70)
display_frame.pack(padx=4, pady=5, fill=BOTH)
# Button frame
button_frame = Frame(root, bg="#2E2E2E")
button_frame.pack(padx=4, pady=5)

# Button layout
buttons = [
    ('7', 1, 0), ('8', 1, 1), ('9', 1, 2), ('/', 1, 3),
    ('4', 2, 0), ('5', 2, 1), ('6', 2, 2), ('*', 2, 3),
    ('1', 3, 0), ('2', 3, 1), ('3', 3, 2), ('-', 3, 3),
    ('0', 4, 0), ('.', 4, 1), ('+', 4, 2), ('=', 4, 3),
]

for (text, row, col) in buttons:
    button = Button(button_frame, text=text, font=("Arial", 18), bg="#4CAF50" if text == "=" else "#2E2E2E", 
                    fg="white", padx=20, pady=20)
    button.grid(row=row, column=col, padx=4, pady=4, sticky="nsew")
# Configure grid layout for equal column and row expansion
for i in range(6):
    button_frame.rowconfigure(i, weight=1)
for j in range(4):
    button_frame.columnconfigure(j, weight=1)

root.mainloop()
