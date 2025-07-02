import requests
import tkinter as tk
from tkinter import Frame, Entry, Label, StringVar, LEFT, RIGHT, X, TOP
def main():

    # ta część kodu przestała działać w związku ze zmianą API
    """
    wyniki14 = (requests.get('http://app.lotto.pl/wyniki/?type=mm14').text).split()
    wyniki22 = (requests.get('http://app.lotto.pl/wyniki/?type=mm22').text).split()
 
    dat_g14 = wyniki14[0] + ('  14:00')
    wyniki14 = sorted([int(i) for i in wyniki14[1:]])
 
    dat_g22 = wyniki22[0] + ('  21:40')
    wyniki22 = sorted([int(i) for i in wyniki22[1:]])
    """

    # do wersji demo zostały użyte ręcznie wpisane przykładowe liczby
    wyniki14 = sorted([4, 16, 22, 33, 35, 37, 43, 47, 52, 60])
    wyniki22 = sorted([1, 5, 11, 22, 33, 34, 41, 46, 54, 57])

    dat_g14 = (' 14:00')
    dat_g22 = (' 21:40')

    root = tk.Tk()
    root.title("Multi v3.0")
    root.geometry("650x200")
    d_font = 'Verdana 14'
    header_font = 'Verdana 12'
    root.option_add("*Font", d_font)
    in_frame = Frame(root)
    header = Frame(root)
 
    #główny frame
    label = Label(header, font=header_font, text="Wprowadź do porównania: ")
    label.pack(side=LEFT)
 
    golde_nums = StringVar()
    golde_nums.set('22, 33, 34, 37, 41, 43, 46, 47, 51, 54, 57, 60')
    entry = Entry(header, textvariable=golde_nums, font=header_font)
    entry.pack(expand=True, side=RIGHT, fill=X)
 
    #in_frame labels
    label = Label(in_frame) # free space
    label.grid(row=1)
 
    label = Label(in_frame, text=dat_g14, anchor='center')
    label.grid(row=2)
 
    create_multicolor_label(wyniki14, golde_nums.get().split(', '), in_frame, 3)
 
    label = Label(in_frame, text='-'*64)
    label.grid(row=4)
 
    label = Label(in_frame, text=dat_g22, anchor='center')
    label.grid(row=5)
 
    create_multicolor_label(wyniki22, golde_nums.get().split(', '), in_frame, 6)
 
    label = Label(in_frame) # free space
    label.grid(row=7)
 
    header.pack(side=TOP, fill=X)
    in_frame.pack()
 
    def update():
        create_multicolor_label(wyniki14, golde_nums.get().split(', '), in_frame, 3)
        create_multicolor_label(wyniki22, golde_nums.get().split(', '), in_frame, 6)
        root.after(1500, update)
 
    root.bind("<Escape>", lambda escape: root.destroy())
    #root.after(1500, update)    automatyczny refresh
    root.mainloop()
 
 
def create_multicolor_label(list_1, list_2, in_frame,x):
    try:
        for i in range(len(list_2)):
            list_2[i]=int(list_2[i])
    except:
        return 0
    common_nums = set(list_1).intersection(list_2)
    i1=''
    i2=''
    selected = Frame(in_frame)
 
    for i in list_1:
        if i in common_nums:
            if i2!='':
                label = Label(selected, text=i2)
                label.pack(side=LEFT, fill=X)
            i2=''
            i1+=str(i)+' '
        else:
            if i1!='':
                label = Label(selected, text=i1)
                label.config(fg='red')
                label.pack(side=LEFT, fill=X)
            i1=''
            i2+=str(i)+' '
 
    if i2.strip()!='':
        label = Label(selected, text=i2)
        label.pack(side=LEFT, fill=X)
        del i2
 
    if i1.strip()!='':
        label = Label(selected, text=i1)
        label.pack(side=LEFT, fill=X)
        del i1
 
    selected.grid(row=x)
 
if __name__=="__main__":
    main()
