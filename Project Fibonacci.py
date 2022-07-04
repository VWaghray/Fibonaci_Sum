from tkinter import *
root = Tk()
root.title("Fibonacci")
root.geometry("400x400")

label_series = Label(root, text = 'Fibonacci Series: ')
label_spiral = Label(root)
Entry_Vihaan = Entry(root)

def Fibonacci():
    num = int(Entry_Vihaan.get())
    num1 = 0
    num2 = 1
    sum = 0
    sum2 = 0
    i=1
    while(i<=num):
        label_series['text'] += str(sum) + " "
        label_spiral['text'] = "Fibonacci Sum: " + str(sum2)
        i=i+1
        num1 = num2
        num2 = sum
        sum = num1 + num2
        sum2 = sum2 + sum
        
   

btn = Button(root, text = 'Show Fibonacci series', command=Fibonacci)
Entry_Vihaan.pack()
btn.pack()
label_series.pack()
label_spiral.pack()


root.mainloop()