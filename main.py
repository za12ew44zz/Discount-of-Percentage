from tkinter import *

root = Tk()
window_width = 320
window_height = 400
screen_width = root.winfo_screenwidth()
screen_height = root.winfo_screenheight()
x_axis = (screen_width / 2) - (window_width / 2)
y_axis = (screen_height / 2) - (window_height /2)

root.geometry("{}x{}+{}+{}".format(window_width,window_height,int(x_axis),int(y_axis)))
root.resizable(0,0)



root.title("Discount Calculator")
txt = StringVar()
txt2 = StringVar()
Font_tuple = ("Comic Sans MS", 20, "bold")

def cal():
    amount = txt.get()
    discount = txt2.get()
    intAmount = int(amount)
    intDiscount = int(discount)
    result = intAmount - (intAmount * intDiscount / 100)
    resultText = Label(root,text=result,font=Font_tuple).grid(row=6,column=1) 


myLabel1 = Label(root,text="Amount",font=Font_tuple).grid(row=1,column=1)
amount = Entry(root,textvariable=txt,width="20",font=Font_tuple).grid(row=2,column=1)
myLabel2 = Label(root,text="Percentage of Discount",font=Font_tuple).grid(row=3,column=1)
myDiscountPercent = Entry(root,textvariable=txt2,width="20",font=Font_tuple).grid(row=4,column=1)
btnCal = Button(root,text="Calculate",command=cal,font=Font_tuple).grid(row=5,column=1)

root.mainloop()