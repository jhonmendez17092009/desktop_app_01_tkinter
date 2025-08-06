
from tkinter import *

# -----------------------------------------------------
#funciones de la app
#------------------------------------------------------


#------------------------------------------------------
# ventana principal
#------------------------------------------------------

# Se declara una variable llamada ventana_principal, que adquiere ls carcteristicas de un objeto de tipo TK()
ventana_principal = Tk()

#Titulo de la ventana
ventana_principal.title("Jhoasnel Mendez")

#Tamaño de laventana
ventana_principal.geometry("800x500")

#desavilitar boton maximizar
ventana_principal.resizable(0,0)

#color de fondo de la ventana
ventana_principal.config(bg="black")

#-------------------------
# variables globales
#--------------------------
a=StringVar()
b=StringVar()
c=IntVar()


#_-------------------------
# frame 1 - entrada de datos
#--------------------------
frame_1= Frame(ventana_principal)
frame_1.config(bg="ivory2", width=780,height=240)
frame_1.place(x=10,y=10)

# imagen logo de la app
logo = PhotoImage(file="img/btn-suma.png")
Label_logo=Label(frame_1,image=logo)
Label_logo.place(x=10,y=10)
# etiqueta para el titulode la app
titulo = Label(frame_1,text=" Colegio San José de Guanenta")
titulo.config(bg="yellow", fg="blue",font=("arial",16))
titulo.place(x=390,y=10)
# Etiqueta para sunbtitulo 1 de la app
subtitulo1 = Label(frame_1,text="  Especialidad en sistemas")
subtitulo1.config(bg="yellow",fg="blue",font=("arial",12))
subtitulo1.place(x=390,y=40)
#Etiqueta subtitulo2
subtitulo2 = Label(frame_1,text="SUMA DE DOS ENTEROS")
subtitulo2.config(bg="ivory2",fg="blue",font=("arial",15),anchor=CENTER)
subtitulo2.place(x=390,y=70)
#Etiqueta el primer vaolr
label_a = Label(frame_1,text="a = ")
label_a.config(bg="ivory2",fg="blue",font=("arial",20),anchor=CENTER)
label_a.place(x=390,y=120)
# Entry para el primer valor(a)
entry_a=Entry(frame_1, width=4, textvariable=a)
entry_a.config(font=("Arial",20), justify=CENTER)
entry_a.focus_set()
entry_a.place(x=487, y=120)

# en
label_b = Label(frame_1, text =" b  " )
label_b.config(bg="ivory2" , fg="blue", font=("arial", 20), anchor = CENTER   )
label_b.place(x = 585 , y = 120)

# entry para el segundo valor 
    
entry_b = Entry(frame_1, width=4 , textvariable = a)
entry_b.config(font=("Arial", 20), justify=CENTER)
entry_b.focus_set()
entry_b.place(x = 682 , y = 120)
# -----------------------------

#_-------------------------
# frame 2 - panel de operaciones
#--------------------------
frame_2= Frame(ventana_principal)
frame_2.config(bg="ivory2", width=780,height=120)
frame_2.place(x=10,y=260)
# boton para sumar
img_bt_sumar = PhotoImage(file="img/boton_sumar.png")
bt_sumar = Button(frame_2, image = img_bt_sumar, width = 105, height = 105)
# bt_sumar=Button(frame_2, text="Sumar", width=10)
bt_sumar.place(x =166, y = 7)
# boton para borrar entrada y resultados
img_bt_borrar = PhotoImage(file="img/boton_borrar.png")
bt_borrar = Button(frame_2, image = img_bt_borrar, width = 105, height = 105)
# bt_sumar=Button(frame_2, text="Sumar", width=10)
bt_borrar.place(x =337, y = 7)
# boton para cerrar la app
img_bt_salir = PhotoImage(file="img/boton_salir.png")
bt_salir = Button(frame_2, image = img_bt_salir, width = 105, height = 105)
# bt_sumar=Button(frame_2, text="Sumar", width=10)
bt_salir.place(x = 558, y = 7)


#--------------------------
# frame 3 -Resultado
#--------------------------
frame_3= Frame(ventana_principal)
frame_3.config(bg="ivory2", width=780,height=100)
frame_3.place(x=10,y= 390)
# area de texto
t_resultados = Text(frame_3, width=50, height=3)
t_resultados.config(bg="green", fg="white", font=("Courier", 20))
t_resultados.pack()
#Metodo principal quedespiega la ventana en pantalla
ventana_principal.mainloop()