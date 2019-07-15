import tkinter
from tkinter import*
from tkinter import messagebox

def caesar():
    menu=Tk()
    menu.title("Perhitungan Caesar")
    menu.geometry("300x150")
    L1=Label(menu,text="Masukkan Pesan")
    L1.pack()
    L1.place(x=25, y=40)
    E1=Entry(menu,bd=5)
    E1.pack()
    E1.place(x=125, y=40)

    def callback():
        ubah=E1.get()
        alphabet = ['a','b','c','d','e','f','g','h','i','j','k','l','m','n','o','p','q','r','s','t','u','v','w','x','y','z']
        key=3
        plain= ' '

        for c in ubah:
            if c in alphabet:
                plain += alphabet[(alphabet.index(c)+key)%(len(alphabet))]
        print (plain)

        messagebox.showinfo("asdas",("Hasil : " + plain))

    B1=Button(menu, text="Convert",command = callback)
    B1.pack()
    B1.place(x=200, y=100)

    def delete():
        menu.destroy()

    B2=Button(menu, text="Back",command = delete)
    B2.pack()
    B2.place(x=50, y=100)    
    menu.mainloop()

def biner():
    box=Tk()
    box.title("Perhitungan Biner")
    box.geometry("300x150")
    L2=Label(box,text="Masukan Pesan")
    L2.pack()
    L2.place(x=25, y=40)
    E2=Entry(box,bd=5)
    E2.pack()
    E2.place(x=125, y=40)
    def binary ():
        ubah=E2.get()
        binary=[]

        def strBin(s_str):
            for s in s_str:
                if s == ' ':
                    binary.append('00100000')
                else:
                    binary.append(bin(ord(s)))
        s_str = ubah
        strBin(s_str)

        b_str = '\n'.join(str(b_str) for b_str in binary)
        print(b_str.replace('b', ''))

        messagebox.showinfo("Enkripsi Biner",("Hasil : \n"+ (b_str.replace('b', ''))))
        
    B2=Button(box, text="Convert", command=binary)
    B2.pack()
    B2.place(x=200, y=100)

    def delete():
        box.destroy()
        
    B3=Button(box, text="Back",command = delete)
    B3.pack()
    B3.place(x=50, y=100)   
    box.mainloop()
    
top = Tk()
top.title("Code Conversion")
top.geometry("300x100")

L1 = Label(top, text="Pilih Metode Enkripsi")
L1.pack()

B1 = Button(top, text="Caesar", command=caesar)
B1.pack()
B1.place(x=75, y=50)

B2 = Button(top, text="Biner", command=biner)
B2.pack()
B2.place(x=180, y=50)

top.mainloop()

