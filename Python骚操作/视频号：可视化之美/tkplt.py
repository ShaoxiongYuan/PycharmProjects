import tkinter as tk
import matplotlib.pyplot as plt
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg

# 第1步，实例化object，建立窗口window
window = tk.Tk()

# 第2步，给窗口的可视化起名字
window.title('My Window')

# 第3步，设定窗口的大小(长 * 宽)
# 这里的乘是小x
window.geometry('1200x600')

# 第4步，在图形界面上创建一个标签label用以显示并放置
# 定义一个var用来将radiobutton的值和Label的值联系在一起.
var = tk.StringVar()
l = tk.Label(window, bg='yellow', width=30, height=3,
             text='matplotlib in tkinter', font=('Arial', 21))

l.pack()


# 第6步，定义选项触发函数功能
def show_selection():
    l.config(text='you have selected ' + var.get())
    if var.get() == 'bar':
        ax_l.set_visible(True)
        ax_r.set_visible(False)
    elif var.get() == 'pie':
        ax_l.set_visible(False)
        ax_r.set_visible(True)
    else:
        ax_l.set_visible(True)
        ax_r.set_visible(True)
    canvas_l.draw()
    canvas_r.draw()


# 第7步，创建三个radiobutton选项，其中variable=var,
# value='A'的意思就是，当我们鼠标选中其中一个选项，把value的值A放到变量var中，
# 然后赋值给variable
r1 = tk.Radiobutton(window, text='bar', variable=var,
                    value='bar', command=show_selection,
                    font=('Arial', 21))
r1.pack()
r2 = tk.Radiobutton(window, text='pie', variable=var,
                    value='pie', command=show_selection,
                    font=('Arial', 21))
r2.pack()
r3 = tk.Radiobutton(window, text='both', variable=var,
                    value='both', command=show_selection,
                    font=('Arial', 21))
r3.pack()

# 第8步，创建一个主frame，长在主window窗口上
frame = tk.Frame(window)
frame.pack()
# 创建第二层框架frame，长在主框架frame上面
# 第二层frame，左frame，长在主frame上
frame_l = tk.Frame(frame)
# 第二层frame，右frame，长在主frame上
frame_r = tk.Frame(frame)
frame_l.pack(side='left')
frame_r.pack(side='right')

# 第9步
figure_l = plt.figure(figsize=(3, 5))
labels = ['1', '2', '3', '4', '5']
men_means = [20, 35, 30, 35, 27]
women_means = [25, 32, 34, 20, 25]
width = 0.35
figure_l, ax_l = plt.subplots(figsize=(3, 5))
ax_l.bar(labels, men_means, width, label='Men')
# bottom
ax_l.bar(labels, women_means, width, bottom=men_means, label='Women')
canvas_l = FigureCanvasTkAgg(figure_l, frame_l)
canvas_l.draw()
canvas_l.get_tk_widget().pack()

figure_r = plt.figure(figsize=(3, 5))
ax_r = figure_r.gca()
labels = 'Frogs', 'Hogs', 'Dogs'
sizes = [15, 30, 45]
# 设置分离的距离，0表示不分离
explode = (0, 0.1, 0)
plt.pie(sizes, explode=explode, labels=labels, autopct='%1.1f%%',
        shadow=True, startangle=90)
canvas_r = FigureCanvasTkAgg(figure_r, frame_r)
# 用draw代替，但是用show不会报错，会显示警告
canvas_r.draw()
canvas_r.get_tk_widget().pack()

# 第10步，主窗口循环显示
window.mainloop()
