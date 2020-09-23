#!/usr/bin/python3
from tkinter import *


def helloCallBack():
	sub_ventana2 = Frame(inicio_ventana, width="200", height="50")
	sub_ventana2.place(x=200, y=400)
	sub_ventana2.config(bg='#BABDB6')

	if int(input_texto_edad.get()) >= 18 : 

		if int(input_texto_edad.get()) <= 70 :
			if var1.get() == 1:
				votar_i = "SI TIENE PERMITIDO  PARA  VOTAR\n "+ input_texto_nombre.get()
				votar_si_inprimiir = Label(sub_ventana2, text=votar_i, bg="#33AA57")
				votar_si_inprimiir.pack()				
			elif var1.get() == 2:
				votar_sii = "NO TIENE PERMITIDO PARA VOTAR\nPOR NO INSCRIBIR "+ input_texto_nombre.get()
				votar_si_inprimire= Label(sub_ventana2, text=votar_sii, bg="red")
				votar_si_inprimire.pack()
			else:
				votar_s = "NO A SELECINADO \nSI O NO "+ input_texto_nombre.get()
				votar_si_inprimi= Label(sub_ventana2, text=votar_s, bg="red")
				votar_si_inprimi.pack()
				

		else:
			if var1.get()==1:
				votar_no_70 = "NO TIENE PERMITIDO VOTAR  \nTIENES MAS DE 70 AÑOS "+ input_texto_nombre.get()
				votar_si_inprimir= Label(sub_ventana2,text=votar_no_70, bg="red")
				votar_si_inprimir.pack()
			elif var1.get() == 2:
				votar_no = "NO TIENE PERMITIDO PARA VOTAR\nPOR NO INSCRIBIR LA CEDULA "+ input_texto_nombre.get()
				votar_si_inprimirno= Label(sub_ventana2, text=votar_no, bg="red")
				votar_si_inprimirno.pack()
			else:
				votar_si = "NO A SELECINADO SI O NO "+ input_texto_nombre.get()
				votar_si_inprimir= Label(sub_ventana2, text=votar_si, bg="red")
				votar_si_inprimir.pack()

	else:
		if var1.get() == 1:
			nombre_menor = "NO TIENES PERMISO DE VOTAR\nPOR SER MENOR DE EDAD " + input_texto_nombre.get()
			votar_si_inprimir = Label(sub_ventana2,text=nombre_menor, bg="red")
			votar_si_inprimir.pack()
		elif var1.get() == 2:
			votar_no = "NO TIENE PERMITIDO PARA VOTAR\nPOR NO INSCRIBIR LA CEDULA "+ input_texto_nombre.get()
			votar_si_inprimir= Label(sub_ventana2, text=votar_no, bg="red")
			votar_si_inprimir.pack()
		else:
			votar_si = "NO A SELECINADO SI O NO "+ input_texto_nombre.get()
			votar_si_inprimir= Label(sub_ventana2, text=votar_si, bg="red")
			votar_si_inprimir.pack()


inicio_ventana = Tk()
inicio_ventana.title("VERIFICAR VOTO")
inicio_ventana.geometry("600x500")
inicio_ventana.resizable(width=False, height=False)
inicio_ventana.config(bg="#BABDB6")

sub_ventana = Frame(inicio_ventana, width="450", height="250")
sub_ventana.place(x=75, y=150)
sub_ventana.config(bg="#EEEEEC")

photo = PhotoImage(file = "co.png")
inicio_ventana.iconphoto(False, photo)
avatar = PhotoImage(file="4887.gif")


titulo_h2= Label(inicio_ventana,text="Comprobar si tiene \npermiso de votar ", font=("Arial Bold", 22,), bg="#BABDB6", fg="#000000")
titulo_h2.place(x=160, y=50)

imagenn=Label(sub_ventana, image=avatar)
imagenn.place(x=12, y=25)

texto_nombre = Label(sub_ventana,text="SU NOMBRE:",bg="#EEEEEC", fg="#000000")
texto_nombre.place(x=180, y=30)
input_texto_nombre = Entry(sub_ventana, bg="#FFFFFF", fg="#000000")
input_texto_nombre.focus()
input_texto_nombre.place(x=180, y=60)

texto_edad = Label(sub_ventana,text="SU EDAD:", bg="#EEEEEC", fg="#000000")
texto_edad.place(x=180, y=90)
input_texto_edad = Entry(sub_ventana,  bg="#FFFFFF", fg="#000000")
input_texto_edad.place(x=180, y=120)

exitButton = Button(sub_ventana, text="COMPROBAR", command=helloCallBack, borderwidth=6, bg="#F57900")
exitButton.place(x=220, y=205)

textosiono = Label(sub_ventana,text="SU CEDULA LA INSCRIBIO:", bg="#EEEEEC", fg="#000000")
textosiono.place(x=180, y=147)
var1 = IntVar()
x = Radiobutton(sub_ventana, text="SI", variable=var1, value=1, borderwidth=6, bg="#F57900").place(x=180, y=170)
xx = Radiobutton(sub_ventana, text="NO", variable=var1, value=2, borderwidth=6, bg="#F57900").place(x=250, y=170)

inicio_ventana.mainloop()
#.delete(0, "end")