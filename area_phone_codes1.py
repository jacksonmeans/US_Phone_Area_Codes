import pandas as pd
#import random
import tkinter as tk

df = pd.read_csv('area-codes-usa.csv')
columns = df.columns
df.drop('latitude',axis=1)
df.drop('longitude',axis=1)

#df = df.groupby('area-code')
df['idx'] = df.groupby(['area-code']).ngroup()
df = df.groupby('idx')

idx = [0]
code = df.first()['area-code'].to_dict()
answer = df.first()['state'].to_dict()

root = tk.Tk()
root.title('U.S. Phone Area Codes')
root.geometry('500x500+380+120')

def increment(idx):
    idx[0] += 1

def skip(idx):
    txt.delete(0,'end')
    lbl2.config(text=f'({code[idx[0]]}) {answer[idx[0]]}')
    increment(idx)
    lbl1.config(text=code[idx[0]])

def guess(code, answer, idx):
    if answer[idx[0]].lower() == txt.get().lower():
        txt.delete(0,'end')
        increment(idx)
        lbl1.config(text=code[idx[0]])
        lbl2.config(text='')

def enter(event):
    guess(code, answer, idx)


lbl1 = tk.Label(root, text=code[idx[0]])
lbl1.pack()

lbl2 = tk.Label(root, text='')
lbl2.pack()

txt = tk.Entry(root)
txt.pack()

txt.bind('<Return>', enter)

btn1 = tk.Button(root, text="Skip", command=lambda: skip(idx))
btn1.place(relx=.35,rely=.3)

btn2 = tk.Button(root, text="Guess", command=lambda: guess(code, answer, idx))
btn2.place(relx=.55,rely=.3)



root.mainloop()
