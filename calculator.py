from tkinter import *
root = Tk()
root.title(" Jarvis Calculator)")
root.geometry("380x550+650+150")
root.resizable(False,False)
###                  Functions              ################
def enterNumber(x):
    if entry_box.get() == "O":
        entry_box.delete(0,'end')
        entry_box.insert(0,str(x))
    else:
        length = len(entry_box.get())
        entry_box.insert(length,str(x))

def enterOperator(x):
    if entry_box.get() != "O":
        length = len(entry_box.get())
        entry_box.insert(length,btn_operators[x]['text'])

def funcClear():
    entry_box.delete(0,END)
    entry_box.insert(0,"O")
def funcdel():
    length = len(entry_box.get())
    entry_box.delete((length-1),'end')
result = 0
result_list = []
def funcOperator():
    content = entry_box.get()
    result = eval(content)
    print(result)
    entry_box.delete(0, 'end')
    entry_box.insert(0, str(result))

    result_list.append(content)
    result_list.reverse()
    statusBar.configure(text='History : '+'|'.join(result_list[:5]),font = 'verdana 10')

##        Entry Box           #############################

entry_box = Entry(font='verdana 14 bold',width=22,bd=10,justify=RIGHT, bg='#e6e6fa')
entry_box.insert(0,"O")
entry_box.place(x=20,y=10)

##          Buttons  NUmbers        #################################
btn_numbers=[]
for i in range(10):
    btn_numbers.append(Button(width=4,text=str(i),font='times 15 bold',bd=5,
                              command= lambda x=i: enterNumber(x)))
btn_text=1
for i  in range(0,3):
    for j in range (0,3):
        btn_numbers[btn_text].place(x=25+j*90,y=70+i*70)
        btn_text +=1
##          Button Operators        ######################33
btn_operators=[]
for i in range(4):
    btn_operators.append(Button(width=4,font='times 15 bold',bd=5, command = lambda x=i:enterOperator(x)))
btn_operators[0]['text']="+"
btn_operators[1]['text']="-"
btn_operators[2]['text']="*"
btn_operators[3]['text']="/"

for i in range(4):
    btn_operators[i].place(x=290,y=70+70*i)

##### Other Buttons #########################################
btn_zero = Button(width=19,text = '0', font = 'times 15 bold',bd=5, command=lambda x=0: enterNumber(x))
btn_clear = Button(width=4,text = 'C', font = 'times 15 bold',bd=5, command=funcClear)
icon = PhotoImage(file='arrow.png')
btn_del = Button(width=50, height =35 ,font = 'times 15 bold',bd=5, command=funcdel,image=icon)
btn_equal = Button(width=4,text = '=', font = 'times 15 bold',bd=5, command=funcOperator)
btn_zero.place(x=25, y=280)
btn_clear.place(x=25 , y=340)
btn_del.place(x=110 , y=340)
btn_equal.place(x=195 , y=340)


################### STATUS BAR #####################################

statusBar = Label(root,text='History: ', relief=SUNKEN,height=3,font = 'verdana 11 bold',anchor=W)
statusBar.pack(side=BOTTOM,fill=X)


root.mainloop()

