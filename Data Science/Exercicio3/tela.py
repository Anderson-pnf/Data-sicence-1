import tkinter as tk

    
janela = tk.Tk()

janela.geometry('300x300')

janela.title("Notas")

def lista():
    
    n = float(input.get())
    n1 = float(input1.get())
    n2 = float(input2.get())
    n3 = float(input3.get())

    lista = []
    lista += (n,n1,n2,n3)
    print(lista)

texto = tk.Label(janela,text="Calculo de notas")
texto.grid(row = 1, column = 3, padx= 85, pady= 5)   

input = tk.Entry(janela)
input.grid(row= 2, column= 3, padx= 85, pady= 5)

input1 = tk.Entry(janela)
input1.grid(row= 3, column= 3, padx= 85, pady= 5)

input2 = tk.Entry(janela)
input2.grid(row= 4, column= 3, padx= 85, pady= 5)

input3 = tk.Entry(janela)
input3.grid(row= 5, column= 3, padx= 85, pady= 5)

btn = tk.Button(janela, text='Resultados', command= lista)
btn.grid(row=6,column=3, padx= 85, pady= 5)


janela.mainloop()