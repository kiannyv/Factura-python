from tkinter import *
import random
import os
import sys
from tkinter import messagebox
raiz = Tk()
class Menu_App:
    def __init__(terry, raiz):
        terry.raiz = raiz
        terry.raiz.geometry("1350x1000")
        terry.raiz.configure(bg="#eeebe7")
        terry.raiz.title("GTA_12_")
        title = Label(terry.raiz, text="New Contact", bd=10, font=(
            "Arial Black", 40), bg="blue violet", fg="#eeebe7").pack(fill=X)

        terry.nombre = StringVar()
        terry.apellidos = StringVar ()
        terry.empresa = StringVar()
        terry.puesto = StringVar()
        terry.direccion = StringVar()
        terry.direccion2 = StringVar ()
        terry.provincia = StringVar()
        terry.canton = StringVar()
        terry.CodPostal = StringVar()
        terry.telefo = IntVar()
        terry.telefo2 = IntVar ()
        terry.celu = StringVar()
        terry.email = StringVar()
        terry.comentarios = StringVar()
        terry.email2 =StringVar()
        terry.Año =StringVar()
        
        # ==========================================Informacion del Contacto=================================================
        varios1 = LabelFrame(terry.raiz, text="Información del Contacto", font=("Arial Black", 16), bg="DeepSkyBlue2", fg="Black",relief=RIDGE, bd=10)
        varios1.place(x=5, y=110, height=550, width=440)
        nombre = Label(varios1, text="Nombre:", font=("Lorem ipsum", 16), bg="DeepSkyBlue2", fg="Black").grid(row=0, column=0, pady=11)
        nombre_entry = Entry(varios1, borderwidth=2, width=35, textvariable=terry.nombre,bg="SlateBlue1").grid(row=0, column=1, padx=10)
        grado = Label(varios1, text="Apellidos:", font=("Lorem ipsum", 16), bg="DeepSkyBlue2", fg="Black").grid(row=1, column=0, pady=11)
        grado_entry = Entry(varios1, borderwidth=2, width=35, textvariable=terry.apellidos,bg="SlateBlue1").grid(row=1, column=1, padx=10)
        empresa = Label(varios1, text="Empresa:", font=("Lorem ipsum", 16), bg="DeepSkyBlue2", fg="Black").grid(row=2, column=0, pady=11)
        empresa_entry = Entry(varios1, borderwidth=2, width=35, textvariable=terry.empresa,bg="SlateBlue1").grid(row=2, column=1, padx=10)
        puesto = Label(varios1, text="Puesto:", font=("Lorem ipsum", 16), bg="DeepSkyBlue2", fg="Black").grid(row=3, column=0, pady=11)
        puesto_entry = Entry(varios1, borderwidth=2, width=35, textvariable=terry.puesto,bg="SlateBlue1").grid(row=3, column=1, padx=10)
        direccion = Label(varios1, text="Dirección:", font=("Lorem ipsum", 16), bg="DeepSkyBlue2", fg="Black").grid(row=4, column=0, pady=11)
        direccion_entry = Entry(varios1, borderwidth=2, width=35, textvariable=terry.direccion,bg="SlateBlue1").grid(row=4, column=1, padx=10)
        direccion2 = Label(varios1, text="Dirección2:", font=("Lorem ipsum", 16), bg="DeepSkyBlue2", fg="Black").grid(row=5, column=0, pady=11)
        direccion2_entry = Entry(varios1, borderwidth=2, width=35, textvariable=terry.direccion2,bg="SlateBlue1").grid(row=5, column=1, padx=10)
        provincia = Label(varios1, text="Provincia:", font=("Lorem ipsum", 16), bg="DeepSkyBlue2", fg="Black").grid(row=6, column=0, pady=11)
        provincia_entry = Entry(varios1, borderwidth=2, width=35, textvariable=terry.provincia,bg="SlateBlue1").grid(row=6, column=1, padx=10)
        canton = Label(varios1, text="Cantón:", font=("Lorem ipsum", 16), bg="DeepSkyBlue2", fg="Black").grid(row=7, column=0, pady=11)
        canton_entry = Entry(varios1, borderwidth=2, width=35, textvariable=terry.canton,bg="SlateBlue1").grid(row=7, column=1, padx=10)
        codPostal= Label(varios1, text="Codigo Postal:", font=("Lorem ipsum", 16), bg="DeepSkyBlue2", fg="Black").grid(row=8, column=0, pady=11)
        codPostal_entry = Entry(varios1, borderwidth=2, width=35, textvariable=terry.CodPostal,bg="SlateBlue1").grid(row=8, column=1, padx=10)


       # ================================================Telefonos y emails========================================================
        varios2 = LabelFrame(terry.raiz, text="Teléfonos y emails:", font=("Arial Black", 16),bg="DeepSkyBlue2", fg="Black", relief=RIDGE, bd=10)
        varios2.place(x=470, y=110, height=370, width=440)
        direccion = Label(varios2, text="Teléfono:", font=("Lorem ipsum", 16), bg="DeepSkyBlue2", fg="Black").grid(row=0, column=0, pady=11)
        direccion_entry = Entry(varios2, borderwidth=2, width=35, textvariable=terry.telefo,bg="SlateBlue1").grid(row=0, column=1, padx=10)
        direccion = Label(varios2, text="Teléfono2:", font=("Lorem ipsum", 16), bg="DeepSkyBlue2", fg="Black").grid(row=1, column=0, pady=11)
        direccion_entry = Entry(varios2, borderwidth=2, width=35, textvariable=terry.telefo2,bg="SlateBlue1").grid(row=1, column=1, padx=10)
        provincia = Label(varios2, text="Celular:", font=("Lorem ipsum", 16), bg="DeepSkyBlue2", fg="Black").grid(row=2, column=0, pady=11)
        provincia_entry = Entry(varios2, borderwidth=2, width=35, textvariable=terry.celu,bg="SlateBlue1").grid(row=2, column=1, padx=10)
        canton = Label(varios2, text="Email:", font=("Lorem ipsum", 16), bg="DeepSkyBlue2", fg="Black").grid(row=3, column=0, pady=11)
        canton_entry = Entry(varios2, borderwidth=2, width=35, textvariable=terry.email,bg="SlateBlue1").grid(row=3, column=1, padx=10)
        canton = Label(varios2, text="Email2:", font=("Lorem ipsum", 16), bg="DeepSkyBlue2", fg="Black").grid(row=4, column=0, pady=11)
        canton_entry = Entry(varios2, borderwidth=2, width=35, textvariable=terry.email2,bg="SlateBlue1").grid(row=4, column=1, padx=10)

        
        # ==============================================Resumen del contacto=========================================================
        resumen = Frame(terry.raiz, bd=10, bg="SlateBlue1",relief=RIDGE)
        resumen.place(x=940, y=110, width=400, height=550)
        resumen_title = Label(resumen, text="Resumen de Contacto", font=("Arial Black", 18), bd=10, bg="DeepSkyBlue2", fg="Black").pack(fill=X)
        scrol_y = Scrollbar(resumen, orient=VERTICAL)
        terry.txtarea = Text(resumen, yscrollcommand=scrol_y.set)
        scrol_y.pack(side=RIGHT, fill=Y)
        scrol_y.config(command=terry.txtarea.yview)
        terry.txtarea.pack(fill=BOTH, expand=1)
        

       # =================================================Comentarios==================================================================
        comentarios = LabelFrame (terry.raiz, text="Comentarios", font=("Arial Black", 16), bd=10, bg="DeepSkyBlue2", fg="Black")
        comentarios.place(x=470, y=490, width=450, height=170)
        comentarios_entry = Entry(comentarios,borderwidth=45, width=35, textvariable=terry.comentarios,bg="SlateBlue1", relief=FLAT).grid(row=0, column=1, padx=10)
        #Registrar
        boton_registrar = Button(comentarios, text="Registrar", font=("Time New Roman", 14), pady=10,
                              bg="#c0b6c1", fg="#705e6c", command=show_data(terry)).grid(row=0, column=7, padx=10)


def show_data(terry):
    terry.nu = terry.nombre.get()
    terry.no = terry.apellidos.get()
    terry.la = terry.empresa.get()
    terry.ore = terry.puesto.get ()
    terry.mu = terry.direccion.get()
    terry.mo = terry.direccion2.get()
    terry.si = terry.provincia.get()
    terry.at = terry.canton.get()
    terry.po = terry.CodPostal.get ()
    terry.oi = terry.telefo.get()
    terry.ma = terry.telefo2.get()
    terry.ri = terry.celu.get()
    terry.su = terry.email.get()
    terry.sa = terry.email2.get()
    terry.lo = terry.Año.get()
    
    if terry.nombre.get() !=0:
        terry.txtarea.insert(END, f"Nombre: ***\t\t{terry.nombre.get()}\t{terry.nu}\n")
    if terry.apellidos.get()!=0:
        terry.txtarea.insert(END, f"Apellidos: ***\t\t{terry.apellidos.get()}\t{terry.no}\n")
    if terry.empresa.get()!=0:
        terry.txtarea.insert(END, f"Empresa: ***\t\t{terry.empresa.get()}\t{terry.la}\n") 
    if terry.puesto.get()!=0:
        terry.txtarea.insert(END, f"Puesto: ***\t\t{terry.puesto.get()}\t{terry.ore}\n\n")
    if terry.direccion.get()!=0:
        terry.txtarea.insert(END, f"Dirección: ***\t\t{terry.direccion.get()}\t{terry.mu}\n")
    if terry.direccion2.get() !=0:
        terry.txtarea.insert(END, f"Dirección2: ***\t\t{terry.direccion2.get()}\t{terry.mo}\n")
    if terry.provincia.get()!=0:
        terry.txtarea.insert(END, f"Provincia: ***\t\t{terry.provincia.get()}\t{terry.si}\n")
    if terry.canton.get()!=0:
        terry.txtarea.insert(END, f"Cantón: ***\t\t{terry.canton.get()}\t{terry.at}\n")
    if terry.CodPostal.get()!=0:
        terry.txtarea.insert(END, f"Codigo Postal: ***\t\t{terry.CodPostal.get()}\t{terry.po}\n\n\n")
    if terry.telefo.get()!=0:
        terry.txtarea.insert(END, f"Teléfono: ***\t\t{terry.telefo.get()}\t{terry.oi}\n")
    if terry.telefo2.get()!=0:
        terry.txtarea.insert(END, f"Teléfono2: ***\t\t{terry.telefo2.get()}\t{terry.ma}\n")
    if terry.celu.get()!=0:
        terry.txtarea.insert(END, f"Celular:  ***\t\t{terry.celu.get()}\t{terry.ri}\n") 
    if terry.email.get()!=0:
        terry.txtarea.insert(END, f"Email: ***\t\t{terry.email.get()}\t{terry.su}\n")
    if terry.email2.get()!=0:
        terry.txtarea.insert(END, f"Email2: ***\t\t{terry.email2.get()}\t{terry.sa}\n\n\n")
    if terry.Año.get()!=0:
        terry.txtarea.insert(END, f"\n\n\n\n\n\n\n\n\n2021\n\t\t{terry.Año.get()}\t{terry.lo}\n")
        
obj = Menu_App(raiz)
raiz.mainloop()
