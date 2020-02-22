#!/usr/bin/env python3
# -*- coding: utf-8 -*-

from tkinter import *
from tkinter import ttk
import tkinter as tk
import webbrowser
from subprocess import call
import subprocess
import os
import subprocess as sub
import numpy as np
import cv2

from tkinter import filedialog
from tkinter import messagebox

def caja_offshell():
    
    #Ventana Aviso Primera Instalación.

    root = Tk()
    root.title("··· OffShell System Society ···")
    root.geometry("430x170+397+300")
    root.resizable(width=False, height=False)
    root.config(bg='black')

    root.tk.call('wm', 'iconphoto', root._w, tk.PhotoImage(file='primate.gif'))

    label=Label(root, text="La guía está en desarrollo\nDisponible en la próxima actualización", 
        font=("URW Chancery L", 17), foreground="Red", background="black").place(x=67, y=20)

    #
    
    boton_ejecutar_avs=Frame(root)
    boton_ejecutar_avs.pack(fill=BOTH, expand=YES)
    boton_ejecutar_avs.place(x=100, y=90)
    Button(boton_ejecutar_avs, highlightbackground="black", command=lambda:[root.destroy()], 
        width=23, height=1, text="Continuar", foreground='green', activeforeground='purple', 
        cursor="fleur", justify="center", bd=0,  relief="raised", overrelief="sunken", 
        background="black", activebackground="black", font=("URW Chancery L", 15)).pack()

    root.mainloop()

    pass


def offshell_desplegable():
   
    botonBienvenido=Frame(root, width=1024, height=1024)
    botonBienvenido.pack(fill=BOTH, expand=YES)
    botonBienvenido.place(x=0, y=0)
    Button(botonBienvenido, image=imagen_fondo1, cursor="heart", justify="center", bd=0, 
        relief="raised", background="Black", activebackground='black', font=("URW Chancery L", 15)).pack()


    #BOTON MENÚ DESPLEGABLE
    boton_offshell_menu=Frame(root)
    boton_offshell_menu.pack(fill=BOTH, expand=YES)
    boton_offshell_menu.place(x=41, y=200)
    Button(boton_offshell_menu, highlightbackground="black", command=lambda:[], 
        text="Off - Shell en física significa\n'partícula sin movimiento'.\n \nOffShell System es un nombre en clave.\nRepresenta un sistema con intérprete\nde órdenes bajo estado de movimiento nulo.\n \nAlgo sin movimiento, puede contener\nmiles de funciones y valores atribuídos a su estado.", 
        foreground='orange', activeforeground='white', cursor="heart", 
        justify="center", bd=0, relief="groove", background="black", activebackground="black", 
        font=("URW Chancery L", 14)).pack()


    boton_offshell_menu=Frame(root)
    boton_offshell_menu.pack(fill=BOTH, expand=YES)
    boton_offshell_menu.place(x=725, y=150)
    Button(boton_offshell_menu, highlightbackground="black", command=lambda:[], 
        text="Suelo usar el apodo ShellDredd\n \nDesarrollo software comunitario para\nsistemas y usuari@s éticamente afínes.\n \nSi quieres conocer mis planes y proyectos,\nno dudes en conectar conmigo.", 
        foreground='orange', activeforeground='white', cursor="heart", 
        justify="center", bd=0, relief="groove", background="black", activebackground="black", 
        font=("URW Chancery L", 14)).pack()



    botonBienvenido6=Frame(root)
    botonBienvenido6.pack(fill=BOTH, expand=YES)
    botonBienvenido6.place(x=470, y=400)
    Button(botonBienvenido6, highlightbackground="black", 
        command=lambda:[webbrowser.open_new_tab("https://www.linkedin.com/in/alexandre-varela-offshell/")], 
        width=17, height=1, text="Linkedin", foreground='red', activeforeground='orange', 
        cursor="fleur", justify="center", bd=0,  relief="raised", overrelief="sunken", 
        background="black", activebackground="black", font=("URW Chancery L", 13)).pack()

    botonBienvenido5=Frame(root)
    botonBienvenido5.pack(fill=BOTH, expand=NO)
    botonBienvenido5.place(x=470, y=350)
    Button(botonBienvenido5, highlightbackground="black", 
        command=lambda:[webbrowser.open_new_tab("https://discord.gg/ShKjFfe")], 
        width=17, height=1, text="Discord", foreground='red', activeforeground='orange', cursor="fleur", 
        justify="center", bd=0,  relief="raised", overrelief="sunken", background="black", 
        activebackground="black", font=("URW Chancery L", 13)).pack()

    botonBienvenido4=Frame(root)
    botonBienvenido4.pack(fill=BOTH, expand=YES)
    botonBienvenido4.place(x=470, y=250)
    Button(botonBienvenido4, highlightbackground="black", command=lambda:[webbrowser.open_new_tab("https://www.youtube.com/channel/UC3qdw1OjdgmRHPY3-KiyQuA")], width=17, 
        height=1, text="Canal Youtube", foreground='red', activeforeground='orange', cursor="fleur", 
        justify="center", bd=0,  relief="raised", overrelief="sunken", background="black", 
        activebackground="black", font=("URW Chancery L", 13)).pack()

    botonBienvenido3=Frame(root)
    botonBienvenido3.pack(fill=BOTH, expand=YES)
    botonBienvenido3.place(x=470, y=300)
    Button(botonBienvenido3, highlightbackground="black", command=lambda:[webbrowser.open_new_tab("https://github.com/OffShellSystem")], width=17, height=1, 
        text="Git Hub", foreground='red', activeforeground='orange', cursor="fleur", justify="center", 
        bd=0,  relief="raised", overrelief="sunken", background="black", activebackground="black", 
        font=("URW Chancery L", 13)).pack()

    botonBienvenido2=Frame(root)
    botonBienvenido2.pack(fill=BOTH, expand=YES)
    botonBienvenido2.place(x=470, y=200)
    Button(botonBienvenido2, highlightbackground="black", 
        command=lambda:[webbrowser.open_new_tab("www.shelldredd.tk")], 
        width=17, height=1, text="ShellDredd Web", foreground='red', activeforeground='orange', 
        cursor="fleur", justify="center", bd=0,  relief="raised", overrelief="sunken", 
        background="black", activebackground="black", font=("URW Chancery L", 13)).pack()


    botonBienvenido1=Frame(root)
    botonBienvenido1.pack(fill=BOTH, expand=YES)
    botonBienvenido1.place(x=470, y=150)
    Button(botonBienvenido1, highlightbackground="black", 
        command=lambda:[webbrowser.open_new_tab("https://www.offshellsystem.tk/p/offshell-system.html")], 
        width=17, height=1, text="Plataforma Web", foreground='red', activeforeground='orange', cursor="fleur", 
        justify="center", bd=0,  relief="raised", overrelief="sunken", background="black", 
        activebackground="black", font=("URW Chancery L", 13)).pack()


    #Imagen logo OffShell System
    boton_menu2=Frame(root)
    boton_menu2.pack(fill=BOTH, expand=YES)
    boton_menu2.place(x=170, y=100)
    Button(boton_menu2, highlightbackground="black", image=primate_logo, foreground='red', activeforeground='black',
         cursor="fleur", justify="center", bd=0,  relief="raised", background="black", activebackground="black",
          font=("URW Chancery L", 16)).pack()

    boton_menu2=Frame(root)
    boton_menu2.pack(fill=BOTH, expand=YES)
    boton_menu2.place(x=827, y=355)
    Button(boton_menu2, highlightbackground="black", image=fun_logo, foreground='red', activeforeground='black',
         cursor="fleur", justify="center", bd=0,  relief="raised", background="black", activebackground="black",
          font=("URW Chancery L", 16)).pack()


    #Menu Volver Logo.
    boton_img_ligeros=Frame(root)
    boton_img_ligeros.place(x=514, y=530)
    Button(boton_img_ligeros, highlightbackground="black", command=lambda:[menu_principal()],
        image=inicio_logo, cursor='fleur', justify='center', bd=0, background="black", 
        activebackground="black").pack()



    pass

def ampliar_texto_soft():
    boton_stallman=Frame(root)
    boton_stallman.pack(fill=BOTH, expand=YES)
    boton_stallman.place(x=60, y=130)
    Button(boton_stallman, highlightbackground="black", command=lambda:[soflibre_desp()], 
        text="La definición de software libre estipula los criterios que\nse tienen que cumplir para que un programa sea considerado libre.\nDe vez en cuando modificamos esta definición para clarificarla\no para resolver problemas sobre cuestiones delicadas.\n«Software libre» es el software que respeta la libertad\nde los usuarios y la comunidad.\nA grandes rasgos, significa que los usuarios tienen la libertad de\nejecutar, copiar, distribuir, estudiar, modificar y mejorar el software.\nEs decir, el «software libre» es una cuestión de libertad, no de precio.\nPara entender el concepto, piense en «libre» como en «libre expresión»,\nno como en «barra libre».\nEn inglés, a veces en lugar de «free software» decimos «libre software»,\nempleando ese adjetivo francés o español, derivado de «libertad»,\npara mostrar que no queremos decir que el software es gratuito.", 
        foreground='orange', activeforeground='white', cursor="heart", 
        justify="left", bd=2, relief="groove", background="black", activebackground="black", 
        font=("URW Chancery L", 18)).pack()

def soflibre_desp():
   
    botonBienvenido=Frame(root, width=1024, height=1024)
    botonBienvenido.pack(fill=BOTH, expand=YES)
    botonBienvenido.place(x=0, y=0)
    Button(botonBienvenido, image=imagen_fondo1, cursor="heart", justify="center", bd=0, 
        relief="raised", background="Black", activebackground='black', 
        font=("URW Chancery L", 15)).pack()

    boton_ver_texto=Frame(root)
    boton_ver_texto.pack(fill=BOTH, expand=YES)
    boton_ver_texto.place(x=30, y=100)
    Button(boton_ver_texto, highlightbackground="black", command=lambda:[ampliar_texto_soft()], 
        text="Ampliar texto", foreground='red', activeforeground='orange', cursor="heart", 
        justify="center", bd=0, relief="groove", background="black", activebackground="black", 
        font=("URW Chancery L", 14)).pack()

    boton_stallman=Frame(root)
    boton_stallman.pack(fill=BOTH, expand=YES)
    boton_stallman.place(x=10, y=130)
    Button(boton_stallman, highlightbackground="black", command=lambda:[ampliar_texto_soft()], 
        text="La definición de software libre estipula los criterios que\nse tienen que cumplir para que un programa sea considerado libre.\nDe vez en cuando modificamos esta definición para clarificarla\no para resolver problemas sobre cuestiones delicadas.\n«Software libre» es el software que respeta la libertad\nde los usuarios y la comunidad.\nA grandes rasgos, significa que los usuarios tienen la libertad de\nejecutar, copiar, distribuir, estudiar, modificar y mejorar el software.\nEs decir, el «software libre» es una cuestión de libertad, no de precio.\nPara entender el concepto, piense en «libre» como en «libre expresión»,\nno como en «barra libre».\nEn inglés, a veces en lugar de «free software» decimos «libre software»,\nempleando ese adjetivo francés o español, derivado de «libertad»,\npara mostrar que no queremos decir que el software es gratuito.", 
        foreground='orange', activeforeground='gray', cursor="heart", 
        justify="left", bd=0, relief="groove", background="black", activebackground="black", 
        font=("URW Chancery L", 12)).pack()

    boton_img_mapa_conceptual=Frame(root)
    boton_img_mapa_conceptual.place(x=20, y=450)
    Button(boton_img_mapa_conceptual, highlightbackground="black", command=lambda:[mapa_ampliar()],
        image=mapa_libre, cursor='fleur', justify='center', bd=0, background="black", 
        activebackground="black").pack()

    boton_ver_mapa=Frame(root)
    boton_ver_mapa.pack(fill=BOTH, expand=YES)
    boton_ver_mapa.place(x=30, y=593)
    Button(boton_ver_mapa, highlightbackground="black", command=lambda:[mapa_ampliar()], 
        text="Ampliar mapa conceptual", foreground='red', activeforeground='orange', cursor="heart", 
        justify="center", bd=0, relief="groove", background="black", activebackground="black", 
        font=("URW Chancery L", 14)).pack()



    #BOTON MENÚ DESPLEGABLE
    boton_offshell_menu=Frame(root)
    boton_offshell_menu.pack(fill=BOTH, expand=YES)
    boton_offshell_menu.place(x=780, y=100)
    Button(boton_offshell_menu, highlightbackground="black", command=lambda:[], width=18, height=1, 
        text="Amigos del Movimiento", foreground='orange', activeforeground='orange', cursor="heart", 
        justify="center", bd=0, relief="groove", background="black", activebackground="black", 
        font=("URW Chancery L", 16)).pack()


    #BOTONES IZQUIERDA
    boton_offshell_desplegable_izq=Frame(root)
    boton_offshell_desplegable_izq.pack(fill=BOTH, expand=YES)
    boton_offshell_desplegable_izq.place(x=730, y=180)
    Button(boton_offshell_desplegable_izq, highlightbackground="black", 
        command=lambda:[webbrowser.open_new_tab("https://www.gnu.org/")], width=15, height=1, 
        text="Fundación GNU", foreground='red', activeforeground='orange', cursor="heart", 
        justify="center", bd=0, relief="groove", background="black", activebackground="black", 
        font=("URW Chancery L", 14)).pack()

    boton_offshell_desplegable_izq2=Frame(root)
    boton_offshell_desplegable_izq2.pack(fill=BOTH, expand=YES)
    boton_offshell_desplegable_izq2.place(x=730, y=240)
    Button(boton_offshell_desplegable_izq2, highlightbackground="black", 
        command=lambda:[webbrowser.open_new_tab("http://aomedia.org/")], 
        width=15, height=1, text="Aomedia", foreground='red', 
        activeforeground='orange', cursor="heart", justify="center", bd=0, relief="groove", 
        background="black", activebackground="black", font=("URW Chancery L", 14)).pack()

    boton_offshell_desplegable_izq3=Frame(root)
    boton_offshell_desplegable_izq3.pack(fill=BOTH, expand=YES)
    boton_offshell_desplegable_izq3.place(x=730, y=300)
    Button(boton_offshell_desplegable_izq3, highlightbackground="black", 
        command=lambda:[webbrowser.open_new_tab("https://www.bilib.es/")], width=15, height=1, 
        text="Bilib", foreground='red', activeforeground='orange', cursor="heart", 
        justify="center", bd=0, relief="groove", background="black", activebackground="black", 
        font=("URW Chancery L", 14)).pack()

    boton_offshell_desplegable_izq4=Frame(root)
    boton_offshell_desplegable_izq4.pack(fill=BOTH, expand=YES)
    boton_offshell_desplegable_izq4.place(x=730, y=360)
    Button(boton_offshell_desplegable_izq4, highlightbackground="black", 
        command=lambda:[webbrowser.open_new_tab("https://web.archive.org/web/20070319232139/http://www.doss.dk/joom/")], width=15, height=1, 
        text="Doss", foreground='red', activeforeground='orange', cursor="heart", 
        justify="center", bd=0, relief="groove", background="black", activebackground="black", 
        font=("URW Chancery L", 14)).pack()

    #BOTONES DERECHA
    boton_offshell_desplegable_der=Frame(root)
    boton_offshell_desplegable_der.pack(fill=BOTH, expand=YES)
    boton_offshell_desplegable_der.place(x=880, y=180)
    Button(boton_offshell_desplegable_der, highlightbackground="black", 
        command=lambda:[webbrowser.open_new_tab("https://www.kernel.org/")], width=15, height=1, 
        text="Linux Kernel", foreground='red', activeforeground='orange', cursor="heart", 
        justify="center", bd=0, relief="groove", background="black", activebackground="black", 
        font=("URW Chancery L", 14)).pack()

    boton_offshell_desplegable_der2=Frame(root)
    boton_offshell_desplegable_der2.pack(fill=BOTH, expand=YES)
    boton_offshell_desplegable_der2.place(x=880, y=240)
    Button(boton_offshell_desplegable_der2, highlightbackground="black", 
        command=lambda:[webbrowser.open_new_tab("https://lapipaplena.wordpress.com/")], 
        width=15, height=1, text="La Pipa Plena", foreground='red', activeforeground='orange', 
        cursor="heart", justify="center", bd=0, relief="groove", background="black", 
        activebackground="black", font=("URW Chancery L", 14)).pack()

    boton_offshell_desplegable_der2=Frame(root)
    boton_offshell_desplegable_der2.pack(fill=BOTH, expand=YES)
    boton_offshell_desplegable_der2.place(x=880, y=300)
    Button(boton_offshell_desplegable_der2, highlightbackground="black", 
        command=lambda:[webbrowser.open_new_tab("https://comunes.org/#")], 
        width=15, height=1, text="Comunes", foreground='red', activeforeground='orange', 
        cursor="heart", justify="center", bd=0, relief="groove", background="black", 
        activebackground="black", font=("URW Chancery L", 14)).pack()

    boton_offshell_desplegable_der3=Frame(root)
    boton_offshell_desplegable_der3.pack(fill=BOTH, expand=YES)
    boton_offshell_desplegable_der3.place(x=880, y=360)
    Button(boton_offshell_desplegable_der3, highlightbackground="black", 
        command=lambda:[webbrowser.open_new_tab("https://framasoft.org/")], 
        width=15, height=1, text="Framasoft", foreground='red', activeforeground='orange', 
        cursor="heart", justify="center", bd=0, relief="groove", background="black", 
        activebackground="black", font=("URW Chancery L", 14)).pack()

    #CERRAR DESPLEGABLE
    boton_cerrar_distros=Frame(root)
    boton_cerrar_distros.pack(fill=BOTH, expand=YES)
    boton_cerrar_distros.place(x=470, y=200)
    Button(boton_cerrar_distros, highlightbackground="black", command=lambda:[menu_principal()], 
        width=15, height=1, text="Menú Principal", foreground='red', activeforeground='orange', 
        cursor="fleur", justify="center", bd=0,  relief="raised", overrelief="sunken", 
        background="black", activebackground="black", font=("URW Chancery L", 15)).pack()


    pass

def mapa_ampliar():
    
    #Mapa Conceptual Ampliado.
    botonBienvenido=Frame(root, width=1024, height=1024)
    botonBienvenido.pack(fill=BOTH, expand=YES)
    botonBienvenido.place(x=220, y=0)
    Button(botonBienvenido, image=mapa_ampliado, command=lambda:[soflibre_desp()], 
        cursor="heart", justify="center", bd=0, relief="raised", background="Black", 
        activebackground='black', font=("URW Chancery L", 15)).pack()



def codigo_open():
   
    botonBienvenido=Frame(root, width=1024, height=1024)
    botonBienvenido.pack(fill=BOTH, expand=YES)
    botonBienvenido.place(x=0, y=0)
    Button(botonBienvenido, image=imagen_fondo1, cursor="heart", justify="center", bd=0, 
        relief="raised", background="Black", activebackground='black', 
        font=("URW Chancery L", 15)).pack()

    boton_ver_texto=Frame(root)
    boton_ver_texto.pack(fill=BOTH, expand=YES)
    boton_ver_texto.place(x=30, y=70)
    Button(boton_ver_texto, highlightbackground="black", command=lambda:[ampliar_texto_open()], 
        text="Ampliar texto", foreground='red', activeforeground='orange', cursor="heart", 
        justify="center", bd=0, relief="groove", background="black", activebackground="black", 
        font=("URW Chancery L", 14)).pack()

    boton_stallman=Frame(root)
    boton_stallman.pack(fill=BOTH, expand=YES)
    boton_stallman.place(x=10, y=100)
    Button(boton_stallman, highlightbackground="black", command=lambda:[ampliar_texto_open()], 
        text="El código abierto es un modelo de desarrollo de software basado en la\ncolaboración abierta. Se enfoca más en los beneficios prácticos\n(acceso al código fuente) que en cuestiones éticas o de libertad que\ntanto se destacan en el software libre. Para muchos el término «libre»\nhace referencia al hecho de adquirir un software de manera gratuita.\nLa idea del código abierto se centra en la premisa de que al compartir\nel código, el programa resultante tiende a ser de calidad superior\nal software propietario, es una visión técnica. El código abierto ofrece:\n1·Acceso al código fuente:\n  Para modificarlo, corregirlo o añadir más prestaciones.\n2·Gratuidad:\n  El software puede obtenerse libremente.\n3·La posibilidad de evitar monopolios de software propietario:\n  Para no depender de un único fabricante de software.\n4·Un modelo de avance:\n  Por lo cual la información no se oculta.", 
        foreground='orange', activeforeground='gray', cursor="heart", 
        justify="left", bd=0, relief="groove", background="black", activebackground="black", 
        font=("URW Chancery L", 12)).pack()

    boton_img_mapa_conceptual=Frame(root)
    boton_img_mapa_conceptual.pack(fill=BOTH, expand=YES)
    boton_img_mapa_conceptual.place(x=20, y=450)
    Button(boton_img_mapa_conceptual, highlightbackground="black", command=lambda:[mapa_ampliar2()],
        image=codigo_abierto, cursor='fleur', justify='center', bd=0, background="black", 
        activebackground="black").pack()

    boton_ver_mapa=Frame(root)
    boton_ver_mapa.pack(fill=BOTH, expand=YES)
    boton_ver_mapa.place(x=30, y=593)
    Button(boton_ver_mapa, highlightbackground="black", command=lambda:[mapa_ampliar2()], 
        text="Ampliar mapa conceptual", foreground='red', activeforeground='orange', cursor="heart", 
        justify="center", bd=0, relief="groove", background="black", activebackground="black", 
        font=("URW Chancery L", 14)).pack()



    #BOTON MENÚ DESPLEGABLE
    boton_offshell_menu=Frame(root)
    boton_offshell_menu.pack(fill=BOTH, expand=YES)
    boton_offshell_menu.place(x=780, y=100)
    Button(boton_offshell_menu, highlightbackground="black", command=lambda:[], width=18, height=1, 
        text="Amigos del Movimiento", foreground='orange', activeforeground='orange', cursor="heart", 
        justify="center", bd=0, relief="groove", background="black", activebackground="black", 
        font=("URW Chancery L", 16)).pack()


    #BOTONES IZQUIERDA
    boton_offshell_desplegable_izq=Frame(root)
    boton_offshell_desplegable_izq.pack(fill=BOTH, expand=YES)
    boton_offshell_desplegable_izq.place(x=727, y=180)
    Button(boton_offshell_desplegable_izq, highlightbackground="black", 
        command=lambda:[webbrowser.open_new_tab("https://opensource.org/")], width=16, height=1, 
        text="OpenSource Iniciative", foreground='red', activeforeground='orange', cursor="heart", 
        justify="center", bd=0, relief="groove", background="black", activebackground="black", 
        font=("URW Chancery L", 14)).pack()

    boton_offshell_desplegable_izq2=Frame(root)
    boton_offshell_desplegable_izq2.pack(fill=BOTH, expand=YES)
    boton_offshell_desplegable_izq2.place(x=730, y=240)
    Button(boton_offshell_desplegable_izq2, highlightbackground="black", 
        command=lambda:[webbrowser.open_new_tab("https://www.docker.com/")], 
        width=15, height=1, text="Docker", foreground='red', 
        activeforeground='orange', cursor="heart", justify="center", bd=0, relief="groove", 
        background="black", activebackground="black", font=("URW Chancery L", 14)).pack()

    boton_offshell_desplegable_izq3=Frame(root)
    boton_offshell_desplegable_izq3.pack(fill=BOTH, expand=YES)
    boton_offshell_desplegable_izq3.place(x=730, y=300)
    Button(boton_offshell_desplegable_izq3, highlightbackground="black", 
        command=lambda:[webbrowser.open_new_tab("https://www.tensorflow.org/")], width=15, height=1, 
        text="TensorFlow", foreground='red', activeforeground='orange', cursor="heart", 
        justify="center", bd=0, relief="groove", background="black", activebackground="black", 
        font=("URW Chancery L", 14)).pack()

    boton_offshell_desplegable_izq4=Frame(root)
    boton_offshell_desplegable_izq4.pack(fill=BOTH, expand=YES)
    boton_offshell_desplegable_izq4.place(x=730, y=360)
    Button(boton_offshell_desplegable_izq4, highlightbackground="black", 
        command=lambda:[webbrowser.open_new_tab("http://consulproject.org/en/")], width=15, height=1, 
        text="Consul", foreground='red', activeforeground='orange', cursor="heart", 
        justify="center", bd=0, relief="groove", background="black", activebackground="black", 
        font=("URW Chancery L", 14)).pack()

    #BOTONES DERECHA
    boton_offshell_desplegable_der=Frame(root)
    boton_offshell_desplegable_der.pack(fill=BOTH, expand=YES)
    boton_offshell_desplegable_der.place(x=883, y=180)
    Button(boton_offshell_desplegable_der, highlightbackground="black", 
        command=lambda:[webbrowser.open_new_tab("https://www.linuxfoundation.org/")], width=15, height=1, 
        text="Linux Fundation", foreground='red', activeforeground='orange', cursor="heart", 
        justify="center", bd=0, relief="groove", background="black", activebackground="black", 
        font=("URW Chancery L", 14)).pack()

    boton_offshell_desplegable_der2=Frame(root)
    boton_offshell_desplegable_der2.pack(fill=BOTH, expand=YES)
    boton_offshell_desplegable_der2.place(x=880, y=240)
    Button(boton_offshell_desplegable_der2, highlightbackground="black", 
        command=lambda:[webbrowser.open_new_tab("https://www.hyperledger.org/")], 
        width=15, height=1, text="Hiperledger", foreground='red', activeforeground='orange', 
        cursor="heart", justify="center", bd=0, relief="groove", background="black", 
        activebackground="black", font=("URW Chancery L", 14)).pack()

    boton_offshell_desplegable_der2=Frame(root)
    boton_offshell_desplegable_der2.pack(fill=BOTH, expand=YES)
    boton_offshell_desplegable_der2.place(x=880, y=300)
    Button(boton_offshell_desplegable_der2, highlightbackground="black", 
        command=lambda:[webbrowser.open_new_tab("https://ev.kde.org/advisoryboard/")], 
        width=15, height=1, text="KDE e.V", foreground='red', activeforeground='orange', 
        cursor="heart", justify="center", bd=0, relief="groove", background="black", 
        activebackground="black", font=("URW Chancery L", 14)).pack()

    boton_offshell_desplegable_der3=Frame(root)
    boton_offshell_desplegable_der3.pack(fill=BOTH, expand=YES)
    boton_offshell_desplegable_der3.place(x=878, y=360)
    Button(boton_offshell_desplegable_der3, highlightbackground="black", 
        command=lambda:[webbrowser.open_new_tab("https://www.ow2.org/")], 
        width=15, height=1, text="OW2 Community", foreground='red', activeforeground='orange', 
        cursor="heart", justify="center", bd=0, relief="groove", background="black", 
        activebackground="black", font=("URW Chancery L", 14)).pack()

    #CERRAR DESPLEGABLE
    boton_cerrar_distros=Frame(root)
    boton_cerrar_distros.pack(fill=BOTH, expand=YES)
    boton_cerrar_distros.place(x=470, y=200)
    Button(boton_cerrar_distros, highlightbackground="black", command=lambda:[menu_principal()], 
        width=15, height=1, text="Menú Principal", foreground='red', activeforeground='orange', 
        cursor="fleur", justify="center", bd=0,  relief="raised", overrelief="sunken", 
        background="black", activebackground="black", font=("URW Chancery L", 15)).pack()


    pass

def mapa_ampliar2():
    
    #Mapa Conceptual Ampliado.
    botonBienvenido=Frame(root, width=1024, height=1024)
    botonBienvenido.pack(fill=BOTH, expand=YES)
    botonBienvenido.place(x=220, y=0)
    Button(botonBienvenido, image=codigo_grande, command=lambda:[codigo_open()], 
        cursor="heart", justify="center", bd=0, relief="raised", background="Black", 
        activebackground='black', font=("URW Chancery L", 15)).pack()

    pass

def ampliar_texto_open():
    boton_stallman=Frame(root)
    boton_stallman.pack(fill=BOTH, expand=YES)
    boton_stallman.place(x=60, y=110)
    Button(boton_stallman, highlightbackground="black", command=lambda:[codigo_open()], 
        text="El código abierto es un modelo de desarrollo de software basado en la\ncolaboración abierta. Se enfoca más en los beneficios prácticos\n(acceso al código fuente) que en cuestiones éticas o de libertad que\ntanto se destacan en el software libre. Para muchos el término «libre»\nhace referencia al hecho de adquirir un software de manera gratuita.\nLa idea del código abierto se centra en la premisa de que al compartir\nel código, el programa resultante tiende a ser de calidad superior\nal software propietario, es una visión técnica. El código abierto ofrece:\n1·Acceso al código fuente:\n  Para modificarlo, corregirlo o añadir más prestaciones.\n2·Gratuidad:\n  El software puede obtenerse libremente.\n3·La posibilidad de evitar monopolios de software propietario:\n  Para no depender de un único fabricante de software.\n4·Un modelo de avance:\n  Por lo cual la información no se oculta.", 
        foreground='orange', activeforeground='white', cursor="heart", 
        justify="left", bd=2, relief="groove", background="black", activebackground="black", 
        font=("URW Chancery L", 18)).pack()

    pass








def unete():

    boton_offshell_unete=Frame(root)
    boton_offshell_unete.pack(fill=BOTH, expand=YES)
    boton_offshell_unete.place(x=214, y=510)
    Button(boton_offshell_unete, highlightbackground="black", 
        command=lambda:[boton_offshell_unete.destroy()], width=80, height=5, 
        text="OffShell System nació con la idea de unificar una comunidad donde publicar software creado por usuari@s,\n para usuari@s. La mayor parte son aplicaciones o programas en GPL, licencia de Software Libre\npero también publicamos en código abierto con otras licencias, siempre respetuosas en su finalidad.\n Necesitamos más personas para ampliar los programas y la comunidad. Si te apasiona este mundo\ny quieres participar en el movimiento de software comunitario, puedes unirte a OffShell System.", 
        foreground='white', activeforeground='DarkRed', cursor="pirate", justify="center", bd=0, 
        relief="groove", background="black", activebackground="black", font=("URW Chancery L", 13)).pack()

    #Menu Volver Logo.
    boton_img_ligeros=Frame(root)
    boton_img_ligeros.place(x=513, y=300)
    Button(boton_img_ligeros, highlightbackground="black", command=lambda:[menu_principal()],
        image=inicio_logo, cursor='fleur', justify='center', bd=0, background="black", 
        activebackground="black").pack()


    pass


def menu_distros():

    botonBienvenido=Frame(root, width=1024, height=1024)
    botonBienvenido.pack(fill=BOTH, expand=YES)
    botonBienvenido.place(x=0, y=0)
    Button(botonBienvenido, image=imagen_fondo1, cursor="heart", justify="center", bd=0, relief="raised", 
        background="Black", activebackground='black', font=("URW Chancery L", 15)).pack()



    boton_img_servidor=Frame(root)
    boton_img_servidor.place(x=50, y=30)
    Button(boton_img_servidor, highlightbackground="Red", image=servidores_logo, 
        command=lambda:[servidores_distro()], cursor='fleur', justify='center', bd=0, 
        background="red", activebackground="DarkRed").pack()

    boton_servidor=Frame(root)
    boton_servidor.pack(fill=BOTH, expand=YES)
    boton_servidor.place(x=240, y=210)
    Button(boton_servidor, highlightbackground="red", command=lambda:[servidores_distro()], 
        width=17, height=1, text="OS Servidores", foreground='orange', activeforeground='Red', 
        cursor="fleur", justify="center", bd=0,  relief="raised", overrelief="sunken", 
        background="black", activebackground="black", font=("URW Chancery L", 15)).pack()


    boton_img_escritorio=Frame(root)
    boton_img_escritorio.place(x=710, y=30)
    Button(boton_img_escritorio, highlightbackground="Red", image=casa_logo, command=lambda:[distros()], 
        cursor='fleur', justify='center', bd=0, background="red", activebackground="DarkRed").pack()

    boton_escritorio=Frame(root)
    boton_escritorio.pack(fill=BOTH, expand=YES)
    boton_escritorio.place(x=700, y=210)
    Button(boton_escritorio, highlightbackground="red", command=lambda:[distros()], width=17, height=1, 
        text="OS Escritorio", foreground='orange', activeforeground='Red', cursor="fleur", 
        justify="center", bd=0,  relief="raised", overrelief="sunken", background="black", 
        activebackground="black", font=("URW Chancery L", 15)).pack()


    boton_img_juegos=Frame(root)
    boton_img_juegos.place(x=100, y=300)
    Button(boton_img_juegos, highlightbackground="black", image=juego_logo, 
        command=lambda:[juegos_distros()], cursor='fleur', justify='center', bd=0, 
        background="black", activebackground="black").pack()

    boton_juegos=Frame(root)
    boton_juegos.pack(fill=BOTH, expand=YES)
    boton_juegos.place(x=210, y=300)
    Button(boton_juegos, highlightbackground="black", command=lambda:[juegos_distros()], 
        width=10, height=1, text="OS para Gamers", foreground='orange', activeforeground='Red', 
        cursor="fleur", justify="center", bd=0,  relief="raised", overrelief="sunken", 
        background="black", activebackground="black", font=("URW Chancery L", 15)).pack()


    boton_img_ligeros=Frame(root)
    boton_img_ligeros.place(x=920, y=300)
    Button(boton_img_ligeros, highlightbackground="black", image=ligero_logo, 
        command=lambda:[ligeros()], cursor='fleur', justify='center', bd=0, 
        background="black", activebackground="black").pack()

    boton_ligeros=Frame(root)
    boton_ligeros.pack(fill=BOTH, expand=YES)
    boton_ligeros.place(x=760, y=300)
    Button(boton_ligeros, highlightbackground="black", command=lambda:[ligeros()], 
        width=14, height=1, text="OS Hardware Ligero", foreground='orange', activeforeground='Red', 
        cursor="fleur", justify="center", bd=0,  relief="raised", overrelief="sunken", 
        background="black", activebackground="black", font=("URW Chancery L", 15)).pack()




    #Cerrar Distribuciones.
    boton_cerrar_distros=Frame(root)
    boton_cerrar_distros.pack(fill=BOTH, expand=YES)
    boton_cerrar_distros.place(x=470, y=200)
    Button(boton_cerrar_distros, highlightbackground="black", command=lambda:[menu_principal()], width=15, height=1, text="Menú Principal", foreground='red', activeforeground='DarkRed', cursor="fleur", justify="center", bd=0,  relief="raised", overrelief="sunken", background="black", activebackground="black", font=("URW Chancery L", 15)).pack()

    boton_img_ligeros=Frame(root)
    boton_img_ligeros.place(x=515, y=560)
    Button(boton_img_ligeros, highlightbackground="black", image=probar_logo, cursor='fleur', 
        command=lambda:[webbrowser.open_new_tab("https://distrotest.net/")],
        justify='center', bd=0, background="black", activebackground="black").pack()

    boton_ligeros=Frame(root)
    boton_ligeros.pack(fill=BOTH, expand=YES)
    boton_ligeros.place(x=436, y=520)
    Button(boton_ligeros, highlightbackground="black", width=21, height=1, text="Probar Distribuciones Online", 
        command=lambda:[webbrowser.open_new_tab("https://distrotest.net/")],
        foreground='orange', activeforeground='Red', cursor="fleur", justify="center", bd=0,  
        relief="raised", overrelief="sunken", background="black", activebackground="black", 
        font=("URW Chancery L", 17)).pack()



    pass




def distros():

    botonBienvenido=Frame(root, width=1024, height=1024)
    botonBienvenido.pack(fill=BOTH, expand=YES)
    botonBienvenido.place(x=0, y=0)
    Button(botonBienvenido, image=imagen_fondo1, cursor="heart", justify="center", bd=0, relief="raised", 
        background="Black", activebackground='black', font=("URW Chancery L", 15)).pack()


    #Debian
    boton_img_distro1=Frame(root)
    boton_img_distro1.place(x=55, y=12)
    Button(boton_img_distro1, highlightbackground="Red", image=debian_logo, 
        command=lambda:[webbrowser.open_new_tab("https://www.debian.org/")], 
        cursor='fleur', justify='center', bd=0,  relief="raised", overrelief="raised", 
        activebackground="DarkRed").pack()

    boton_distro1=Frame(root)
    boton_distro1.pack(fill=BOTH, expand=YES)
    boton_distro1.place(x=6, y=64)
    Button(boton_distro1, highlightbackground="black", 
        command=lambda:[webbrowser.open_new_tab("https://www.debian.org/")], 
        width=17, height=1, text="Debian OS", foreground='white', activeforeground='Red', 
        cursor="fleur", justify="center", bd=0,  relief="raised", overrelief="sunken", 
        background="black", activebackground="black", font=("URW Chancery L", 15)).pack()

    #Ubuntu
    boton_img_distro2=Frame(root)
    boton_img_distro2.place(x=205, y=12)
    Button(boton_img_distro2, highlightbackground="Red", image=ubuntu_logo, 
        command=lambda:[webbrowser.open_new_tab("https://ubuntu.com/")], cursor='fleur', 
        justify='center', bd=0,  relief="raised", overrelief="raised", activebackground="DarkRed").pack()

    boton_distro2=Frame(root)
    boton_distro2.pack(fill=BOTH, expand=YES)
    boton_distro2.place(x=155, y=64)
    Button(boton_distro2, highlightbackground="black", 
        command=lambda:[webbrowser.open_new_tab("https://ubuntu.com/")], width=17, height=1, 
        text="Ubuntu OS", foreground='white', activeforeground='Red', cursor="fleur", 
        justify="center", bd=0,  relief="raised", overrelief="sunken", background="black", 
        activebackground="black", font=("URW Chancery L", 15)).pack()

    #Linux Mint
    boton_img_distro3=Frame(root)
    boton_img_distro3.place(x=355, y=12)
    Button(boton_img_distro3, highlightbackground="Red", image=linuxmint_logo, 
        command=lambda:[webbrowser.open_new_tab("https://linuxmint.com/")], cursor='fleur', 
        justify='center', bd=0,  relief="raised", overrelief="raised", activebackground="DarkRed").pack()

    boton_distro3=Frame(root)
    boton_distro3.pack(fill=BOTH, expand=YES)
    boton_distro3.place(x=304, y=64)
    Button(boton_distro3, highlightbackground="black", 
        command=lambda:[webbrowser.open_new_tab("https://linuxmint.com/")], width=17, height=1, 
        text="Linux Mint OS", foreground='white', activeforeground='Red', cursor="fleur", 
        justify="center", bd=0,  relief="raised", overrelief="sunken", background="black", 
        activebackground="black", font=("URW Chancery L", 15)).pack()

    #Elementary OS
    boton_img_distro4=Frame(root)
    boton_img_distro4.place(x=505, y=12)
    Button(boton_img_distro4, highlightbackground="Red", image=elementary_logo, 
        command=lambda:[webbrowser.open_new_tab("https://linuxmint.com/")], cursor='fleur', 
        justify='center', bd=0, relief="raised", overrelief="raised", activebackground="DarkRed").pack()

    boton_distro4=Frame(root)
    boton_distro4.pack(fill=BOTH, expand=YES)
    boton_distro4.place(x=454, y=64)
    Button(boton_distro4, highlightbackground="black", 
        command=lambda:[webbrowser.open_new_tab("https://linuxmint.com/")], 
        width=17, height=1, text="Elementary OS", foreground='white', activeforeground='Red', 
        cursor="fleur", justify="center", bd=0,  relief="raised", overrelief="sunken", 
        background="black", activebackground="black", font=("URW Chancery L", 15)).pack()

    #Fedora OS
    boton_img_distro5=Frame(root)
    boton_img_distro5.place(x=655, y=12)
    Button(boton_img_distro5, highlightbackground="Red", image=fedora_logo, 
        command=lambda:[webbrowser.open_new_tab("https://getfedora.org/")], cursor='fleur', 
        justify='center', bd=0, relief="raised", overrelief="raised", activebackground="DarkRed").pack()

    boton_distro5=Frame(root)
    boton_distro5.pack(fill=BOTH, expand=YES)
    boton_distro5.place(x=605, y=64)
    Button(boton_distro5, highlightbackground="black", 
        command=lambda:[webbrowser.open_new_tab("https://getfedora.org/")], width=17, height=1, 
        text="Fedora OS", foreground='white', activeforeground='Red', cursor="fleur", 
        justify="center", bd=0,  relief="raised", overrelief="sunken", background="black", 
        activebackground="black", font=("URW Chancery L", 15)).pack()

    #Manjaro OS
    boton_img_distro6=Frame(root)
    boton_img_distro6.place(x=805, y=12)
    Button(boton_img_distro6, highlightbackground="Red", image=manjaro_logo, command=lambda:[webbrowser.open_new_tab("https://manjaro.org/")], cursor='fleur', justify='center', bd=0, relief="raised", overrelief="raised", activebackground="DarkRed").pack()

    boton_distro6=Frame(root)
    boton_distro6.pack(fill=BOTH, expand=YES)
    boton_distro6.place(x=754, y=64)
    Button(boton_distro6, highlightbackground="black", 
        command=lambda:[webbrowser.open_new_tab("https://manjaro.org/")], width=17, height=1, 
        text="Manjaro OS", foreground='white', activeforeground='Red', cursor="fleur", 
        justify="center", bd=0,  relief="raised", overrelief="sunken", background="black", 
        activebackground="black", font=("URW Chancery L", 15)).pack()

    #Deepin OS
    boton_img_distro7=Frame(root)
    boton_img_distro7.place(x=955, y=12)
    Button(boton_img_distro7, highlightbackground="Red", image=deepin_logo, 
        command=lambda:[webbrowser.open_new_tab("https://www.distrowatch.com/table.php?distribution=deepin")], 
        cursor='fleur', justify='center', bd=0, relief="raised", overrelief="raised", 
        activebackground="DarkRed").pack()

    boton_distro7=Frame(root)
    boton_distro7.pack(fill=BOTH, expand=YES)
    boton_distro7.place(x=904, y=64)
    Button(boton_distro7, highlightbackground="black", 
        command=lambda:[webbrowser.open_new_tab("https://www.distrowatch.com/table.php?distribution=deepin")], 
        width=17, height=1, text="Deepin OS", foreground='white', activeforeground='Red', 
        cursor="fleur", justify="center", bd=0,  relief="raised", overrelief="sunken", 
        background="black", activebackground="black", font=("URW Chancery L", 15)).pack()


    #Peppermint OS
    boton_img_distro8=Frame(root)
    boton_img_distro8.place(x=55, y=152)
    Button(boton_img_distro8, highlightbackground="Red", image=peppermint_logo, 
        command=lambda:[webbrowser.open_new_tab("https://www.distrowatch.com/table.php?distribution=peppermint")], 
        cursor='fleur', justify='center', bd=0, relief="raised", overrelief="raised", 
        activebackground="DarkRed").pack()

    boton_distro8=Frame(root)
    boton_distro8.pack(fill=BOTH, expand=YES)
    boton_distro8.place(x=6, y=204)
    Button(boton_distro8, highlightbackground="black", 
        command=lambda:[webbrowser.open_new_tab("https://www.distrowatch.com/table.php?distribution=peppermint")], 
        width=17, height=1, text="Peppermint OS", foreground='white', activeforeground='Red', 
        cursor="fleur", justify="center", bd=0,  relief="raised", overrelief="sunken", 
        background="black", activebackground="black", font=("URW Chancery L", 15)).pack()


    #Bunsen Labs OS
    boton_img_distro9=Frame(root)
    boton_img_distro9.place(x=205, y=152)
    Button(boton_img_distro9, highlightbackground="red", image=bunsenlabs_logo, command=lambda:[webbrowser.open_new_tab("https://www.distrowatch.com/table.php?distribution=bunsenlabs")], cursor='fleur', justify='center', bd=0, relief="raised", overrelief="raised", activebackground="DarkRed").pack()

    boton_distro9=Frame(root)
    boton_distro9.pack(fill=BOTH, expand=YES)
    boton_distro9.place(x=155, y=204)
    Button(boton_distro9, highlightbackground="black", command=lambda:[webbrowser.open_new_tab("https://www.distrowatch.com/table.php?distribution=bunsenlabs")], width=17, height=1, text="BunsenLabs OS", foreground='white', activeforeground='Red', cursor="fleur", justify="center", bd=0,  relief="raised", overrelief="sunken", background="black", activebackground="black", font=("URW Chancery L", 15)).pack()

    #OpenBSD OS
    boton_img_distro10=Frame(root)
    boton_img_distro10.place(x=805, y=152)
    Button(boton_img_distro10, highlightbackground="red", image=openbsd_logo, command=lambda:[webbrowser.open_new_tab("https://www.openbsd.org/")], cursor='fleur', justify='center', bd=0, relief="raised", overrelief="raised", activebackground="DarkRed").pack()

    boton_distro10=Frame(root)
    boton_distro10.pack(fill=BOTH, expand=YES)
    boton_distro10.place(x=755, y=204)
    Button(boton_distro10, highlightbackground="black", command=lambda:[webbrowser.open_new_tab("https://www.openbsd.org/")], width=17, height=1, text="OpenBSD OS", foreground='white', activeforeground='Red', cursor="fleur", justify="center", bd=0,  relief="raised", overrelief="sunken", background="black", activebackground="black", font=("URW Chancery L", 15)).pack()

    #Zorin OS
    boton_img_distro11=Frame(root)
    boton_img_distro11.place(x=955, y=152)
    Button(boton_img_distro11, highlightbackground="red", image=zorin_logo, command=lambda:[webbrowser.open_new_tab("https://zorinos.com/")], cursor='fleur', justify='center', bd=0, relief="raised", overrelief="raised", activebackground="DarkRed").pack()

    boton_distro11=Frame(root)
    boton_distro11.pack(fill=BOTH, expand=YES)
    boton_distro11.place(x=904, y=204)
    Button(boton_distro11, highlightbackground="black", command=lambda:[webbrowser.open_new_tab("https://zorinos.com/")], width=17, height=1, text="Zorin OS", foreground='white', activeforeground='Red', cursor="fleur", justify="center", bd=0,  relief="raised", overrelief="sunken", background="black", activebackground="black", font=("URW Chancery L", 15)).pack()

    #MX Linux OS
    boton_img_distro12=Frame(root)
    boton_img_distro12.place(x=55, y=294)
    Button(boton_img_distro12, highlightbackground="Red", image=mxlinux_logo, command=lambda:[webbrowser.open_new_tab("https://mxlinux.org/")], cursor='fleur', justify='center', bd=0, relief="raised", overrelief="raised", activebackground="DarkRed").pack()

    boton_distro12=Frame(root)
    boton_distro12.pack(fill=BOTH, expand=YES)
    boton_distro12.place(x=6, y=344)
    Button(boton_distro12, highlightbackground="black", command=lambda:[webbrowser.open_new_tab("https://mxlinux.org/")], width=17, height=1, text="MX Linux OS", foreground='white', activeforeground='Red', cursor="fleur", justify="center", bd=0,  relief="raised", overrelief="sunken", background="black", activebackground="black", font=("URW Chancery L", 15)).pack()

    #Diagramas\nFeynman
    boton_img_distro13=Frame(root)
    boton_img_distro13.place(x=205, y=294)
    Button(boton_img_distro13, highlightbackground="Red", image=sabayon_logo, command=lambda:[webbrowser.open_new_tab("https://www.sabayon.org/")], cursor='fleur', justify='center', bd=0, relief="raised", overrelief="raised", background='black', activebackground="DarkRed").pack()

    boton_distro13=Frame(root)
    boton_distro13.pack(fill=BOTH, expand=YES)
    boton_distro13.place(x=155, y=344)
    Button(boton_distro13, highlightbackground="black", command=lambda:[webbrowser.open_new_tab("https://www.sabayon.org/")], width=17, height=1, text="Sabayon OS", foreground='white', activeforeground='Red', cursor="fleur", justify="center", bd=0,  relief="raised", overrelief="sunken", background="black", activebackground="black", font=("URW Chancery L", 15)).pack()

    #OpenSUSE OS
    boton_img_distro14=Frame(root)
    boton_img_distro14.place(x=805, y=294)
    Button(boton_img_distro14, highlightbackground="red", image=opensuse_logo2, command=lambda:[webbrowser.open_new_tab("https://www.opensuse.org/")], cursor='fleur', justify='center', bd=0, relief="raised", overrelief="raised", background="black", activebackground="DarkRed").pack()

    boton_distro10=Frame(root)
    boton_distro10.pack(fill=BOTH, expand=YES)
    boton_distro10.place(x=755, y=344)
    Button(boton_distro10, highlightbackground="black", command=lambda:[webbrowser.open_new_tab("https://www.opensuse.org/")], width=17, height=1, text="OpenSUSE OS", foreground='white', activeforeground='Red', cursor="fleur", justify="center", bd=0,  relief="raised", overrelief="sunken", background="black", activebackground="black", font=("URW Chancery L", 15)).pack()

    #Arch Linux OS
    boton_img_distro14=Frame(root)
    boton_img_distro14.place(x=955, y=294)
    Button(boton_img_distro14, highlightbackground="red", image=archlinux_logo, 
        command=lambda:[webbrowser.open_new_tab("https://www.archlinux.org/")], cursor='fleur', 
        justify='center', bd=0, relief="raised", overrelief="raised", background="black", 
        activebackground="DarkRed").pack()

    boton_distro10=Frame(root)
    boton_distro10.pack(fill=BOTH, expand=YES)
    boton_distro10.place(x=905, y=344)
    Button(boton_distro10, highlightbackground="black", 
        command=lambda:[webbrowser.open_new_tab("https://www.archlinux.org/")], width=17, height=1, 
        text="ArchLinux OS", foreground='white', activeforeground='Red', cursor="fleur", justify="center", 
        bd=0,  relief="raised", overrelief="sunken", background="black", activebackground="black", 
        font=("URW Chancery L", 15)).pack()




    #Cerrar Distribuciones.
    boton_cerrar_distros=Frame(root)
    boton_cerrar_distros.pack(fill=BOTH, expand=YES)
    boton_cerrar_distros.place(x=470, y=200)
    Button(boton_cerrar_distros, highlightbackground="black", command=lambda:[menu_principal()], width=15, height=1, text="Menú Principal", foreground='red', activeforeground='DarkRed', cursor="fleur", justify="center", bd=0,  relief="raised", overrelief="sunken", background="black", activebackground="black", font=("URW Chancery L", 15)).pack()

    #Menu Distribuciones.
    boton_cerrar_distros=Frame(root)
    boton_cerrar_distros.pack(fill=BOTH, expand=YES)
    boton_cerrar_distros.place(x=470, y=250)
    Button(boton_cerrar_distros, highlightbackground="black", command=lambda:[menu_distros()], width=15, height=1, text="Menú Distribuciones", foreground='red', activeforeground='DarkRed', cursor="fleur", justify="center", bd=0,  relief="raised", overrelief="sunken", background="black", activebackground="black", font=("URW Chancery L", 15)).pack()


    #Escritorio OS Logo.
    boton_img_ligeros=Frame(root)
    boton_img_ligeros.place(x=445, y=540)
    Button(boton_img_ligeros, highlightbackground="black", image=house_logo, cursor='fleur', justify='center', bd=0, background="black", activebackground="black").pack()

    boton_ligeros=Frame(root)
    boton_ligeros.pack(fill=BOTH, expand=YES)
    boton_ligeros.place(x=530, y=550)
    Button(boton_ligeros, highlightbackground="black", width=14, height=1, text="Distros Escritorio", foreground='white', activeforeground='Red', cursor="fleur", justify="center", bd=0,  relief="raised", overrelief="sunken", background="black", activebackground="black", font=("URW Chancery L", 15)).pack()

    pass


def servidores_distro():

    botonBienvenido=Frame(root, width=1024, height=1024)
    botonBienvenido.pack(fill=BOTH, expand=YES)
    botonBienvenido.place(x=0, y=0)
    Button(botonBienvenido, image=imagen_fondo1, cursor="heart", justify="center", bd=0, relief="raised", background="Black", activebackground='black', font=("URW Chancery L", 15)).pack()


    #Red Hat.
    boton_img_distro1=Frame(root)
    boton_img_distro1.place(x=55, y=12)
    Button(boton_img_distro1, highlightbackground="Red", image=redhat_logo, command=lambda:[webbrowser.open_new_tab("https://www.redhat.com/en")], cursor='fleur', justify='center', bd=0).pack()

    boton_distro1=Frame(root)
    boton_distro1.pack(fill=BOTH, expand=YES)
    boton_distro1.place(x=6, y=64)
    Button(boton_distro1, highlightbackground="black", command=lambda:[webbrowser.open_new_tab("https://www.redhat.com/en")], width=17, height=1, text="RedHat OS", foreground='white', activeforeground='Red', cursor="fleur", justify="center", bd=0,  relief="raised", overrelief="sunken", background="black", activebackground="black", font=("URW Chancery L", 15)).pack()

    #CentOS
    boton_img_distro2=Frame(root)
    boton_img_distro2.place(x=205, y=12)
    Button(boton_img_distro2, highlightbackground="Red", image=centos_logo, command=lambda:[webbrowser.open_new_tab("https://www.centos.org/")], cursor='fleur', justify='center', bd=0).pack()

    boton_distro2=Frame(root)
    boton_distro2.pack(fill=BOTH, expand=YES)
    boton_distro2.place(x=155, y=64)
    Button(boton_distro2, highlightbackground="black", command=lambda:[webbrowser.open_new_tab("https://www.centos.org/")], width=17, height=1, text="Centos OS", foreground='white', activeforeground='Red', cursor="fleur", justify="center", bd=0,  relief="raised", overrelief="sunken", background="black", activebackground="black", font=("URW Chancery L", 15)).pack()

    #Suse
    boton_img_distro3=Frame(root)
    boton_img_distro3.place(x=355, y=12)
    Button(boton_img_distro3, highlightbackground="Red", image=suse_logo, command=lambda:[webbrowser.open_new_tab("https://www.suse.com/download-linux/")], cursor='fleur', justify='center', bd=0).pack()

    boton_distro3=Frame(root)
    boton_distro3.pack(fill=BOTH, expand=YES)
    boton_distro3.place(x=304, y=64)
    Button(boton_distro3, highlightbackground="black", command=lambda:[webbrowser.open_new_tab("https://www.suse.com/download-linux/")], width=17, height=1, text="Suse OS", foreground='white', activeforeground='Red', cursor="fleur", justify="center", bd=0,  relief="raised", overrelief="sunken", background="black", activebackground="black", font=("URW Chancery L", 15)).pack()

    #Debian OS
    boton_img_distro4=Frame(root)
    boton_img_distro4.place(x=505, y=12)
    Button(boton_img_distro4, highlightbackground="Red", image=debian_logo, command=lambda:[webbrowser.open_new_tab("https://www.debian.org/")], cursor='fleur', justify='center', bd=0).pack()

    boton_distro4=Frame(root)
    boton_distro4.pack(fill=BOTH, expand=YES)
    boton_distro4.place(x=454, y=64)
    Button(boton_distro4, highlightbackground="black", command=lambda:[webbrowser.open_new_tab("https://www.debian.org/")], width=17, height=1, text="Debian OS", foreground='white', activeforeground='Red', cursor="fleur", justify="center", bd=0,  relief="raised", overrelief="sunken", background="black", activebackground="black", font=("URW Chancery L", 15)).pack()

    #Ubuntu Server OS
    boton_img_distro5=Frame(root)
    boton_img_distro5.place(x=655, y=12)
    Button(boton_img_distro5, highlightbackground="Red", image=ubuntuserver_logo, command=lambda:[webbrowser.open_new_tab("https://ubuntu.com/server")], cursor='fleur', justify='center', bd=0).pack()

    boton_distro5=Frame(root)
    boton_distro5.pack(fill=BOTH, expand=YES)
    boton_distro5.place(x=605, y=64)
    Button(boton_distro5, highlightbackground="black", command=lambda:[webbrowser.open_new_tab("https://ubuntu.com/server")], width=17, height=1, text="Ubuntu Server", foreground='white', activeforeground='Red', cursor="fleur", justify="center", bd=0,  relief="raised", overrelief="sunken", background="black", activebackground="black", font=("URW Chancery L", 15)).pack()

    #Fedora Server OS
    boton_img_distro6=Frame(root)
    boton_img_distro6.place(x=805, y=12)
    Button(boton_img_distro6, highlightbackground="Red", image=fedoraserver_logo, command=lambda:[webbrowser.open_new_tab("https://getfedora.org/en/server/")], cursor='fleur', justify='center', bd=0).pack()

    boton_distro6=Frame(root)
    boton_distro6.pack(fill=BOTH, expand=YES)
    boton_distro6.place(x=754, y=64)
    Button(boton_distro6, highlightbackground="black", command=lambda:[webbrowser.open_new_tab("https://getfedora.org/en/server/")], width=17, height=1, text="Fedora Server", foreground='white', activeforeground='Red', cursor="fleur", justify="center", bd=0,  relief="raised", overrelief="sunken", background="black", activebackground="black", font=("URW Chancery L", 15)).pack()

    #Oracle Cloud OS
    boton_img_distro7=Frame(root)
    boton_img_distro7.place(x=955, y=12)
    Button(boton_img_distro7, highlightbackground="Red", image=oraclecloud_logo, command=lambda:[webbrowser.open_new_tab("https://edelivery.oracle.com/osdc/faces/Home.jspx;jsessionid=BP_vhWxsqGrqrvjq4ixyRejB-lnDym3FZY8pjeAnMh4DA9p5oPgO!-1722204455")], cursor='fleur', justify='center', bd=0).pack()

    boton_distro7=Frame(root)
    boton_distro7.pack(fill=BOTH, expand=YES)
    boton_distro7.place(x=904, y=64)
    Button(boton_distro7, highlightbackground="black", command=lambda:[webbrowser.open_new_tab("https://edelivery.oracle.com/osdc/faces/Home.jspx;jsessionid=BP_vhWxsqGrqrvjq4ixyRejB-lnDym3FZY8pjeAnMh4DA9p5oPgO!-1722204455")], width=17, height=1, text="Oracle Cloud", foreground='white', activeforeground='Red', cursor="fleur", justify="center", bd=0,  relief="raised", overrelief="sunken", background="black", activebackground="black", font=("URW Chancery L", 15)).pack()

    #Mageia OS
    boton_img_distro8=Frame(root)
    boton_img_distro8.place(x=55, y=152)
    Button(boton_img_distro8, highlightbackground="Red", image=mageia_logo, command=lambda:[webbrowser.open_new_tab("https://www.mageia.org/es/")], cursor='fleur', justify='center', bd=0, relief="raised", overrelief="raised", activebackground="DarkRed").pack()

    boton_distro8=Frame(root)
    boton_distro8.pack(fill=BOTH, expand=YES)
    boton_distro8.place(x=6, y=204)
    Button(boton_distro8, highlightbackground="black", command=lambda:[webbrowser.open_new_tab("https://www.distrowatch.com/table.php?distribution=peppermint")], width=17, height=1, text="Mageia OS", foreground='white', activeforeground='Red', cursor="fleur", justify="center", bd=0,  relief="raised", overrelief="sunken", background="black", activebackground="black", font=("URW Chancery L", 15)).pack()

    #Clear OS
    boton_img_distro9=Frame(root)
    boton_img_distro9.place(x=205, y=152)
    Button(boton_img_distro9, highlightbackground="red", image=clear_logo, command=lambda:[webbrowser.open_new_tab("https://www.clearos.com/")], cursor='fleur', justify='center', bd=0, relief="raised", overrelief="raised", activebackground="DarkRed").pack()

    boton_distro9=Frame(root)
    boton_distro9.pack(fill=BOTH, expand=YES)
    boton_distro9.place(x=155, y=204)
    Button(boton_distro9, highlightbackground="black", command=lambda:[webbrowser.open_new_tab("https://www.clearos.com/")], width=17, height=1, text="Clear OS", foreground='white', activeforeground='Red', cursor="fleur", justify="center", bd=0,  relief="raised", overrelief="sunken", background="black", activebackground="black", font=("URW Chancery L", 15)).pack()

    #ArchLinux OS
    boton_img_distro10=Frame(root)
    boton_img_distro10.place(x=805, y=152)
    Button(boton_img_distro10, highlightbackground="red", image=arch_logo, command=lambda:[webbrowser.open_new_tab("https://www.archlinux.org/")], cursor='fleur', justify='center', bd=0, relief="raised", overrelief="raised", activebackground="DarkRed").pack()

    boton_distro10=Frame(root)
    boton_distro10.pack(fill=BOTH, expand=YES)
    boton_distro10.place(x=755, y=204)
    Button(boton_distro10, highlightbackground="black", command=lambda:[webbrowser.open_new_tab("https://www.archlinux.org/")], width=17, height=1, text="ArchLinux OS", foreground='white', activeforeground='Red', cursor="fleur", justify="center", bd=0,  relief="raised", overrelief="sunken", background="black", activebackground="black", font=("URW Chancery L", 15)).pack()

    #Suse Linux OS
    boton_img_distro11=Frame(root)
    boton_img_distro11.place(x=955, y=152)
    Button(boton_img_distro11, highlightbackground="red", image=suse2_logo, command=lambda:[webbrowser.open_new_tab("https://www.suse.com/es-es/products/server/")], cursor='fleur', justify='center', bd=0, relief="raised", overrelief="raised", activebackground="DarkRed").pack()

    boton_distro11=Frame(root)
    boton_distro11.pack(fill=BOTH, expand=YES)
    boton_distro11.place(x=904, y=204)
    Button(boton_distro11, highlightbackground="black", command=lambda:[webbrowser.open_new_tab("https://www.suse.com/es-es/products/server/")], width=17, height=1, text="Suse Linux OS", foreground='white', activeforeground='Red', cursor="fleur", justify="center", bd=0,  relief="raised", overrelief="sunken", background="black", activebackground="black", font=("URW Chancery L", 15)).pack()



    #Cerrar Distribuciones.
    boton_cerrar_distros=Frame(root)
    boton_cerrar_distros.pack(fill=BOTH, expand=YES)
    boton_cerrar_distros.place(x=470, y=200)
    Button(boton_cerrar_distros, highlightbackground="black", command=lambda:[menu_principal()], width=15, height=1, text="Menú Principal", foreground='red', activeforeground='DarkRed', cursor="fleur", justify="center", bd=0,  relief="raised", overrelief="sunken", background="black", activebackground="black", font=("URW Chancery L", 15)).pack()

    #Menu Distribuciones.
    boton_cerrar_distros=Frame(root)
    boton_cerrar_distros.pack(fill=BOTH, expand=YES)
    boton_cerrar_distros.place(x=470, y=250)
    Button(boton_cerrar_distros, highlightbackground="black", command=lambda:[menu_distros()], width=15, height=1, text="Menú Distribuciones", foreground='red', activeforeground='DarkRed', cursor="fleur", justify="center", bd=0,  relief="raised", overrelief="sunken", background="black", activebackground="black", font=("URW Chancery L", 15)).pack()


    #Servidores OS Logo.
    boton_img_ligeros=Frame(root)
    boton_img_ligeros.place(x=445, y=540)
    Button(boton_img_ligeros, highlightbackground="black", image=servidores_logo2, cursor='fleur', justify='center', bd=0, background="black", activebackground="black").pack()

    boton_ligeros=Frame(root)
    boton_ligeros.pack(fill=BOTH, expand=YES)
    boton_ligeros.place(x=530, y=550)
    Button(boton_ligeros, highlightbackground="black", width=14, height=1, text="Distros Servidores", foreground='white', activeforeground='Red', cursor="fleur", justify="center", bd=0,  relief="raised", overrelief="sunken", background="black", activebackground="black", font=("URW Chancery L", 15)).pack()


    
    pass

def ligeros():

    botonBienvenido=Frame(root, width=1024, height=1024)
    botonBienvenido.pack(fill=BOTH, expand=YES)
    botonBienvenido.place(x=0, y=0)
    Button(botonBienvenido, image=imagen_fondo1, cursor="heart", justify="center", bd=0, relief="raised", background="Black", activebackground='black', font=("URW Chancery L", 15)).pack()


    #TinyCore OS
    boton_img_distro8=Frame(root)
    boton_img_distro8.place(x=55, y=152)
    Button(boton_img_distro8, highlightbackground="Red", image=tinycore_logo, command=lambda:[webbrowser.open_new_tab("http://tinycorelinux.net/")], cursor='fleur', justify='center', bd=0, relief="raised", overrelief="raised", activebackground="DarkRed").pack()

    boton_distro8=Frame(root)
    boton_distro8.pack(fill=BOTH, expand=YES)
    boton_distro8.place(x=6, y=204)
    Button(boton_distro8, highlightbackground="black", command=lambda:[webbrowser.open_new_tab("http://tinycorelinux.net/")], width=17, height=1, text="Tiny Core OS", foreground='white', activeforeground='Red', cursor="fleur", justify="center", bd=0,  relief="raised", overrelief="sunken", background="black", activebackground="black", font=("URW Chancery L", 15)).pack()


    #Bunsen Labs OS
    boton_img_distro9=Frame(root)
    boton_img_distro9.place(x=205, y=152)
    Button(boton_img_distro9, highlightbackground="red", image=bunsenlabs_logo, command=lambda:[webbrowser.open_new_tab("https://www.distrowatch.com/table.php?distribution=bunsenlabs")], cursor='fleur', justify='center', bd=0, relief="raised", overrelief="raised", activebackground="DarkRed").pack()

    boton_distro9=Frame(root)
    boton_distro9.pack(fill=BOTH, expand=YES)
    boton_distro9.place(x=155, y=204)
    Button(boton_distro9, highlightbackground="black", command=lambda:[webbrowser.open_new_tab("https://www.distrowatch.com/table.php?distribution=bunsenlabs")], width=17, height=1, text="BunsenLabs OS", foreground='white', activeforeground='Red', cursor="fleur", justify="center", bd=0,  relief="raised", overrelief="sunken", background="black", activebackground="black", font=("URW Chancery L", 15)).pack()

    #Puppy Linux OS
    boton_img_distro10=Frame(root)
    boton_img_distro10.place(x=805, y=152)
    Button(boton_img_distro10, highlightbackground="red", image=puppy_logo, command=lambda:[webbrowser.open_new_tab("http://puppylinux.com/")], cursor='fleur', justify='center', bd=0, relief="raised", overrelief="raised", activebackground="DarkRed").pack()

    boton_distro10=Frame(root)
    boton_distro10.pack(fill=BOTH, expand=YES)
    boton_distro10.place(x=755, y=204)
    Button(boton_distro10, highlightbackground="black", command=lambda:[webbrowser.open_new_tab("http://puppylinux.com/")], width=17, height=1, text="Puppy Linux OS", foreground='white', activeforeground='Red', cursor="fleur", justify="center", bd=0,  relief="raised", overrelief="sunken", background="black", activebackground="black", font=("URW Chancery L", 15)).pack()

    #Linux Lite OS
    boton_img_distro11=Frame(root)
    boton_img_distro11.place(x=955, y=152)
    Button(boton_img_distro11, highlightbackground="red", image=linuxlite_logo, command=lambda:[webbrowser.open_new_tab("https://www.linuxliteos.com/")], cursor='fleur', justify='center', bd=0, relief="raised", overrelief="raised", activebackground="DarkRed").pack()

    boton_distro11=Frame(root)
    boton_distro11.pack(fill=BOTH, expand=YES)
    boton_distro11.place(x=904, y=204)
    Button(boton_distro11, highlightbackground="black", command=lambda:[webbrowser.open_new_tab("https://www.linuxliteos.com/")], width=17, height=1, text="Linux Lite OS", foreground='white', activeforeground='Red', cursor="fleur", justify="center", bd=0,  relief="raised", overrelief="sunken", background="black", activebackground="black", font=("URW Chancery L", 15)).pack()

    #Lubuntu OS
    boton_img_distro12=Frame(root)
    boton_img_distro12.place(x=55, y=294)
    Button(boton_img_distro12, highlightbackground="Red", image=lubuntu_logo, command=lambda:[webbrowser.open_new_tab("https://lubuntu.me/")], cursor='fleur', justify='center', bd=0, relief="raised", overrelief="raised", activebackground="DarkRed").pack()

    boton_distro12=Frame(root)
    boton_distro12.pack(fill=BOTH, expand=YES)
    boton_distro12.place(x=6, y=344)
    Button(boton_distro12, highlightbackground="black", command=lambda:[webbrowser.open_new_tab("https://lubuntu.me/")], width=17, height=1, text="Lubuntu OS", foreground='white', activeforeground='Red', cursor="fleur", justify="center", bd=0,  relief="raised", overrelief="sunken", background="black", activebackground="black", font=("URW Chancery L", 15)).pack()

    #Lxle OS
    boton_img_distro13=Frame(root)
    boton_img_distro13.place(x=205, y=294)
    Button(boton_img_distro13, highlightbackground="Red", image=lxle_logo, command=lambda:[webbrowser.open_new_tab("https://www.lxle.net/")], cursor='fleur', justify='center', bd=0, relief="raised", overrelief="raised", background='black', activebackground="DarkRed").pack()

    boton_distro13=Frame(root)
    boton_distro13.pack(fill=BOTH, expand=YES)
    boton_distro13.place(x=155, y=344)
    Button(boton_distro13, highlightbackground="black", command=lambda:[webbrowser.open_new_tab("https://www.lxle.net/")], width=17, height=1, text="LXLE OS", foreground='white', activeforeground='Red', cursor="fleur", justify="center", bd=0,  relief="raised", overrelief="sunken", background="black", activebackground="black", font=("URW Chancery L", 15)).pack()

    #AntiX OS
    boton_img_distro14=Frame(root)
    boton_img_distro14.place(x=805, y=294)
    Button(boton_img_distro14, highlightbackground="red", image=antix_logo, command=lambda:[webbrowser.open_new_tab("https://antixlinux.com/")], cursor='fleur', justify='center', bd=0, relief="raised", overrelief="raised", background="black", activebackground="DarkRed").pack()

    boton_distro14=Frame(root)
    boton_distro14.pack(fill=BOTH, expand=YES)
    boton_distro14.place(x=755, y=344)
    Button(boton_distro14, highlightbackground="black", command=lambda:[webbrowser.open_new_tab("https://antixlinux.com/")], width=17, height=1, text="AntiX OS", foreground='white', activeforeground='Red', cursor="fleur", justify="center", bd=0,  relief="raised", overrelief="sunken", background="black", activebackground="black", font=("URW Chancery L", 15)).pack()

    #Xubuntu OS
    boton_img_distro14=Frame(root)
    boton_img_distro14.place(x=955, y=294)
    Button(boton_img_distro14, highlightbackground="red", image=xubuntu_logo, command=lambda:[webbrowser.open_new_tab("https://xubuntu.org/")], cursor='fleur', justify='center', bd=0, relief="raised", overrelief="raised", background="black", activebackground="DarkRed").pack()

    boton_distro14=Frame(root)
    boton_distro14.pack(fill=BOTH, expand=YES)
    boton_distro14.place(x=905, y=344)
    Button(boton_distro14, highlightbackground="black", 
        command=lambda:[webbrowser.open_new_tab("https://xubuntu.org/")], width=17, height=1, 
        text="Xubuntu OS", foreground='white', activeforeground='Red', cursor="fleur", 
        justify="center", bd=0,  relief="raised", overrelief="sunken", background="black", 
        activebackground="black", font=("URW Chancery L", 15)).pack()




    #Cerrar Distribuciones.
    boton_cerrar_distros=Frame(root)
    boton_cerrar_distros.pack(fill=BOTH, expand=YES)
    boton_cerrar_distros.place(x=470, y=200)
    Button(boton_cerrar_distros, highlightbackground="black", command=lambda:[menu_principal()], 
        width=15, height=1, text="Menú Principal", foreground='red', activeforeground='DarkRed', 
        cursor="fleur", justify="center", bd=0,  relief="raised", overrelief="sunken", 
        background="black", activebackground="black", font=("URW Chancery L", 15)).pack()

    #Menu Distribuciones.
    boton_cerrar_distros=Frame(root)
    boton_cerrar_distros.pack(fill=BOTH, expand=YES)
    boton_cerrar_distros.place(x=470, y=250)
    Button(boton_cerrar_distros, highlightbackground="black", command=lambda:[menu_distros()], 
        width=15, height=1, text="Menú Distribuciones", foreground='red', activeforeground='DarkRed', 
        cursor="fleur", justify="center", bd=0,  relief="raised", overrelief="sunken", 
        background="black", activebackground="black", font=("URW Chancery L", 15)).pack()


    #Ligeros OS Logo.
    boton_img_ligeros=Frame(root)
    boton_img_ligeros.place(x=445, y=550)
    Button(boton_img_ligeros, highlightbackground="black", image=ligero_logo, cursor='fleur', 
        justify='center', bd=0, background="black", activebackground="black").pack()

    boton_ligeros=Frame(root)
    boton_ligeros.pack(fill=BOTH, expand=YES)
    boton_ligeros.place(x=530, y=550)
    Button(boton_ligeros, highlightbackground="black", width=14, height=1, text="Distros Ligeras", 
        foreground='white', activeforeground='Red', cursor="fleur", justify="center", bd=0,  
        relief="raised", overrelief="sunken", background="black", activebackground="black", 
        font=("URW Chancery L", 15)).pack()



    pass


def juegos_distros():

    botonBienvenido=Frame(root, width=1024, height=1024)
    botonBienvenido.pack(fill=BOTH, expand=YES)
    botonBienvenido.place(x=0, y=0)
    Button(botonBienvenido, image=imagen_fondo1, cursor="heart", justify="center", bd=0, 
        relief="raised", background="Black", activebackground='black', 
        font=("URW Chancery L", 15)).pack()


    #Steam OS.
    boton_img_distro1=Frame(root)
    boton_img_distro1.place(x=55, y=12)
    Button(boton_img_distro1, highlightbackground="Red", image=steam_logo, 
        command=lambda:[webbrowser.open_new_tab("https://store.steampowered.com/steamos/buildyourown")], 
        cursor='fleur', justify='center', bd=0,  relief="raised", overrelief="raised", 
        activebackground="DarkRed").pack()

    boton_distro1=Frame(root)
    boton_distro1.pack(fill=BOTH, expand=YES)
    boton_distro1.place(x=6, y=64)
    Button(boton_distro1, highlightbackground="black", 
        command=lambda:[webbrowser.open_new_tab("https://store.steampowered.com/steamos/buildyourown")], 
        width=17, height=1, text="Steam OS", foreground='white', activeforeground='Red', 
        cursor="fleur", justify="center", bd=0,  relief="raised", overrelief="sunken", 
        background="black", activebackground="black", font=("URW Chancery L", 15)).pack()

    #Ubuntu OS
    boton_img_distro2=Frame(root)
    boton_img_distro2.place(x=205, y=12)
    Button(boton_img_distro2, highlightbackground="Red", image=ubuntu_logo, 
        command=lambda:[webbrowser.open_new_tab("https://ubuntu.com/")], cursor='fleur', 
        justify='center', bd=0,  relief="raised", overrelief="raised", 
        activebackground="DarkRed").pack()

    boton_distro2=Frame(root)
    boton_distro2.pack(fill=BOTH, expand=YES)
    boton_distro2.place(x=155, y=64)
    Button(boton_distro2, highlightbackground="black", 
        command=lambda:[webbrowser.open_new_tab("https://ubuntu.com/")], width=17, height=1, 
        text="Ubuntu OS", foreground='white', activeforeground='Red', cursor="fleur", 
        justify="center", bd=0,  relief="raised", overrelief="sunken", background="black", 
        activebackground="black", font=("URW Chancery L", 15)).pack()

    #Super Gamer Mint
    boton_img_distro3=Frame(root)
    boton_img_distro3.place(x=355, y=12)
    Button(boton_img_distro3, highlightbackground="Red", image=supergamer_logo, 
        command=lambda:[webbrowser.open_new_tab("https://www.supergamer.x10host.com/")], 
        cursor='fleur', justify='center', bd=0,  relief="raised", overrelief="raised", 
        activebackground="DarkRed").pack()

    boton_distro3=Frame(root)
    boton_distro3.pack(fill=BOTH, expand=YES)
    boton_distro3.place(x=304, y=64)
    Button(boton_distro3, highlightbackground="black", 
        command=lambda:[webbrowser.open_new_tab("https://www.supergamer.x10host.com/")], width=17, height=1, 
        text="Super Gamer OS", foreground='white', activeforeground='Red', cursor="fleur", justify="center", 
        bd=0,  relief="raised", overrelief="sunken", background="black", activebackground="black", 
        font=("URW Chancery L", 15)).pack()

    #Linux Console OS
    boton_img_distro4=Frame(root)
    boton_img_distro4.place(x=505, y=12)
    Button(boton_img_distro4, highlightbackground="Red", image=linuxconsole_logo, 
        command=lambda:[webbrowser.open_new_tab("https://www.linuxconsole.org/")], cursor='fleur', 
        justify='center', bd=0, relief="raised", overrelief="raised", activebackground="DarkRed").pack()

    boton_distro4=Frame(root)
    boton_distro4.pack(fill=BOTH, expand=YES)
    boton_distro4.place(x=454, y=64)
    Button(boton_distro4, highlightbackground="black", 
        command=lambda:[webbrowser.open_new_tab("https://www.linuxconsole.org/")], width=17, height=1, 
        text="Linux Console", foreground='white', activeforeground='Red', cursor="fleur", 
        justify="center", bd=0,  relief="raised", overrelief="sunken", background="black", 
        activebackground="black", font=("URW Chancery L", 15)).pack()

    #Manjaro MGame OS
    boton_img_distro5=Frame(root)
    boton_img_distro5.place(x=655, y=12)
    Button(boton_img_distro5, highlightbackground="Red", image=manjarogame_logo, 
        command=lambda:[webbrowser.open_new_tab("https://sourceforge.net/projects/mgame/")], 
        cursor='fleur', justify='center', bd=0, relief="raised", overrelief="raised", 
        activebackground="DarkRed").pack()

    boton_distro5=Frame(root)
    boton_distro5.pack(fill=BOTH, expand=YES)
    boton_distro5.place(x=605, y=64)
    Button(boton_distro5, highlightbackground="black", 
        command=lambda:[webbrowser.open_new_tab("https://sourceforge.net/projects/mgame/")], width=17, height=1, 
        text="Manjaro MGame", foreground='white', activeforeground='Red', cursor="fleur", justify="center", bd=0, 
        relief="raised", overrelief="sunken", background="black", activebackground="black", 
        font=("URW Chancery L", 15)).pack()

    #Lakka OS
    boton_img_distro6=Frame(root)
    boton_img_distro6.place(x=805, y=12)
    Button(boton_img_distro6, highlightbackground="Red", image=lakka_logo, 
        command=lambda:[webbrowser.open_new_tab("https://www.lakka.tv/")], cursor='fleur', 
        justify='center', bd=0, relief="raised", overrelief="raised", background="black", 
        activebackground="DarkRed").pack()

    boton_distro6=Frame(root)
    boton_distro6.pack(fill=BOTH, expand=YES)
    boton_distro6.place(x=754, y=64)
    Button(boton_distro6, highlightbackground="black", 
        command=lambda:[webbrowser.open_new_tab("https://www.lakka.tv/")], width=17, height=1, 
        text="Lakka OS", foreground='white', activeforeground='Red', cursor="fleur", 
        justify="center", bd=0,  relief="raised", overrelief="sunken", background="black", 
        activebackground="black", font=("URW Chancery L", 15)).pack()

    #Solus OS
    boton_img_distro7=Frame(root)
    boton_img_distro7.place(x=955, y=12)
    Button(boton_img_distro7, highlightbackground="Red", image=solus_logo, 
        command=lambda:[webbrowser.open_new_tab("https://getsol.us/home/")], 
        cursor='fleur', justify='center', bd=0, relief="raised", overrelief="raised", 
        activebackground="DarkRed").pack()

    boton_distro7=Frame(root)
    boton_distro7.pack(fill=BOTH, expand=YES)
    boton_distro7.place(x=904, y=64)
    Button(boton_distro7, highlightbackground="black", 
        command=lambda:[webbrowser.open_new_tab("https://getsol.us/home/")], 
        width=17, height=1, text="Solus OS", foreground='white', activeforeground='Red', 
        cursor="fleur", justify="center", bd=0,  relief="raised", overrelief="sunken", 
        background="black", activebackground="black", font=("URW Chancery L", 15)).pack()


    #Fedora Games Spin OS
    boton_img_distro8=Frame(root)
    boton_img_distro8.place(x=55, y=152)
    Button(boton_img_distro8, highlightbackground="Red", image=fedoragames_logo, 
        command=lambda:[webbrowser.open_new_tab("https://fedoraproject.org/wiki/Games_Lab?rd=Games_Spin")], 
        cursor='fleur', justify='center', bd=0, relief="raised", overrelief="raised", 
        activebackground="DarkRed").pack()

    boton_distro8=Frame(root)
    boton_distro8.pack(fill=BOTH, expand=YES)
    boton_distro8.place(x=6, y=204)
    Button(boton_distro8, highlightbackground="black", 
        command=lambda:[webbrowser.open_new_tab("https://fedoraproject.org/wiki/Games_Lab?rd=Games_Spin")], 
        width=17, height=1, text="Spin FedoraGames", foreground='white', activeforeground='Red', 
        cursor="fleur", justify="center", bd=0,  relief="raised", overrelief="sunken", 
        background="black", activebackground="black", font=("URW Chancery L", 15)).pack()


    #Sparky GameOver OS
    boton_img_distro9=Frame(root)
    boton_img_distro9.place(x=205, y=152)
    Button(boton_img_distro9, highlightbackground="red", image=gameover_logo, 
        command=lambda:[webbrowser.open_new_tab("https://sparkylinux.org/download/")], 
        cursor='fleur', justify='center', bd=0, relief="raised", overrelief="raised", 
        activebackground="DarkRed").pack()

    boton_distro9=Frame(root)
    boton_distro9.pack(fill=BOTH, expand=YES)
    boton_distro9.place(x=155, y=204)
    Button(boton_distro9, highlightbackground="black", 
        command=lambda:[webbrowser.open_new_tab("https://sparkylinux.org/download/")], width=17, height=1, 
        text="Sparky GameOver", foreground='white', activeforeground='Red', cursor="fleur", 
        justify="center", bd=0,  relief="raised", overrelief="sunken", background="black", 
        activebackground="black", font=("URW Chancery L", 15)).pack()

    #Ubuntu GamePack Spin OS
    boton_img_distro10=Frame(root)
    boton_img_distro10.place(x=805, y=152)
    Button(boton_img_distro10, highlightbackground="red", image=ubuntugame_logo, 
        command=lambda:[webbrowser.open_new_tab("https://ualinux.com/en/ubuntu-gamepack")], 
        cursor='fleur', justify='center', bd=0, relief="raised", overrelief="raised", 
        activebackground="DarkRed").pack()

    boton_distro10=Frame(root)
    boton_distro10.pack(fill=BOTH, expand=YES)
    boton_distro10.place(x=751, y=204)
    Button(boton_distro10, highlightbackground="black", 
        command=lambda:[webbrowser.open_new_tab("https://ualinux.com/en/ubuntu-gamepack")], 
        width=17, height=1, text="Ubuntu GamePack", foreground='white', activeforeground='Red', 
        cursor="fleur", justify="center", bd=0,  relief="raised", overrelief="sunken", 
        background="black", activebackground="black", font=("URW Chancery L", 15)).pack()

    #Game Drift Linux OS
    boton_img_distro11=Frame(root)
    boton_img_distro11.place(x=955, y=152)
    Button(boton_img_distro11, highlightbackground="red", image=gamedrift_logo, 
        command=lambda:[webbrowser.open_new_tab("http://gamedrift.org/obsolete/")], 
        cursor='fleur', justify='center', bd=0, relief="raised", overrelief="raised", 
        activebackground="DarkRed").pack()

    boton_distro11=Frame(root)
    boton_distro11.pack(fill=BOTH, expand=YES)
    boton_distro11.place(x=908, y=204)
    Button(boton_distro11, highlightbackground="black", 
        command=lambda:[webbrowser.open_new_tab("http://gamedrift.org/obsolete/")], width=17, height=1, 
        text="Game Drift OS", foreground='white', activeforeground='Red', cursor="fleur", 
        justify="center", bd=0,  relief="raised", overrelief="sunken", background="black", 
        activebackground="black", font=("URW Chancery L", 15)).pack()



    #Cerrar Distribuciones.
    boton_cerrar_distros=Frame(root)
    boton_cerrar_distros.pack(fill=BOTH, expand=YES)
    boton_cerrar_distros.place(x=470, y=200)
    Button(boton_cerrar_distros, highlightbackground="black", 
        command=lambda:[menu_principal(), boton_cerrar_distros.destroy(), boton_img_distro1.destroy(),  boton_distro1.destroy(), boton_img_distro2.destroy(), boton_distro2.destroy(), boton_img_distro3.destroy(), boton_distro3.destroy(), boton_img_distro4.destroy(), boton_distro4.destroy(), boton_img_distro5.destroy(), boton_distro5.destroy(), boton_img_distro6.destroy(), boton_distro6.destroy(), boton_img_distro7.destroy(), boton_distro7.destroy(), boton_img_distro8.destroy(), boton_distro8.destroy(), boton_img_distro9.destroy(), boton_distro9.destroy(), boton_img_distro10.destroy(), boton_distro10.destroy(), boton_img_distro11.destroy(), boton_distro11.destroy()], 
        width=15, height=1, text="Menú Principal", foreground='red', activeforeground='DarkRed', 
        cursor="fleur", justify="center", bd=0,  relief="raised", overrelief="sunken", 
        background="black", activebackground="black", font=("URW Chancery L", 15)).pack()

    #Menu Distribuciones.
    boton_cerrar_distros=Frame(root)
    boton_cerrar_distros.pack(fill=BOTH, expand=YES)
    boton_cerrar_distros.place(x=470, y=250)
    Button(boton_cerrar_distros, highlightbackground="black", command=lambda:[menu_distros()], 
        width=15, height=1, text="Menú Distribuciones", foreground='red', activeforeground='DarkRed', 
        cursor="fleur", justify="center", bd=0,  relief="raised", overrelief="sunken", 
        background="black", activebackground="black", font=("URW Chancery L", 15)).pack()


    #Icono Juegos.
    boton_img_juegos=Frame(root)
    boton_img_juegos.place(x=460, y=550)
    Button(boton_img_juegos, highlightbackground="black", image=juego_logo, cursor='fleur', 
        justify='center', bd=0, background="black", activebackground="black").pack()

    boton_juegos=Frame(root)
    boton_juegos.pack(fill=BOTH, expand=YES)
    boton_juegos.place(x=550, y=550)
    Button(boton_juegos, highlightbackground="black", width=10, height=1, text="OS Juegos", 
        foreground='white', activeforeground='Red', cursor="fleur", justify="center", bd=0, 
        relief="raised", overrelief="sunken", background="black", activebackground="black", 
        font=("URW Chancery L", 15)).pack()


    pass




def menu_principal():
    
    botonBienvenido=Frame(root, width=1024, height=1024)
    botonBienvenido.pack(fill=BOTH, expand=YES)
    botonBienvenido.place(x=0, y=0)
    Button(botonBienvenido, image=imagen_fondo1, cursor="heart", justify="center", bd=0, relief="raised", 
        background="Black", activebackground='black', font=("URW Chancery L", 15)).pack()


    #Botones menu principal.
    botonBienvenido6=Frame(root)
    botonBienvenido6.pack(fill=BOTH, expand=YES)
    botonBienvenido6.place(x=470, y=400)
    Button(botonBienvenido6, highlightbackground="black", 
        command=lambda:[equipo()], 
        width=17, height=1, text="Backdoor", foreground='red', activeforeground='orange', 
        cursor="fleur", justify="center", bd=0,  relief="raised", overrelief="sunken", 
        background="black", activebackground="black", font=("URW Chancery L", 13)).pack()

    botonBienvenido5=Frame(root)
    botonBienvenido5.pack(fill=BOTH, expand=NO)
    botonBienvenido5.place(x=470, y=350)
    Button(botonBienvenido5, highlightbackground="black", 
        command=lambda:[menu_distros(), botonBienvenido6.destroy(), botonBienvenido5.destroy(), botonBienvenido4.destroy(), botonBienvenido3.destroy(), botonBienvenido2.destroy(), botonBienvenido1.destroy()], 
        width=17, height=1, text="Distribuciones", foreground='red', activeforeground='orange', cursor="fleur", 
        justify="center", bd=0,  relief="raised", overrelief="sunken", background="black", 
        activebackground="black", font=("URW Chancery L", 13)).pack()

    botonBienvenido4=Frame(root)
    botonBienvenido4.pack(fill=BOTH, expand=YES)
    botonBienvenido4.place(x=470, y=300)
    Button(botonBienvenido4, highlightbackground="black", command=lambda:[herramientas()], width=17, 
        height=1, text="Herramientas", foreground='red', activeforeground='orange', cursor="fleur", 
        justify="center", bd=0,  relief="raised", overrelief="sunken", background="black", 
        activebackground="black", font=("URW Chancery L", 13)).pack()

    botonBienvenido3=Frame(root)
    botonBienvenido3.pack(fill=BOTH, expand=YES)
    botonBienvenido3.place(x=470, y=250)
    Button(botonBienvenido3, highlightbackground="black", command=lambda:[codigo_open()], width=17, height=1, 
        text="Código Abierto", foreground='red', activeforeground='orange', cursor="fleur", justify="center", 
        bd=0,  relief="raised", overrelief="sunken", background="black", activebackground="black", 
        font=("URW Chancery L", 13)).pack()

    botonBienvenido2=Frame(root)
    botonBienvenido2.pack(fill=BOTH, expand=YES)
    botonBienvenido2.place(x=470, y=200)
    Button(botonBienvenido2, highlightbackground="black", 
        command=lambda:[soflibre_desp(), botonBienvenido6.destroy(), botonBienvenido5.destroy(), botonBienvenido4.destroy(), botonBienvenido3.destroy(), botonBienvenido2.destroy(), botonBienvenido1.destroy()], 
        width=17, height=1, text="Software Libre", foreground='red', activeforeground='orange', 
        cursor="fleur", justify="center", bd=0,  relief="raised", overrelief="sunken", 
        background="black", activebackground="black", font=("URW Chancery L", 13)).pack()

    botonBienvenido1=Frame(root)
    botonBienvenido1.pack(fill=BOTH, expand=YES)
    botonBienvenido1.place(x=470, y=150)
    Button(botonBienvenido1, highlightbackground="black", 
        command=lambda:[offshell_desplegable(), botonBienvenido6.destroy(), botonBienvenido5.destroy(), botonBienvenido4.destroy(), botonBienvenido3.destroy(), botonBienvenido2.destroy(), botonBienvenido1.destroy()], 
        width=17, height=1, text="OffShell System", foreground='red', activeforeground='orange', cursor="fleur", 
        justify="center", bd=0,  relief="raised", overrelief="sunken", background="black", 
        activebackground="black", font=("URW Chancery L", 13)).pack()

    pass

def herramientas():

    botonBienvenido=Frame(root, width=1024, height=1024)
    botonBienvenido.pack(fill=BOTH, expand=YES)
    botonBienvenido.place(x=0, y=0)
    Button(botonBienvenido, image=imagen_fondo1, cursor="heart", justify="center", bd=0, 
        relief="raised", background="Black", activebackground='black', 
        font=("URW Chancery L", 17)).pack()

    #
    
    boton_distro4=Frame(root)
    boton_distro4.pack(fill=BOTH, expand=YES)
    boton_distro4.place(x=230, y=150)
    Button(boton_distro4, highlightbackground="black", 
        command=lambda:[educacion_herr()], 
        width=17, height=1, 
        text="Software Cientifíco", foreground='red', activeforeground='orange', cursor="fleur", 
        justify="center", bd=0,  relief="raised", overrelief="sunken", background="black", 
        activebackground="black", font=("URW Chancery L", 17)).pack()


    #
    
    boton_distro5=Frame(root)
    boton_distro5.pack(fill=BOTH, expand=YES)
    boton_distro5.place(x=9, y=150)
    Button(boton_distro5, highlightbackground="black", command=lambda:[bloqueado()], 
        width=17, height=1, text="Accesorios", foreground='red', activeforeground='orange', 
        cursor="fleur", justify="center", bd=0,  relief="raised", overrelief="sunken", 
        background="black", activebackground="black", font=("URW Chancery L", 17)).pack()


    #
    
    boton_distro6=Frame(root)
    boton_distro6.pack(fill=BOTH, expand=YES)
    boton_distro6.place(x=230, y=350)
    Button(boton_distro6, highlightbackground="black", command=lambda:[bloqueado()], width=17, height=1, 
        text="Hacking Ético", foreground='orange', activeforeground='red', cursor="fleur", 
        justify="center", bd=0,  relief="raised", overrelief="sunken", background="black", 
        activebackground="black", font=("URW Chancery L", 15)).pack()


    #
    
    boton_distro7=Frame(root)
    boton_distro7.pack(fill=BOTH, expand=YES)
    boton_distro7.place(x=9, y=220)
    Button(boton_distro7, highlightbackground="black", command=lambda:[bloqueado()], width=17, height=1, 
        text="Multimedia", foreground='red', activeforeground='orange', cursor="fleur", 
        justify="center", bd=0,  relief="raised", overrelief="sunken", background="black", 
        activebackground="black", font=("URW Chancery L", 17)).pack()


    #
    
    boton_distro8=Frame(root)
    boton_distro8.pack(fill=BOTH, expand=YES)
    boton_distro8.place(x=6, y=350)
    Button(boton_distro8, highlightbackground="black", command=lambda:[bloqueado()], width=17, height=1, 
        text="Programación", foreground='orange', activeforeground='red', cursor="fleur", 
        justify="center", bd=0,  relief="raised", overrelief="sunken", background="black", 
        activebackground="black", font=("URW Chancery L", 15)).pack()


    #
    
    boton_distro9=Frame(root)
    boton_distro9.pack(fill=BOTH, expand=YES)
    boton_distro9.place(x=230, y=220)
    Button(boton_distro9, highlightbackground="black", command=lambda:[bloqueado()], 
        width=17, height=1, text="Sonido", foreground='red', activeforeground='orange', 
        cursor="fleur", justify="center", bd=0,  relief="raised", overrelief="sunken", 
        background="black", activebackground="black", font=("URW Chancery L", 17)).pack()

    #
    
    boton_distro10=Frame(root)
    boton_distro10.pack(fill=BOTH, expand=YES)
    boton_distro10.place(x=700, y=150)
    Button(boton_distro10, highlightbackground="black", command=lambda:[bloqueado()], width=17, height=1, 
        text="Gráficos", foreground='red', activeforeground='orange', cursor="fleur", 
        justify="center", bd=0,  relief="raised", overrelief="sunken", background="black", 
        activebackground="black", font=("URW Chancery L", 17)).pack()


    #
    
    boton_distro10=Frame(root)
    boton_distro10.pack(fill=BOTH, expand=YES)
    boton_distro10.place(x=700, y=204)
    Button(boton_distro10, highlightbackground="black", command=lambda:[bloqueado()], width=17, height=1, 
        text="Oficina", foreground='red', activeforeground='orange', cursor="fleur", 
        justify="center", bd=0,  relief="raised", overrelief="sunken", background="black", 
        activebackground="black", font=("URW Chancery L", 17)).pack()

    #
    
    boton_distro11=Frame(root)
    boton_distro11.pack(fill=BOTH, expand=YES)
    boton_distro11.place(x=904, y=150)
    Button(boton_distro11, highlightbackground="black", command=lambda:[bloqueado()], width=17, height=1, 
        text="Internet", foreground='red', activeforeground='orange', cursor="fleur", 
        justify="center", bd=0,  relief="raised", overrelief="sunken", background="black", 
        activebackground="black", font=("URW Chancery L", 17)).pack()


    #
    
    boton_distro11=Frame(root)
    boton_distro11.pack(fill=BOTH, expand=YES)
    boton_distro11.place(x=904, y=204)
    Button(boton_distro11, highlightbackground="black", command=lambda:[bloqueado()], width=17, height=1, 
        text="Sistema", foreground='red', activeforeground='orange', cursor="fleur", justify="center", 
        bd=0,  relief="raised", overrelief="sunken", background="black", activebackground="black", 
        font=("URW Chancery L", 17)).pack()

    #
    
    boton_distro12=Frame(root)
    boton_distro12.pack(fill=BOTH, expand=YES)
    boton_distro12.place(x=6, y=420)
    Button(boton_distro12, highlightbackground="black", command=lambda:[bloqueado()], width=17, height=1, 
        text="Entornos Escritorio", foreground='orange', activeforeground='Red', cursor="fleur", 
        justify="center", bd=0,  relief="raised", overrelief="sunken", background="black", 
        activebackground="black", font=("URW Chancery L", 15)).pack()

    #
    
    boton_distro13=Frame(root)
    boton_distro13.pack(fill=BOTH, expand=YES)
    boton_distro13.place(x=230, y=420)
    Button(boton_distro13, highlightbackground="black", command=lambda:[bloqueado()], width=17, height=1, 
        text="Apariencia", foreground='orange', activeforeground='Red', cursor="fleur", 
        justify="center", bd=0,  relief="raised", overrelief="sunken", background="black", 
        activebackground="black", font=("URW Chancery L", 15)).pack()

    #
    
    boton_distro10=Frame(root)
    boton_distro10.pack(fill=BOTH, expand=YES)
    boton_distro10.place(x=700, y=420)
    Button(boton_distro10, highlightbackground="black", command=lambda:[bloqueado()], width=17, height=1, 
        text="Privacidad", foreground='orange', activeforeground='Red', cursor="fleur", justify="center", 
        bd=0,  relief="raised", overrelief="sunken", background="black", activebackground="black", 
        font=("URW Chancery L", 15)).pack()

    #
    
    boton_distro10=Frame(root)
    boton_distro10.pack(fill=BOTH, expand=YES)
    boton_distro10.place(x=700, y=344)
    Button(boton_distro10, highlightbackground="black", command=lambda:[bloqueado()], width=17, height=1, 
        text="IRC / Chat", foreground='orange', activeforeground='Red', cursor="fleur", 
        justify="center", bd=0,  relief="raised", overrelief="sunken", background="black", 
        activebackground="black", font=("URW Chancery L", 15)).pack()

    #
    
    boton_distro10=Frame(root)
    boton_distro10.pack(fill=BOTH, expand=YES)
    boton_distro10.place(x=905, y=420)
    Button(boton_distro10, highlightbackground="black", command=lambda:[bloqueado()], 
        width=17, height=1, text="Ver Mas...", foreground='white', activeforeground='Red', 
        cursor="fleur", justify="center", bd=0,  relief="raised", overrelief="sunken", 
        background="black", activebackground="black", font=("URW Chancery L", 15)).pack()

    #
    
    boton_distro10=Frame(root)
    boton_distro10.pack(fill=BOTH, expand=YES)
    boton_distro10.place(x=905, y=344)
    Button(boton_distro10, highlightbackground="black", command=lambda:[bloqueado()], 
        width=17, height=1, text="Gestores Correo", foreground='orange', 
        activeforeground='Red', cursor="fleur", justify="center", bd=0,  
        relief="raised", overrelief="sunken", background="black", activebackground="black", 
        font=("URW Chancery L", 15)).pack()




    #Cerrar Distribuciones.
    boton_cerrar_distros=Frame(root)
    boton_cerrar_distros.pack(fill=BOTH, expand=YES)
    boton_cerrar_distros.place(x=470, y=200)
    Button(boton_cerrar_distros, highlightbackground="black", command=lambda:[menu_principal()], 
        width=15, height=1, text="Menú Principal", foreground='red', activeforeground='orange', 
        cursor="fleur", justify="center", bd=0,  relief="raised", overrelief="sunken", 
        background="black", activebackground="black", font=("URW Chancery L", 15)).pack()

    #Menu Distribuciones.
    boton_cerrar_distros=Frame(root)
    boton_cerrar_distros.pack(fill=BOTH, expand=YES)
    boton_cerrar_distros.place(x=470, y=250)
    Button(boton_cerrar_distros, highlightbackground="black", command=lambda:[menu_distros()], 
        width=15, height=1, text="Menú Distribuciones", foreground='red', activeforeground='orange', 
        cursor="fleur", justify="center", bd=0,  relief="raised", overrelief="sunken", 
        background="black", activebackground="black", font=("URW Chancery L", 15)).pack()


    #Herramientas Logo.
    boton_img_ligeros=Frame(root)
    boton_img_ligeros.place(x=445, y=540)
    Button(boton_img_ligeros, highlightbackground="black", image=herramientas_logo, cursor='fleur', 
        justify='center', bd=0, background="black", activebackground="black").pack()

    boton_ligeros=Frame(root)
    boton_ligeros.pack(fill=BOTH, expand=YES)
    boton_ligeros.place(x=530, y=520)
    Button(boton_ligeros, highlightbackground="black", width=14, height=1, 
        text="HERRAMIENTAS", foreground='red', activeforeground='DarkRed', cursor="fleur", 
        justify="center", bd=0,  relief="raised", overrelief="sunken", background="black", 
        activebackground="black", font=("URW Chancery L", 15)).pack()


    pass



def educacion_herr():


    botonBienvenido=Frame(root, width=1024, height=1024)
    botonBienvenido.pack(fill=BOTH, expand=YES)
    botonBienvenido.place(x=0, y=0)
    Button(botonBienvenido, image=imagen_fondo1, cursor="heart", justify="center", bd=0, relief="raised", 
        background="Black", activebackground='black', font=("URW Chancery L", 15)).pack()


    #GCompris
    boton_img_distro1=Frame(root)
    boton_img_distro1.place(x=55, y=12)
    Button(boton_img_distro1, highlightbackground="Red", image=gcompris_logo, 
        command=lambda:[webbrowser.open_new_tab("https://gcompris.net/index-es.html")], 
        cursor='fleur', justify='center', bd=0,  relief="raised", overrelief="raised", 
        activebackground="DarkRed").pack()

    boton_distro1=Frame(root)
    boton_distro1.pack(fill=BOTH, expand=YES)
    boton_distro1.place(x=6, y=64)
    Button(boton_distro1, highlightbackground="black", 
        command=lambda:[webbrowser.open_new_tab("https://gcompris.net/index-es.html")], 
        width=17, height=2, text="GCompris\nJuegos Ciencia", foreground='white', activeforeground='Red', 
        cursor="fleur", justify="center", bd=0,  relief="raised", overrelief="sunken", 
        background="black", activebackground="black", font=("URW Chancery L", 15)).pack()

    #Kig Geometría
    boton_img_distro2=Frame(root)
    boton_img_distro2.place(x=205, y=12)
    Button(boton_img_distro2, highlightbackground="Red", image=kig_logo, 
        command=lambda:[webbrowser.open_new_tab("https://kde.org/applications/education/org.kde.kig")], 
        cursor='fleur', 
        justify='center', bd=0,  relief="raised", overrelief="raised", activebackground="DarkRed").pack()

    boton_distro2=Frame(root)
    boton_distro2.pack(fill=BOTH, expand=YES)
    boton_distro2.place(x=155, y=64)
    Button(boton_distro2, highlightbackground="black", 
        command=lambda:[webbrowser.open_new_tab("https://kde.org/applications/education/org.kde.kig")], 
        width=17, height=1, 
        text="Kig Geometría", foreground='white', activeforeground='Red', cursor="fleur", 
        justify="center", bd=0,  relief="raised", overrelief="sunken", background="black", 
        activebackground="black", font=("URW Chancery L", 15)).pack()

    #Grass Geografía
    boton_img_distro3=Frame(root)
    boton_img_distro3.place(x=355, y=12)
    Button(boton_img_distro3, highlightbackground="Red", image=grass_logo, 
        command=lambda:[webbrowser.open_new_tab("https://grass.osgeo.org/")], cursor='fleur', 
        justify='center', bd=0,  relief="raised", overrelief="raised", activebackground="DarkRed").pack()

    boton_distro3=Frame(root)
    boton_distro3.pack(fill=BOTH, expand=YES)
    boton_distro3.place(x=304, y=64)
    Button(boton_distro3, highlightbackground="black", 
        command=lambda:[webbrowser.open_new_tab("https://grass.osgeo.org/")], width=17, height=1, 
        text="Grass Geografía", foreground='white', activeforeground='Red', cursor="fleur", 
        justify="center", bd=0,  relief="raised", overrelief="sunken", background="black", 
        activebackground="black", font=("URW Chancery L", 15)).pack()

    #Molecular WorkBrench
    boton_img_distro4=Frame(root)
    boton_img_distro4.place(x=505, y=12)
    Button(boton_img_distro4, highlightbackground="Red", image=molecular1_logo, 
        command=lambda:[webbrowser.open_new_tab("http://mw.concord.org/modeler/")], cursor='fleur', 
        justify='center', bd=0, relief="raised", overrelief="raised", activebackground="DarkRed").pack()

    boton_distro4=Frame(root)
    boton_distro4.pack(fill=BOTH, expand=YES)
    boton_distro4.place(x=454, y=64)
    Button(boton_distro4, highlightbackground="black", 
        command=lambda:[webbrowser.open_new_tab("http://mw.concord.org/modeler/")], 
        width=17, height=1, text="Taller Molecular", foreground='white', activeforeground='Red', 
        cursor="fleur", justify="center", bd=0,  relief="raised", overrelief="sunken", 
        background="black", activebackground="black", font=("URW Chancery L", 15)).pack()

    #Phet
    boton_img_distro5=Frame(root)
    boton_img_distro5.place(x=655, y=12)
    Button(boton_img_distro5, highlightbackground="Red", image=phet_logo, 
        command=lambda:[webbrowser.open_new_tab("https://phet.colorado.edu/es/")], cursor='fleur', 
        justify='center', bd=0, relief="raised", overrelief="raised", activebackground="DarkRed").pack()

    boton_distro5=Frame(root)
    boton_distro5.pack(fill=BOTH, expand=YES)
    boton_distro5.place(x=605, y=64)
    Button(boton_distro5, highlightbackground="black", 
        command=lambda:[webbrowser.open_new_tab("https://phet.colorado.edu/es/")], width=17, height=1, 
        text="Ciencia-Mates", foreground='white', activeforeground='Red', cursor="fleur", 
        justify="center", bd=0,  relief="raised", overrelief="sunken", background="black", 
        activebackground="black", font=("URW Chancery L", 15)).pack()

    #Mars Simulation
    boton_img_distro6=Frame(root)
    boton_img_distro6.place(x=805, y=12)
    Button(boton_img_distro6, highlightbackground="Red", image=martesi_logo, 
        command=lambda:[webbrowser.open_new_tab("https://mars-sim.sourceforge.io/")], 
        cursor='fleur', justify='center', bd=0, relief="raised", overrelief="raised", 
        activebackground="DarkRed").pack()

    boton_distro6=Frame(root)
    boton_distro6.pack(fill=BOTH, expand=YES)
    boton_distro6.place(x=754, y=64)
    Button(boton_distro6, highlightbackground="black", 
        command=lambda:[webbrowser.open_new_tab("https://mars-sim.sourceforge.io/")], width=17, height=2, 
        text="Marte\nSimulación", foreground='white', activeforeground='Red', cursor="fleur", 
        justify="center", bd=0,  relief="raised", overrelief="sunken", background="black", 
        activebackground="black", font=("URW Chancery L", 15)).pack()

    #Microscópio Virtual
    boton_img_distro7=Frame(root)
    boton_img_distro7.place(x=955, y=12)
    Button(boton_img_distro7, highlightbackground="Red", image=microscopico_logo, 
        command=lambda:[webbrowser.open_new_tab("http://virtual.itg.uiuc.edu/")], 
        cursor='fleur', justify='center', bd=0, relief="raised", overrelief="raised", 
        activebackground="DarkRed").pack()

    boton_distro7=Frame(root)
    boton_distro7.pack(fill=BOTH, expand=YES)
    boton_distro7.place(x=904, y=64)
    Button(boton_distro7, highlightbackground="black", 
        command=lambda:[webbrowser.open_new_tab("http://virtual.itg.uiuc.edu/")], 
        width=17, height=2, text="Microscopio Virtual\nNASA", foreground='white', activeforeground='Red', 
        cursor="fleur", justify="center", bd=0,  relief="raised", overrelief="sunken", 
        background="black", activebackground="black", font=("URW Chancery L", 15)).pack()


    #Laboratorio Química
    boton_img_distro8=Frame(root)
    boton_img_distro8.place(x=55, y=152)
    Button(boton_img_distro8, highlightbackground="Red", image=quimica1_logo, 
        command=lambda:[webbrowser.open_new_tab("http://chemcollective.org/vlabs")], 
        cursor='fleur', justify='center', bd=0, relief="raised", overrelief="raised", 
        activebackground="DarkRed").pack()

    boton_distro8=Frame(root)
    boton_distro8.pack(fill=BOTH, expand=YES)
    boton_distro8.place(x=6, y=204)
    Button(boton_distro8, highlightbackground="black", 
        command=lambda:[webbrowser.open_new_tab("http://chemcollective.org/vlabs")], 
        width=17, height=2, text="Laboratorio\nQuímica", foreground='white', activeforeground='Red', 
        cursor="fleur", justify="center", bd=0,  relief="raised", overrelief="sunken", 
        background="black", activebackground="black", font=("URW Chancery L", 15)).pack()


    #Parley Vocabulario
    boton_img_distro9=Frame(root)
    boton_img_distro9.place(x=205, y=152)
    Button(boton_img_distro9, highlightbackground="red", image=parley_logo, 
        command=lambda:[webbrowser.open_new_tab("https://kde.org/applications/education/org.kde.parley")], 
        cursor='fleur', justify='center', bd=0, relief="raised", overrelief="raised", 
        activebackground="DarkRed").pack()

    boton_distro9=Frame(root)
    boton_distro9.pack(fill=BOTH, expand=YES)
    boton_distro9.place(x=155, y=204)
    Button(boton_distro9, highlightbackground="black", command=lambda:[webbrowser.open_new_tab("https://kde.org/applications/education/org.kde.parley")], 
        width=17, height=2, text="Parley Clases\nVocabulario", foreground='white', activeforeground='Red', 
        cursor="fleur", justify="center", bd=0,  relief="raised", overrelief="sunken", 
        background="black", activebackground="black", font=("URW Chancery L", 15)).pack()

    #KTouch teclado
    boton_img_distro10=Frame(root)
    boton_img_distro10.place(x=805, y=152)
    Button(boton_img_distro10, highlightbackground="red", 
        image=ktouch_logo, command=lambda:[webbrowser.open_new_tab("https://kde.org/applications/education/org.kde.ktouch")], 
        cursor='fleur', justify='center', bd=0, relief="raised", overrelief="raised", 
        activebackground="DarkRed").pack()

    boton_distro10=Frame(root)
    boton_distro10.pack(fill=BOTH, expand=YES)
    boton_distro10.place(x=755, y=204)
    Button(boton_distro10, highlightbackground="black", 
        command=lambda:[webbrowser.open_new_tab("https://kde.org/applications/education/org.kde.ktouch")], 
        width=17, height=2, 
        text="Entrenador\nMecanografía", foreground='white', activeforeground='Red', cursor="fleur", justify="center", 
        bd=0,  relief="raised", overrelief="sunken", background="black", activebackground="black", 
        font=("URW Chancery L", 15)).pack()

    #Mcstas Neutrones
    boton_img_distro11=Frame(root)
    boton_img_distro11.place(x=955, y=152)
    Button(boton_img_distro11, highlightbackground="red", image=mcstas_logo, 
        command=lambda:[webbrowser.open_new_tab("http://www.mcstas.org/")], cursor='fleur', 
        justify='center', bd=0, relief="raised", overrelief="raised", activebackground="DarkRed").pack()

    boton_distro11=Frame(root)
    boton_distro11.pack(fill=BOTH, expand=YES)
    boton_distro11.place(x=904, y=204)
    Button(boton_distro11, highlightbackground="black", 
        command=lambda:[webbrowser.open_new_tab("http://www.mcstas.org/")], width=17, height=2, 
        text="MCstas Dispersión\nNeutrones", foreground='white', activeforeground='Red', cursor="fleur", 
        justify="center", bd=0,  relief="raised", overrelief="sunken", background="black", 
        activebackground="black", font=("URW Chancery L", 15)).pack()

    #Root CERN FIsica
    boton_img_distro12=Frame(root)
    boton_img_distro12.place(x=55, y=294)
    Button(boton_img_distro12, highlightbackground="Red", image=root_logo, 
        command=lambda:[webbrowser.open_new_tab("https://root.cern.ch/")], cursor='fleur', 
        justify='center', bd=0, relief="raised", overrelief="raised", activebackground="DarkRed").pack()

    boton_distro12=Frame(root)
    boton_distro12.pack(fill=BOTH, expand=YES)
    boton_distro12.place(x=6, y=344)
    Button(boton_distro12, highlightbackground="black", 
        command=lambda:[webbrowser.open_new_tab("https://root.cern.ch/")], width=17, height=2, 
        text="Análisis Datos\nHerramientas", foreground='white', activeforeground='Red', cursor="fleur", 
        justify="center", bd=0,  relief="raised", overrelief="sunken", background="black", 
        activebackground="black", font=("URW Chancery L", 15)).pack()

    #JaxoDraw
    boton_img_distro13=Frame(root)
    boton_img_distro13.place(x=205, y=294)
    Button(boton_img_distro13, highlightbackground="Red", image=jaxo_logo, 
        command=lambda:[webbrowser.open_new_tab("http://jaxodraw.sourceforge.net/index.html")], cursor='fleur', 
        justify='center', bd=0, relief="raised", overrelief="raised", background='black', 
        activebackground="DarkRed").pack()

    boton_distro13=Frame(root)
    boton_distro13.pack(fill=BOTH, expand=YES)
    boton_distro13.place(x=155, y=344)
    Button(boton_distro13, highlightbackground="black", 
        command=lambda:[webbrowser.open_new_tab("http://jaxodraw.sourceforge.net/index.html")], width=17, height=2, 
        text="Diagramas\nFeynman", foreground='white', activeforeground='Red', cursor="fleur", 
        justify="center", bd=0,  relief="raised", overrelief="sunken", background="black", 
        activebackground="black", font=("URW Chancery L", 15)).pack()

    #lightspeed
    boton_img_distro14=Frame(root)
    boton_img_distro14.place(x=805, y=294)
    Button(boton_img_distro14, highlightbackground="red", image=lightspeed_logo, 
        command=lambda:[webbrowser.open_new_tab("http://lightspeed.sourceforge.net/")], cursor='fleur', 
        justify='center', bd=0, relief="raised", overrelief="raised", background="black", 
        activebackground="DarkRed").pack()

    boton_distro10=Frame(root)
    boton_distro10.pack(fill=BOTH, expand=YES)
    boton_distro10.place(x=755, y=344)
    Button(boton_distro10, highlightbackground="black", 
        command=lambda:[webbrowser.open_new_tab("http://lightspeed.sourceforge.net/")], width=17, height=2, 
        text="Relatividad\nEspecial", foreground='white', activeforeground='Red', cursor="fleur", 
        justify="center", bd=0,  relief="raised", overrelief="sunken", background="black", 
        activebackground="black", font=("URW Chancery L", 15)).pack()

    #Emboss
    boton_img_distro14=Frame(root)
    boton_img_distro14.place(x=955, y=294)
    Button(boton_img_distro14, highlightbackground="red", image=emboss_logo, 
        command=lambda:[webbrowser.open_new_tab("http://emboss.sourceforge.net/download/")], cursor='fleur', 
        justify='center', bd=0, relief="raised", overrelief="raised", background="black", 
        activebackground="DarkRed").pack()

    boton_distro10=Frame(root)
    boton_distro10.pack(fill=BOTH, expand=YES)
    boton_distro10.place(x=905, y=344)
    Button(boton_distro10, highlightbackground="black", 
        command=lambda:[webbrowser.open_new_tab("http://emboss.sourceforge.net/download/")], 
        text="Biología\nMolecular", foreground='white', activeforeground='Red', cursor="fleur", 
        justify="center", width=17, height=2,
        bd=0,  relief="raised", overrelief="sunken", background="black", activebackground="black", 
        font=("URW Chancery L", 15)).pack()




    #Cerrar Distribuciones.
    boton_cerrar_distros=Frame(root)
    boton_cerrar_distros.pack(fill=BOTH, expand=YES)
    boton_cerrar_distros.place(x=470, y=200)
    Button(boton_cerrar_distros, highlightbackground="black", command=lambda:[menu_principal()], width=15, height=1, text="Menú Principal", foreground='red', activeforeground='DarkRed', cursor="fleur", justify="center", bd=0,  relief="raised", overrelief="sunken", background="black", activebackground="black", font=("URW Chancery L", 15)).pack()

    #Menu Distribuciones.
    boton_cerrar_distros=Frame(root)
    boton_cerrar_distros.pack(fill=BOTH, expand=YES)
    boton_cerrar_distros.place(x=470, y=250)
    Button(boton_cerrar_distros, highlightbackground="black", command=lambda:[menu_distros()], width=15, height=1, text="Menú Distribuciones", foreground='red', activeforeground='DarkRed', cursor="fleur", justify="center", bd=0,  relief="raised", overrelief="sunken", background="black", activebackground="black", font=("URW Chancery L", 15)).pack()


    #Escritorio OS Logo.
    boton_img_ligeros=Frame(root)
    boton_img_ligeros.place(x=420, y=530)
    Button(boton_img_ligeros, highlightbackground="black", image=ciencia_logo, cursor='fleur', justify='center', bd=0, background="black", activebackground="black").pack()

    boton_ligeros=Frame(root)
    boton_ligeros.pack(fill=BOTH, expand=YES)
    boton_ligeros.place(x=550, y=550)
    Button(boton_ligeros, highlightbackground="black", width=14, height=1, text="Software Ciencia", foreground='white', activeforeground='Red', cursor="fleur", justify="center", bd=0,  relief="raised", overrelief="sunken", background="black", activebackground="black", font=("URW Chancery L", 15)).pack()

    pass


def equipo():
    botonBienvenido=Frame(root, width=1024, height=1024)
    botonBienvenido.pack(fill=BOTH, expand=YES)
    botonBienvenido.place(x=0, y=0)
    Button(botonBienvenido, image=imagen_fondo1, cursor="heart", justify="center", bd=0, relief="raised",
                 background="Black", activebackground='black', font=("URW Chancery L", 15)).pack()


    botonBienvenido1=Frame(root)
    botonBienvenido1.pack(fill=BOTH, expand=YES)
    botonBienvenido1.place(x=470, y=360)
    Button(botonBienvenido1, highlightbackground="black", 
        command=lambda:[old()], 
        width=17, height=1, text="37373", foreground='red', activeforeground='orange', cursor="fleur", 
        justify="center", bd=0,  relief="raised", overrelief="sunken", background="black", 
        activebackground="black", font=("URW Chancery L", 13)).pack()


    boton_menu2=Frame(root)
    boton_menu2.pack(fill=BOTH, expand=YES)
    boton_menu2.place(x=477, y=200)
    Button(boton_menu2, command=lambda:[], 
        highlightbackground="black", image=panda_logo, foreground='red', activeforeground='black',
         cursor="fleur", justify="center", bd=0,  relief="raised", background="black", activebackground="black",
          font=("URW Chancery L", 16)).pack()




    pass


def bloqueado():

    root = Tk()
    root.title("··· Contenido en Desarrollo ···")
    root.geometry("450x150+397+300")
    root.resizable(width=False, height=False)
    root.config(bg='black')

    label1=Label(root, text="Contenido en desarrollo.\nDisponible en próximas actualizaciones.",
                     font=("URW Chancery L", 17), foreground="Red", background="black").place(x=63, y=20)

    #
    
    boton_ejecutar=Frame(root)
    boton_ejecutar.pack(fill=BOTH, expand=YES)
    boton_ejecutar.place(x=100, y=90)
    Button(boton_ejecutar, highlightbackground="black", command=lambda:[root.destroy()], width=23, height=1,
                         text="Continuar Versión Actual", foreground='green', activeforeground='purple',
                          cursor="fleur", justify="center", bd=0,  relief="raised", overrelief="sunken",
                           background="black", activebackground="black", font=("URW Chancery L", 15)).pack()



    root.mainloop()

    pass


def old():
    botonBienvenido=Frame(root, width=1024, height=1024)
    botonBienvenido.pack(fill=BOTH, expand=YES)
    botonBienvenido.place(x=0, y=0)
    Button(botonBienvenido, image=imagen_fondo1, cursor="heart", justify="center", bd=0, relief="raised",
                 background="Black", activebackground='black', font=("URW Chancery L", 15)).pack()

    boton_menu2=Frame(root)
    boton_menu2.pack(fill=BOTH, expand=YES)
    boton_menu2.place(x=477, y=140)
    Button(boton_menu2, command=lambda:[], 
        highlightbackground="black", image=rob, foreground='red', activeforeground='black',
         cursor="fleur", justify="center", bd=0,  relief="raised", background="black", activebackground="black",
          font=("URW Chancery L", 16)).pack()


    pass











def video_intro():

    # Create a VideoCapture object and read from input file 
    cap = cv2.VideoCapture('intro_estrella.flv') 
    
    # Check if camera opened successfully 
    if (cap.isOpened()== False):  
      print("Error opening video  file") 
   
    # Read until video is completed 
    while(cap.isOpened()): 
      
      # Capture frame-by-frame 
      ret, frame = cap.read() 
      if ret == True: 
   
            # Display the resulting frame 
            cv2.imshow('Pulsa Q/Espacio para salir', frame) 
            
            # Press Q on keyboard to  exit 
            if cv2.waitKey(25) & 0xFF == ord('q'): 
             break
            if cv2.waitKey(25) & 0xFF == ord(' '): 
             break
            
      # Break the loop 
      else:  
        break
   
    # When everything done, release  
    # the video capture object 
    cap.release() 
    
    # Closes all the frames 
    cv2.destroyAllWindows()

def entrar_pant_completa():
    root.attributes("-fullscreen", True)

def salir_pant_completa():
    root.attributes("-fullscreen", False) 

#Ventana Aviso Primera Instalación.

root_avs = Tk()
root_avs.title("✰ OffShell System ✰")
root_avs.geometry("600x600+340+150")
root_avs.resizable(width=False, height=False)
root_avs.config(bg='black')

root_avs.tk.call('wm', 'iconphoto', root_avs._w, tk.PhotoImage(file='primate.gif'))


#Gato Inicio
gato_logo=PhotoImage(file="gato.gif")

boton_gato=Frame(root_avs)
boton_gato.pack(fill=BOTH, expand=YES)
boton_gato.place(x=0, y=100)
Button(boton_gato, image=gato_logo, cursor="heart", justify="center", bd=0, relief="raised", 
                 highlightbackground="black", 
                 background="Black", activebackground='black', font=("URW Chancery L", 15)).pack()
#Primate Logo
offshell_logo=PhotoImage(file="offshell.gif")

boton_offlogo=Frame(root_avs)
boton_offlogo.pack(fill=BOTH, expand=YES)
boton_offlogo.place(x=225, y=35)
Button(boton_offlogo, image=offshell_logo, cursor="heart", justify="center", bd=0, relief="raised", 
                 highlightbackground="black", 
                 background="Black", activebackground='black', font=("URW Chancery L", 15)).pack()


boton_ejecutar=Frame(root_avs)
boton_ejecutar.pack(fill=BOTH, expand=YES)
boton_ejecutar.place(x=98, y=220)
Button(boton_ejecutar, highlightbackground="black", command=lambda:[root_avs.destroy()], width=9, height=1,
                 text="Biblioteca", foreground='orange', activeforeground='red', cursor="fleur",
                  justify="center", bd=0,  relief="raised", overrelief="sunken", background="black",
                   activebackground="black", font=("URW Chancery L", 15)).pack()

boton_ejecutar2=Frame(root_avs)
boton_ejecutar2.pack(fill=BOTH, expand=YES)
boton_ejecutar2.place(x=400, y=220)
Button(boton_ejecutar2, highlightbackground="black", command=lambda:[webbrowser.open_new_tab("https://discord.gg/ShKjFfe")], width=9, height=1,
                 text="Soporte Online", foreground='orange', activeforeground='green', cursor="fleur",
                  justify="center", bd=0,  relief="raised", overrelief="sunken", background="black",
                   activebackground="black", font=("URW Chancery L", 15)).pack()



root_avs.mainloop()

#Ventana Principal Grande
root = Tk()
root.title("✰ OffShell System ✰")
root.geometry("1124x650+75+100")
root.resizable(width=False, height=False)
root.config(bg='black')

root.tk.call('wm', 'iconphoto', root._w, tk.PhotoImage(file='primate.gif'))

#Barra MenuBar.
door_door=tk.StringVar()
barramenu=Menu(root, relief=RAISED, cursor="heart", activebackground='Black', foreground='white',
                     activeforeground='Red', activeborderwidth=1, bg='Black', bd=1)


root.config(menu=barramenu, width=300, height=300, cursor="heart")


archMenu=Menu(barramenu, tearoff=0)


barramenu.add_cascade(label="Menú", menu=archMenu, font=("URW Chancery L", 11))



archMenu.add_command(label="Menú Principal", command=lambda:[menu_principal(), boton_menu.destroy()],
                         font=("URW Chancery L", 13), background='black', activebackground='DarkRed',
                          foreground='red', activeforeground='white')


archMenu.add_command(label="OffShell System", command=lambda:[offshell_desplegable()], font=("URW Chancery L", 13),
                         background='black', activebackground='DarkRed', foreground='Red', activeforeground='white')


archMenu.add_command(label="Software Libre", command=lambda:[soflibre_desp()], font=("URW Chancery L", 13),
                         background='black', activebackground='DarkRed', foreground='red', activeforeground='white')


archMenu.add_command(label="Código Abierto", command=lambda:[codigo_open()], font=("URW Chancery L", 13),
                         background='black', activebackground='DarkRed', foreground='red', activeforeground='white')


archMenu.add_command(label="Herramientas", command=lambda:[herramientas()], font=("URW Chancery L", 13),
                         background='black', activebackground='DarkRed', foreground='red', activeforeground='white')


archMenu.add_command(label="Distribuciones OS", command=lambda:[menu_distros()], font=("URW Chancery L", 13),
                         background='black', activebackground='DarkRed', foreground='red', activeforeground='white')


archMenu.add_command(label="Licencia y Autoría", 
    command=lambda:[webbrowser.open_new_tab("https://creativecommons.org/licenses/by-nc-sa/4.0/")], 
    font=("URW Chancery L", 13), background='black', activebackground='DarkRed', foreground='red', 
    activeforeground='white')



# IMAGENES
imagen_fondo1 = PhotoImage(file="puerta_roja.gif")
imagen_fondo3=PhotoImage(file="fondo3.gif")
primate_logo=PhotoImage(file="primate.gif")
fun_logo=PhotoImage(file="alex.gif")
mapa_libre=PhotoImage(file="mapa_software_libre.gif")
mapa_ampliado=PhotoImage(file="Mapa_grande.gif")
herramientas_logo=PhotoImage(file="herramientas_logo.gif")
gato_logo=PhotoImage(file="gato.gif")
desarrollo_logo=PhotoImage(file="desarrollo.gif")

door=PhotoImage(file="door.gif")
ciencia_logo=PhotoImage(file="ciencia_log.gif")
panda_logo=PhotoImage(file="panda.gif")
rob=PhotoImage(file="rob.gif")
probar_logo=PhotoImage(file="probar.gif")

codigo_abierto=PhotoImage(file="opensource.gif")
codigo_grande=PhotoImage(file="open_grande.gif")

gcompris_logo=PhotoImage(file=("GComprisLogo.gif"))
kig_logo=PhotoImage(file=("kig_logo.gif"))
grass_logo=PhotoImage(file=("grass_logo.gif"))
molecular1_logo=PhotoImage(file=("molecularworkbench.gif"))
phet_logo=PhotoImage(file=("phet.gif"))
martesi_logo=PhotoImage(file=("marte.gif"))
microscopico_logo=PhotoImage(file=("microscopio.gif"))
quimica1_logo=PhotoImage(file=("quimica1.gif"))
parley_logo=PhotoImage(file=("parley.gif"))
ktouch_logo=PhotoImage(file=("ktouch.gif"))
mcstas_logo=PhotoImage(file=("mcstas.gif"))
root_logo=PhotoImage(file=("root.gif"))
jaxo_logo=PhotoImage(file=("jaxo.gif"))
lightspeed_logo=PhotoImage(file=("luz.gif"))
emboss_logo=PhotoImage(file=("emboss.gif"))




debian_logo=PhotoImage(file="debian_logo.gif")
ubuntu_logo=PhotoImage(file="ubuntu_logo.gif")
linuxmint_logo = PhotoImage(file="linuxmint_logo.gif")
elementary_logo=PhotoImage(file="elementary_logo.gif")
fedora_logo=PhotoImage(file="fedora_logo.gif")
manjaro_logo=PhotoImage(file="manjaro-logo.gif")
deepin_logo=PhotoImage(file="deepin_logo.gif")
peppermint_logo=PhotoImage(file="peppermint.gif")
bunsenlabs_logo=PhotoImage(file="bunsenlabs_logo.gif")
openbsd_logo=PhotoImage(file="opensbd_logo.gif")
servidores_logo=PhotoImage(file="servidores_logo.gif")
casa_logo=PhotoImage(file="casa_logo.gif")
redhat_logo=PhotoImage(file="redhat_logo.gif")
centos_logo=PhotoImage(file="centos_logo.gif")
suse_logo=PhotoImage(file="suse_logo.gif")
archlinux_logo=PhotoImage(file="archlinux.gif")
ubuntuserver_logo=PhotoImage(file="ubuntuserver_logo.gif")
fedoraserver_logo=PhotoImage(file="fedoraserver_logo.gif")
oraclecloud_logo=PhotoImage(file="oraclecloud_logo.gif")
zorin_logo=PhotoImage(file="zorin_logo.gif")
volver_logo=PhotoImage(file="volver_logo.gif")
mageia_logo=PhotoImage(file="mageia_logo.gif")
clear_logo=PhotoImage(file="clear_logo.gif")
arch_logo=PhotoImage(file="arch_logo.gif")
suse2_logo=PhotoImage(file="suse2_logo.gif")
mxlinux_logo=PhotoImage(file="mxlinux_logo.gif")
sabayon_logo=PhotoImage(file="sabayon_logo.gif")
opensuse_logo2=PhotoImage(file="opensuse_logo2.gif")
juego_logo=PhotoImage(file="juegos.gif")
ligero_logo=PhotoImage(file="pluma.gif")
bodi_logo=PhotoImage(file="bodi.gif")
puppy_logo=PhotoImage(file="puppy.gif")
linuxlite_logo=PhotoImage(file="linuxlite.gif")
lubuntu_logo=PhotoImage(file="lubuntu_logo.gif")
lxle_logo=PhotoImage(file="lxle.gif")
antix_logo=PhotoImage(file="antix_logo.gif")
tinycore_logo=PhotoImage(file="tinycore.gif")
xubuntu_logo=PhotoImage(file="xubuntu.gif")
steam_logo=PhotoImage(file="steam.gif")
supergamer_logo=PhotoImage(file="supergamer.gif")
linuxconsole_logo=PhotoImage(file="linuxconsole.gif")
manjarogame_logo=PhotoImage(file="manjarogame.gif")
lakka_logo=PhotoImage(file="lakka.gif")
solus_logo=PhotoImage(file="solus.gif")
fedoragames_logo=PhotoImage(file="fedoragames.gif")
gameover_logo=PhotoImage(file="gameover.gif")
ubuntugame_logo=PhotoImage(file="ubuntugame.gif")
gamedrift_logo=PhotoImage(file="gamedrift.gif")
servidores_logo2=PhotoImage(file="servidores.gif")
house_logo=PhotoImage(file="house.gif")
inicio_logo=PhotoImage(file="inicio_logo.gif")

dns_logo=PhotoImage(file="dns.gif")

#Imagen de Fondo.
botonBienvenido=Frame(root, width=1024, height=1024)
botonBienvenido.pack(fill=BOTH, expand=YES)
botonBienvenido.place(x=0, y=0)
Button(botonBienvenido, image=imagen_fondo1, cursor="heart", justify="center", bd=0, relief="raised",
                 background="Black", activebackground='black', font=("URW Chancery L", 15)).pack()


#Boton Inicio.
boton_menu=Frame(root)
boton_menu.pack(fill=BOTH, expand=YES)
boton_menu.place(x=483, y=220)
Button(boton_menu, highlightbackground="black", command=lambda:[menu_principal(), boton_menu.destroy()],
         width=12, height=2, text="Sección LS7\nBiblioteca Online", foreground='red', activeforeground='orange',
          cursor="fleur", justify="center", bd=0,  relief="raised", overrelief="sunken", background="black",
           activebackground="black", font=("URW Chancery L", 16)).pack()

#Imagen logo OffShell System
boton_menu2=Frame(root)
boton_menu2.pack(fill=BOTH, expand=YES)
boton_menu2.place(x=500, y=310)
Button(boton_menu2, command=lambda:[menu_principal()], 
        highlightbackground="black", image=primate_logo, foreground='red', activeforeground='black',
         cursor="fleur", justify="center", bd=0,  relief="raised", background="black", activebackground="black",
          font=("URW Chancery L", 16)).pack()



label1=Label(root, text="OffShell System", font=("URW Chancery L", 13), foreground="DarkRed",
                 background="black").place(x=1015, y=618)
label2=Label(root, text="Comunidad", font=("URW Chancery L", 12), foreground="DarkRed",
                 background="black").place(x=1033, y=597)

#salida del bucle y app.

root.mainloop()
