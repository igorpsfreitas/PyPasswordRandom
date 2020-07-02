from tkinter import *
from gerador import *

main = Tk()
main.title("Gerador de Senhas")
main.resizable(False, False)
#main.geometry("200x200")

digitos = IntVar()
cA = BooleanVar()
numer = BooleanVar()
Simbol = BooleanVar()

def Click():
    digitos = int(recDigito.get())
    senha = GerarSenha(digitos, cA.get(), numer.get(), Simbol.get())
    visor.delete(0, END)
    visor.insert(0, senha)

labelDigitus = Label(main, text = 'Digitos:')
recDigito = Entry(main, width = 5)
visor = Entry(main, bd = 5)
botao = Button(main, text = "Gerar", command = lambda: Click())
check01 = Checkbutton(main, text = "Maiuscul", variable = cA, onvalue = True, offvalue = False)
check02 = Checkbutton(main, text = "Numeros", variable = numer, onvalue = True, offvalue = False)
check03 = Checkbutton(main, text = "Simbolos", variable = Simbol, onvalue = True, offvalue = False)



botao.grid(row = 1, column = 1)
visor.grid(row = 1, column = 2, columnspan = 2)
check01.grid(row = 2, column = 1)
check02.grid(row = 3, column = 1)
labelDigitus.grid(row = 3, column = 3)
recDigito.grid(row = 4, column = 3, rowspan = 2)
check03.grid(row = 4, column = 1)
main.mainloop()
