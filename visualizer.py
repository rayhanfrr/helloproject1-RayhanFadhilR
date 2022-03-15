import time
from tkinter import *
from tkinter import ttk

import random

DARK_GREY = '#65696B'
LIGHT_GREY = '#C4C5BF'
BLUE = '#0CA8F6'
DARK_BLUE = '#4204CC'
WHITE = '#FFFFFF'
BLACK = '#000000'
RED = '#F22810'
YELLOW = '#F7E806'
PINK = '#F50BED'
LIGHT_GREEN = '#05F50E'
PURPLE = '#BF01FB'

def partisi(arr, kecil, besar):
    pivot = arr[besar]
    i = kecil - 1

    for j in range(kecil, besar):
        if (arr[j] <= pivot):
            i = i + 1
            (arr[i], arr[j]) = (arr[j], arr[i])
    (arr[i+1], arr[besar]) = (arr[besar], arr[i+1])

    return i + 1

def quickSort(arr, kecil, besar, drawData, timeTick):
    if (kecil < besar):
        pi = partisi(arr, kecil, besar)
        quickSort(arr, kecil, pi - 1, drawData, timeTick)
        quickSort(arr, pi + 1, besar, drawData, timeTick)

        drawData(arr, [PURPLE if x >= kecil and x < pi else YELLOW if x == pi else DARK_BLUE if x > pi and x <= besar else BLUE for x in range(len(arr))])

        time.sleep(timeTick)

    drawData(arr, [BLUE for x in range(len(arr))])

def shellSort(arr, drawData, timeTick):
    n = len(arr)
    gap = n//2

    while gap > 0:
        for i in range(gap, n):
            temp = arr[i]
            j = i
            while j >= gap and arr[j-gap] > temp:
                arr[j] = arr[j-gap]
                j -= gap
                drawData(arr, [YELLOW if x == j or x == j+1 else BLUE for x in range(len(arr))])
                time.sleep(timeTick) 
            arr[j] = temp
        gap //=2
    
    drawData(arr, [BLUE for x in range(len(arr))])

window = Tk()
window.title("Sorting Algorithms Visualization")
window.maxsize(1000, 700)
window.config(bg = WHITE)

algorithm_name = StringVar()
algo_list = ['Quick Sort', 'Shell Sort']

speed_name = StringVar()
speed_list = ['Fast', 'Medium', 'Slow']

arr = []

def drawData(arr, colorArray):
    canvas.delete("all")
    canvas_width = 800
    canvas_height = 400
    x_width = canvas_width / (len(arr) + 1)
    offset = 4
    spacing = 2
    normalizedData = [i / max(arr) for i in arr]

    for i, height in enumerate(normalizedData):
        x0 = i * x_width + offset + spacing
        y0 = canvas_height - height * 390
        x1 = (i + 1) * x_width + offset
        y1 = canvas_height
        canvas.create_rectangle(x0, y0, x1, y1, fill=colorArray[i])

    window.update_idletasks()

def generate():
    global arr

    arr = []
    for i in range(0, 100):
        random_value = random.randint(1, 150)
        arr.append(random_value)

    drawData(arr, [BLUE for x in range(len(arr))])

def set_speed():
    if speed_menu.get() == 'Slow':
        return 0.3
    elif speed_menu.get() == 'Medium':
        return 0.1
    else:
        return 0.001

def sort():
    global arr
    timeTick = set_speed()

    if algo_menu.get() == 'Shell Sort':
        shellSort(arr, drawData, timeTick)
    elif algo_menu.get() == "Quick Sort":
        quickSort(arr, 0, len(arr)-1, drawData, timeTick)

UI_frame = Frame(window, width=990, height=300, bg= WHITE)
UI_frame.grid(row=0, column=0, padx=10, pady=5)

l1 = Label(UI_frame, text="Algorithm: ", bg= WHITE)
l1.grid(row=0, column=0, padx=10, pady=5, sticky=W)
algo_menu = ttk.Combobox(UI_frame, textvariable=algorithm_name, values=algo_list)
algo_menu.grid(row=0, column=1, padx=5, pady=5)
algo_menu.current(0)

l2 = Label(UI_frame, text="Sorting Speed: ", bg=WHITE)
l2.grid(row=1, column=0, padx=10, pady=5, sticky=W)
speed_menu = ttk.Combobox(UI_frame, textvariable=speed_name, values=speed_list)
speed_menu.grid(row=1, column=1, padx=5, pady=5)
speed_menu.current(0)

b1 = Button(UI_frame, text="Sort", command=sort, bg=LIGHT_GREY)
b1.grid(row=2, column=1, padx=5, pady=5)

b3 = Button(UI_frame, text="Generate Array", command=generate, bg=LIGHT_GREY)
b3.grid(row=2, column=0, padx=5, pady=5)

canvas = Canvas(window, width=800, height=400, bg=WHITE)
canvas.grid(row=1, column=0, padx=10, pady=5)

window.mainloop()