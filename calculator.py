from tkinter import *

def btn_click(value):
    content = display_var.get()
    if value == "=":
        try:
            result = str(eval(content))
            display_var.set(result)
        except Exception as e:
            display_var.set("Error")
    elif value == "C":
        display_var.set("")
    else:
        display_var.set(content + value)

root = Tk()
root.title("Calculator")
root.geometry("300x400")
root.minsize(250, 300)
root.maxsize(450, 550)
root.configure(bg="#2E2E2E")

display_var = StringVar()
display_entry = Entry(root, textvariable=display_var, font=("Arial", 30), bg="black", fg="white", borderwidth=0, justify=RIGHT)
display_entry.pack(padx=4, pady=5, fill=BOTH)

button_frame = Frame(root, bg="#2E2E2E")
button_frame.pack(padx=4, pady=5)

buttons = [
    ('7', 1, 0), ('8', 1, 1), ('9', 1, 2), ('/', 1, 3),
    ('4', 2, 0), ('5', 2, 1), ('6', 2, 2), ('*', 2, 3),
    ('1', 3, 0), ('2', 3, 1), ('3', 3, 2), ('-', 3, 3),
    ('0', 4, 0), ('.', 4, 1), ('+', 4, 2), ('=', 4, 3),
]

for (text, row, col) in buttons:
    button = Button(button_frame, text=text, font=("Arial", 18), bg="#3FC5E9" if text == "=" else "#2E2E2E", 
                    fg="white", padx=20, pady=20, command=lambda value=text: btn_click(value))
    button.grid(row=row, column=col, padx=4, pady=4, sticky="nsew")

# Create and place the clear button
clear_button = Button(button_frame, text='C', font=("Arial", 18), bg="red", fg="white", padx=20, pady=20,
                      command=lambda: btn_click("C"))
clear_button.grid(row=5, columnspan=4, padx=4, pady=4)

# Configure grid layout for equal column and row expansion
for i in range(6):
    button_frame.rowconfigure(i, weight=1)
for j in range(4):
    button_frame.columnconfigure(j, weight=1)

root.mainloop()
