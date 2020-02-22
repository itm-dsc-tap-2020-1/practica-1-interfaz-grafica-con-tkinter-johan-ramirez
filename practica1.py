import tkinter as tk
from tkinter import ttk
from tkinter import Menu   
from tkinter import messagebox as mbo


def perex():
    if(nombre.get()=="" or apellidop.get()=="" or apellidom.get()=="" or direccion.get()==""):
        mbo.showinfo("Incompleto","INcompelto")
    else:
        mbo.showinfo("COmpleto","Nombre:"+nombre.get()+"\nApellido Paterno: "+apellidop.get()+"\nApellido Materno: "+apellidom.get()+"\nDireccion: "+direccion.get()+"\nColonia: "+colonia.get()+"\nCiudad: "+ciudad.get()+"\nMunicipio:"+municipio.get())

def impex():
    if(objetivo.get()!="" or (opcion_4.get()==1 and opcion_4.get()==2 and opcion_4.get()==3 and opcion_4.get()==4 and opcion_4.get()==5)):
        a=""
        if(opcion_1.get()==1):
            a+=" Leer"
        if(opcion_2.get()==1):
            a+=" Futbol"
        if(opcion_3.get()==1):
            a+=" Correr"
        if(opcion_5.get()==1):
            a+=" Programar"
        if(opcion_6.get()==1):
            a+=" Videojuegos"
        b=""
        if(opcion_4.get()==1):
            b="Soltero"
        if(opcion_4.get()==2):
            b="Viudo"
        if(opcion_4.get()==3):
            b="Casado"
        if(opcion_4.get()==4):
            b="Entre rel."
        if(opcion_4.get()==5):
            b="Alone"
        mbo.showinfo("Datos","Te gusta:\n"+a+"\nEstas: "+b+"\nTu objetivo es:\n"+objetivo.get())
    else:
        mbo.showinfo("Incompleto","INcompelto")

def imprim():
    impex()
    perex()

def salir():
    ventana.quit()
    ventana.destroy()
    exit()

def ayuda():
    mbo.showinfo("Acerca de","Johan Ramirez\nVed\n2020")

ventana = tk.Tk()
ventana.title("Practica")

barra_menu=Menu(ventana)
ventana.config(menu=barra_menu)
menu_archivo=Menu(barra_menu)
menu_archivo.add_command(label="Imprimir", command=imprim)
menu_archivo.add_command(label="Salir",command=salir)
barra_menu.add_cascade(label="Sistema",menu=menu_archivo)
menu_ayuda=Menu(barra_menu, tearoff=0)
menu_ayuda.add_command(label="Acerca de", command = ayuda)
barra_menu.add_cascade(label="Ayuda", menu=menu_ayuda)

tabControl=ttk.Notebook(ventana)
tab1=ttk.Frame(tabControl)
tabControl.add(tab1, text='Datos Personales')
tabControl.pack(expand=1, fill="both")  

ttk.Label(tab1, text="Nombre:").grid(column=0,row=2)
nombre=tk.StringVar()
nombreCapturado=ttk.Entry(tab1, width=12, textvariable=nombre)
nombreCapturado.grid(column=1,row=2)
ttk.Label(tab1, text="Apellido Paterno:").grid(column=0,row=3)
apellidop=tk.StringVar()
apellidopCapturado=ttk.Entry(tab1, width=12, textvariable=apellidop)
apellidopCapturado.grid(column=1,row=3)
ttk.Label(tab1, text="Apellido Materno:").grid(column=0,row=4)
apellidom=tk.StringVar()
apellidomCapturado=ttk.Entry(tab1, width=12, textvariable=apellidom)
apellidomCapturado.grid(column=1,row=4)
ttk.Label(tab1, text="Direccion:").grid(column=0,row=5)
direccion=tk.StringVar()
direccionCapturado=ttk.Entry(tab1, width=12, textvariable=direccion)
direccionCapturado.grid(column=1,row=5)
ttk.Label(tab1, text="Colonia:").grid(column=0,row=6)
colonia=tk.StringVar()
coloniaSeleccionado=ttk.Combobox(tab1, width=12,textvariable=colonia)
coloniaSeleccionado['values']=("Hacienda del Sol","Villa Universidad","Colonia F")
coloniaSeleccionado.grid(column=1,row=6)
coloniaSeleccionado.current(0)
ttk.Label(tab1, text="Ciudad:").grid(column=0,row=7)
ciudad=tk.StringVar()
ciudadSeleccionado=ttk.Combobox(tab1, width=12,textvariable=ciudad)
ciudadSeleccionado['values']=("Morelia","Quiorga","Monterrey")
ciudadSeleccionado.grid(column=1,row=7)
ciudadSeleccionado.current(0)
ttk.Label(tab1, text="Municipio:").grid(column=0,row=8)
municipio=tk.StringVar()
municipioSeleccionado=ttk.Combobox(tab1, width=12,textvariable=municipio)
municipioSeleccionado['values']=("Morelia","Quiroga","Monterrey")
municipioSeleccionado.grid(column=1,row=8)
municipioSeleccionado.current(0)
pkmn=ttk.Button(tab1, text="Imprimir",command=perex)
pkmn.grid(column=1, row=9)

tab2=ttk.Frame(tabControl)
tabControl.add(tab2, text='Datos Extras')

ttk.Label(tab2, text="Pasatiempos").grid(column=0,row=9)
opcion_1=tk.IntVar()
casilla_1=tk.Checkbutton(tab2,text="Leer",variable=opcion_1)
casilla_1.deselect()
casilla_1.grid(column=0,row=10)
opcion_2=tk.IntVar()
casilla_2=tk.Checkbutton(tab2,text="Futbol",variable=opcion_2)
casilla_2.deselect()
casilla_2.grid(column=1,row=10)
opcion_3=tk.IntVar()
casilla_3=tk.Checkbutton(tab2,text="Correr",variable=opcion_3)
casilla_3.deselect()
casilla_3.grid(column=2,row=10)
opcion_6=tk.IntVar()
casilla_6=tk.Checkbutton(tab2,text="Videojuegos",variable=opcion_6)
casilla_6.deselect()
casilla_6.grid(column=3,row=10)
opcion_5=tk.IntVar()
casilla_5=tk.Checkbutton(tab2,text="Programar",variable=opcion_5)
casilla_5.deselect()
casilla_5.grid(column=4,row=10)
ttk.Label(tab2, text="Estado").grid(column=0,row=11)
opcion_4=tk.IntVar()
radio1=tk.Radiobutton(tab2, text="Soltero", variable=opcion_4,value=1)
radio1.grid(column=0,row=12)
radio2=tk.Radiobutton(tab2, text="Viudo", variable=opcion_4,value=2)
radio2.grid(column=1,row=12)
radio3=tk.Radiobutton(tab2, text="Casado", variable=opcion_4,value=3)
radio3.grid(column=2,row=12)
radio4=tk.Radiobutton(tab2, text="Entre rel.", variable=opcion_4,value=4)
radio4.grid(column=3,row=12)
radio5=tk.Radiobutton(tab2, text="Alone", variable=opcion_4,value=5)
radio5.grid(column=4,row=12)
ttk.Label(tab2, text="Objetivo de la vida").grid(column=0,row=13)
objetivo=tk.StringVar()
objetivoc=ttk.Entry(tab2, width=12, textvariable=objetivo)
objetivoc.grid(column=0,row=14)
pkmn2=ttk.Button(tab2, text="Imprimir",command=impex)
pkmn2.grid(column=1, row=14)

ventana.mainloop()
