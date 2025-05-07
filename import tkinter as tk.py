import tkinter as tk

# Text based caulculator functions
def text_add(x, y):
    return x + y

def text_subtract(x, y):
    return x - y

def text_multiply(x, y):
    return x * y 

def text_divide(x, y):
    if y==0 :
        return "Error! Division by zero."
    return x/y

def text_calculator():
    while True:
        print("\n== SImpla Calculator (Text Mode) === ")
        print("1. Add")
        print("2. Subtract")
        print("3. Multiply")
        print("4. Divide")
        print("5. Exixt")

        choice = input("Choose an option (1-5): ")

        if choice == '5':
            print("Goodbye")
            break
        try:
            a = float(input("Enter first number:"))
            b = float(input("Enter first number:"))
        except ValueError:
            print("invalid input. Please enter number.:")
            continue

        if choice == '1':
            print(f"Result: {text_add(a, b)}")
        elif choice == '2':
            print(f"Result: {text_subtract(a, b)}")
        elif choice == '3':
            print(f"Result: {text_multiply(a, b)}")
        elif choice == '4':
            print(f"Result: {text_divide(a, b)}")
        else:
            print("invalid choice, try again.")

# gui calc
def gui_click(event):
    current = gui_entry.get ()
    button_text = event.widget.cget("text")

    if button_text == '=':
        try:
            result = eval(current)
            gui_entry.delete(0, tk.END)
            gui_entry.insert(0, result)
        except Exception:
             gui_entry.delete(0, tk.END)
             gui_entry.insert(0, "Error")
    elif button_text == "C":
        gui_entry.delete(0, tk.END)
    else:
        gui_entry.insert(tk.END, button_text)

def gui_calculator():
    global gui_entry
    root = tk.Tk()
    root.title("Simple Calculator (GUI Mode)")

    gui_entry = tk.Entry(root, font = "Arial 20")
    gui_entry.grid(row=0, column=0, columnspan=4, sticky="nsew")

    buttons = [
        "7", "8", "9", "/",
        "4", "5", "6", "*",
        "1", "2", "3", "-",
        "0", "C", "=", "+",
    ]

    row_val = 1
    col_val = 0

    for button in  buttons:
        b = tk.Button(root, text=button, font="Arial 18", height=2, width=5)
        b.grid(row=row_val, column=col_val, sticky="nsew")
        b.bind("<Button-1>", gui_click)

        col_val += 1
        if col_val > 3:
            col_val = 0
            row_val += 1

    for i in range(5):
        root.grid_rowconfigure(i, weight=1)
        root.grid_columnconfigure(i, weight=1)
    root.mainloop()

if __name__== "__main__":
    print("Choose mode:")
    print("1. Text Calculator")
    print("2. GUI Calculator")
    mode = input("Enter 1 or 2: ")


    if mode == '1':
        text_calculator()
    elif mode == '2':
        gui_calculator()
    else:
        print("invalid choice. Existing.")