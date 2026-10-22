import tkinter as tk

root = tk.Tk()
root.title("Калькулятор")
root.geometry("350x450")

text_input = tk.Label(root, text="0", anchor="e", bg="white", font=("Arial", 20))
text_input.pack(fill="x", padx=5, pady=5)

text_result = tk.Label(root, text="", anchor="e", bg="white", font=("Arial", 16))
text_result.pack(fill="x", padx=5, pady=5)

def multiply():
    try:
        a, b = map(float, text_input.cget("text").split("*"))
        text_result.config(text=str(a * b))
    except:
        text_result.config(text="Ошибка")

def divide():
    try:
        a, b = map(float, text_input.cget("text").split("/"))
        text_result.config(text=str(a / b))
    except:
        text_result.config(text="Ошибка")

def summy():
    try:
        a, b = map(float, text_input.cget("text").split("+"))
        text_result.config(text=str(a + b))
    except:
        text_result.config(text="Ошибка")

def diff():
    try:
        a, b = map(float, text_input.cget("text").split("-"))
        text_result.config(text=str(a - b))
    except:
        text_result.config(text="Ошибка")

def result():
    try:
        text_result.config(text=str(eval(text_input.cget("text"))))
    except:
        text_result.config(text="Ошибка")

frame = tk.Frame(root)
frame.pack()

for i in range(10):
    btn = tk.Button(frame, text=str(i), width=6, height=2,
                    command=lambda i=i: text_input.config(text=text_input.cget("text") + str(i) if text_input.cget("text") != "0" else str(i)))
    btn.grid(row=i//3, column=i%3, padx=2, pady=2)

operations = [
    ("*", multiply),
    ("/", divide),
    ("+", summy),
    ("-", diff),
    ("=", result)
]

for i, (text, command) in enumerate(operations):
    btn = tk.Button(frame, text=text, width=6, height=2, command=command)
    btn.grid(row=i, column=3, padx=2, pady=2)

root.mainloop()
