import tkinter as tk
import math
# 导入了 tkinter 模块用于创建 GUI 界面，以及 math 模块用于执行数学运算。

# 创建主窗口
root = tk.Tk()
root.title("Simple Calculator")
root.configure(bg="#B8BBDE")  # 设置窗口背景颜色

# 设置主窗口大小
root.geometry("300x400")

# 创建显示结果的文本框
result_display = tk.Entry(root, width=20, font=("Helvetica", 32))
result_display.grid(row=0, column=0, columnspan=4, sticky="nsew")
result_display.configure(bg="white")  # 设置文本框背景颜色

# 设置网格布局的权重，使按钮大小相同
for i in range(2):
    root.grid_rowconfigure(i, weight=1)
    root.grid_columnconfigure(i, weight=1)

# 创建按钮点击事件
def button_click(event):
    current_text = result_display.get()
    button_text = event.widget.cget("text")

    if button_text == "=":
        try:
            # 替换幂运算符号并计算
            current_text = current_text.replace("^", "**")
            # 替换三角函数并计算
            current_text = current_text.replace("sin", "math.sin")
            current_text = current_text.replace("cos", "math.cos")
            current_text = current_text.replace("tan", "math.tan")
            # 替换π
            current_text = current_text.replace("π", str(math.pi))
            result = eval(current_text)
            result_display.delete(0, tk.END)
            result_display.insert(tk.END, str(result))
        except Exception as e:
            result_display.delete(0, tk.END)
            result_display.insert(tk.END, "错误")
    elif button_text == "C":
        result_display.delete(0, tk.END)
    elif button_text in ["(", ")"]:
        result_display.insert(tk.END, button_text)
    elif button_text == "π":
        result_display.insert(tk.END, "π")
    else:
        result_display.insert(tk.END, button_text)

# 创建按钮
buttons = [
    '7', '8', '9', '/',
    '4', '5', '6', '*',
    '1', '2', '3', '-',
    '0', '.', '=', '+',
    'C',
    'sin', 'cos', 'tan', '^',  # 添加三角函数和幂运算按钮
    '(', ')',  # 添加左右括号按钮
    'π'  # 添加π按钮
]

row, col = 1, 0
for button_text in buttons:
    button = tk.Button(root, text=button_text, font=("Helvetica", 20))
    button.grid(row=row, column=col, sticky="nsew")
    col += 1
    if col > 3:
        col = 0
        row += 1

    button.bind("<Button-1>", button_click)
    button.configure(bg="#E6E6FA")  # 设置按钮背景颜色

# 运行应用程序
root.mainloop()