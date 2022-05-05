from tkinter import *
from tkinter import messagebox
import time
import random
import os
import random
import time
import tkinter.ttk as ttk

#Función para cargar imagen
def cargarImagen(nombre):
    ruta=os.path.join("imagenes",nombre)
    imagen=PhotoImage(file=ruta)
    return imagen

#Lista de texto en Inglés y en Español
global diccionario
diccionario=[["Cerrar Tienda", "Close Shop"],
             ["Juegos Principales:", "Best Sellers:"],
             ["Servicio al cliente: jose.david.san@gmail.com","Client Service: jose.david.san@gmail.com"]]

#Constantes para cambiar de Idioma
IDIOMA = 0
ESP = 0
ENG = 1


#Crear ventana Inicio de Sesión
ventana_idioma=Tk()
ventana_idioma.title("Escoger Idioma - Select Language")
ventana_idioma.minsize(500,500)
ventana_idioma.resizable(width=NO, height=NO)

#Crear Canvas de la ventana de Inicio de Sesión
canvas_idioma=Canvas(ventana_idioma,width=500,height=500,bg="black")
canvas_idioma.place(x=-2,y=-2)
canvas_idioma.pack()

#Fondo del Canvas de la ventana de Inicio de Sesión 
fondo1=cargarImagen("fondo_bosque.gif")
fondo_idioma=Label(canvas_idioma, image=fondo1)
fondo_idioma.place(x=-1, y=0)

#Label de Idioma
lb_bienvenida=Label(canvas_idioma,
                text="-Bienvenido a la tienda Astore\n-Welcome to the Astore",
                font=("Arial",22), width=23, bg="darkblue", fg="lightgrey")
lb_bienvenida.place(x=60,y=40)

#Label de Idioma
lb_idioma=Label(canvas_idioma,
                text="Idioma-Language",
                font=("Arial",22), width=14, bg="lightblue")
lb_idioma.place(x=130,y=250)

#Label de Instrucción de Idioma
lb_idioma1=Label(canvas_idioma,
                 text="-Cambie el idioma presionando F1 en cualquier momento\n-Change your language at anytime by pressing F1",
                 font=("Arial",13), width=48, bg="lightblue")

##############################################################################################################################


#Abrir tienda
def tienda():
    ventana_idioma.withdraw()
    ventana_tienda=Toplevel()
    ventana_tienda.title("Tienda AStore")
    ventana_tienda.minsize(1080,720)
    ventana_tienda.resizable(width=NO, height=NO)
    ventana_tienda.configure(background="black")
    
    #canvas de Ventana Principal
    canvas_tienda=Canvas(ventana_tienda, width = 1080, height =720)
    canvas_tienda.place(x = -1, y = 0)

    #Fondo de la tienda AStore
    global fondo2
    fondo2=cargarImagen("fondo_naranja.gif")
    fondo_tienda=Label(canvas_tienda, image=fondo2)
    fondo_tienda.place(x=-1, y=0)

    #Label AStore
    lb_astore = Label(canvas_tienda,text="AStore",font=("Matura MT Script Capitals",35), bg="darkorange")
    lb_astore.place(x=22,y=10)
   
    #Función de cerrar tienda Astore (volver a escoger idioma)
    def cerrar_tienda():
        ventana_tienda.destroy()
        ventana_idioma.deiconify()

    #Boton de Cerrar tienda (volver a selección de idioma)
    bt_volverInstrucciones= Button(canvas_tienda,
                                   text=diccionario[0][IDIOMA],
                                   bg="darkorange", font=("Arial",14), command=cerrar_tienda)
    bt_volverInstrucciones.place(x=10,y=675)

    #E: Entrada de texto de busqueda o las categorías de combobox
    #S: ventana con la app buscada
    #R: La entrada no puede ser vacía o sin datos
    #Función de busqueda
    def buscarApps(event):
        if busqueda.get()!="":
             return buscarApps_aux(0)
        else:
            return None        
    def buscarApps_aux(contador):
        if contador==len(listaApps):
            return []
        elif listaApps[contador][10].lower().startswith((busqueda.get()).lower())==True:#Revisa si la lista en la posicion de los nombres coincide con la busqueda
            return abrir_app(contador)#abre la ventana del juego buscado o seleccionado
        else:
            return buscarApps_aux(contador+1)

    def separarApps(contador):
        if contador == len(listaApps):
            return
        listaApps[contador] = listaApps[contador].replace("\n", "  ").split(";")
        separarApps(contador + 1)
    lista_apps = open("apps.txt", 'r')
    listaApps = lista_apps.readlines()
    separarApps(0)
    lista_apps.close()
    #**********************************************************************************************#

    #Función para abrir ventana para registrar usuario
    def ventana_registar_usuario():
        ventana_tienda.withdraw()
        ventana_usuario=Toplevel()
        ventana_usuario.title("Registro Usuario")
        ventana_usuario.minsize(500,500)
        ventana_usuario.resizable(width=NO, height=NO)
        ventana_usuario.configure(background="black")
        
        #Crear Canvas de la ventana de Inicio de Sesión
        canvas_usuario=Canvas(ventana_usuario,width=500,height=500,bg="black")
        canvas_usuario.place(x=-2,y=-2)
        canvas_usuario.pack()

        #Fondo del Canvas de la ventana de registar usuario
        global fondo8
        fondo8=cargarImagen("fondo_bosque.gif")
        fondo_usuario=Label(canvas_usuario, image=fondo8)
        fondo_usuario.place(x=-1, y=0)

        #Label Nombre de usuario
        lb_nombreUsuario = Label(canvas_usuario,text="Nombre de Usuario:",font=("Arial",18), bg="darkorange")
        lb_nombreUsuario.place(x=145,y=35)

        #Entrada de Nombre de usuario
        nombre_usuario=Entry(canvas_usuario, font=("Arial",18), width=20,bg="orange")
        nombre_usuario.place(x=120, y=75)

        #Label correo de usuario
        lb_nombreCorreo = Label(canvas_usuario,text="Correo de Usuario:",font=("Arial",18), bg="darkorange")
        lb_nombreCorreo.place(x=150,y=160)

        #Entrada de correo de usuario
        correo_usuario=Entry(canvas_usuario, font=("Arial",18), width=20,bg="orange")
        correo_usuario.place(x=120, y=200)

        #Función para cerrar ventana de Ususario
        def cerrar_ventanaUsuario():
            ventana_usuario.destroy()
            ventana_tienda.deiconify()
            
        #E: informacipon del usuario
        #S: registro de usuarios en el txt
        #R: ninguna
        #funcion que registra a los usuarios
        def registro_usuario():
            fileUsuario = open("comprador.txt", "r")
            listaUsuarios=fileUsuario.readlines()
            largo = len(listaUsuarios)
            registro_usuarios_aux(listaUsuarios, 0, largo)
            fileUsuario.close()    
        #funcion auxiliar que verifica que todos los campos de las entradas sean llenados    
        def registro_usuarios_aux(listaUsuarios,contador, largo):
            nombre = str(nombre_usuario.get())
            nombre = nombre.lower()
            correo = str(correo_usuario.get())
            correo = correo.lower()
            id_usuario = largo+1
            print(id_usuario)
            if nombre != "" and correo != "":
                return registro_usuarios_aux2(listaUsuarios, largo, nombre, correo, id_usuario, contador)
            else:
                lb_errorBuscar=Label(canvas_usuario,font=("Arial",18),bg="red",fg="white",text="Error, revise los datos e intentelo nuevamente")
                lb_errorBuscar.place(x=19, y=400)
        #funcion auxiliar que valida que no se repitan datos ya existentes y agrega la nueva información
        def registro_usuarios_aux2(listaUsuarios, largo, nombre, correo, id_usuario, contador):
            if contador != largo:
                listaUsuarios[contador] = listaUsuarios[contador].replace("\n", "  ").split(";")
                if nombre == listaUsuarios[contador][1] or correo == listaUsuarios[contador][2]:
                    lb_datosDuplicados = Label(canvas_usuario, font=("Arial",18), bg="red",fg="white",text= "Nombre o correo ya existentes para vendedor")
                    lb_datosDuplicados.place(x=19, y=400)
                else:
                    return registro_usuarios_aux2(listaUsuarios, largo, nombre, correo, id_usuario, contador+1)
            else:
                fileUsuario = open("comprador.txt", "a")
                fileUsuario.write(str(id_usuario)+ ";" + nombre + ";" + correo + "\n")
                fileUsuario.close
                ventana_usuario.destroy()

        #Boton para registrar usuario
        bt_registrarUsusario= Button(canvas_usuario,
                                           text="Registrar Usuario y Volver",
                                           bg="darkorange", font=("Arial",14), command=registro_usuario)
        bt_registrarUsusario.place(x=120,y=420)
        
    #*********************************************************************#
    
    #Función que abre la app escogida
    def abrir_app(contador):
        ventana_tienda.withdraw()
        ventana_app=Toplevel()
        ventana_app.title("App")
        ventana_app.minsize(1080,720)
        ventana_app.resizable(width=NO, height=NO)
        ventana_app.configure(background="black")
    
        #canvas de Ventana Principal
        canvas_app=Canvas(ventana_app, width = 1080, height =720)
        canvas_app.place(x = -1, y = 0)

        #Fondo de la tienda AStore
        global fondo3
        fondo3=cargarImagen("fondo_naranja.gif")
        fondo_app=Label(canvas_app, image=fondo3)
        fondo_app.place(x=-1, y=0)

        #Label Nombre App
        lb_nombre = Label(canvas_app,text=listaApps[contador][10],font=("Matura MT Script Capitals",35), bg="darkorange")
        lb_nombre.place(x=22,y=10)

        #Label Descripción App
        lb_descripcion = Label(canvas_app,text=listaApps[contador][3],wraplength=800,font=("Arial",18), bg="darkorange")
        lb_descripcion.place(x=125,y=150)

        #Screen Shot 1 de APP
        global app_sc1
        app_sc1=cargarImagen(listaApps[contador][6])
        sc1_app=Label(canvas_app, image=app_sc1)
        sc1_app.place(x=20, y=400)

        #Screen Shot 2 de APP
        global app_sc2
        app_sc2=cargarImagen(listaApps[contador][7])
        sc2_app=Label(canvas_app, image=app_sc2)
        sc2_app.place(x=400, y=400)

        #Función para cerrar ventana de App
        def cerrar_ventanaApp():
            ventana_app.destroy()
            ventana_tienda.deiconify()
        
        #Boton para volver a la tienda
        bt_volverTienda= Button(canvas_app,
                                text="volver tienda",
                                bg="darkorange", font=("Arial",14), command = cerrar_ventanaApp)
        bt_volverTienda.place(x=10,y=675)

        #Boton para descargar app
        bt_descargarApp= Button(canvas_app,
                                text="Descargar App",
                                bg="darkorange", font=("Arial",22), command = ventana_registar_usuario)
        bt_descargarApp.place(x=825,y=650)



    #***************************************************#
    #Funciónes que son asignadas a los botones de la ventana principal para que abra la aplicación seleccionada
    def crear():
        abrir_app(0)
    def crear2():
        abrir_app(1)
    def crear3():
        abrir_app(2)
    def crear4():
        abrir_app(3)

    #Label Juegos principales
    lb_nombre = Label(canvas_tienda,text=diccionario[1][IDIOMA],font=("Matura MT Script Capitals",35), bg="darkorange")
    lb_nombre.place(x=22,y=150)

    #Label Servicio al cliente
    lb_servicio = Label(canvas_tienda,text=diccionario[2][IDIOMA],font=("Arial",18), bg="darkorange")
    lb_servicio.place(x=550,y=675)
        
    #Boton de primera apliccaión
    global fondo4
    fondo4 = cargarImagen("app1.gif")
    bt_priemaraApp= Button(canvas_tienda,
                                   text="App 1", bg="darkorange", image=fondo4, font=("Arial",14), command=crear)
    bt_priemaraApp.place(x=50,y=300)
    
    #Boton de segunda apliccaión
    global fondo5
    fondo5 = cargarImagen("app2.gif")
    bt_segundaApp= Button(canvas_tienda,
                                   text="App 2",
                                   bg="darkorange", image=fondo5, font=("Arial",14), command=crear2)
    bt_segundaApp.place(x=300,y=300)

    global fondo6
    fondo6 = cargarImagen("app3.gif")
    
    #Boton de tercera apliccaión
    bt_terceraApp= Button(canvas_tienda,
                                   text="App 3",
                                   bg="darkorange", image=fondo6, font=("Arial",14), command=crear3)
    bt_terceraApp.place(x=550,y=300)

    global fondo7
    fondo7 = cargarImagen("app4.gif")
    
    #Boton de cuarta apliccaión
    bt_cuartaApp= Button(canvas_tienda,
                                   text="App 4",
                                   bg="darkorange", image=fondo7, font=("Arial",14), command=crear4)
    bt_cuartaApp.place(x=800,y=300)


    #Entrada de buscar
    busqueda=Entry(canvas_tienda,font=("Arial",18), width=20,bg="orange")
    busqueda.place(x=225, y=20)
    busqueda.bind("<Return>", buscarApps)
    
    #E: la categoría seleccionada en el combobox
    #S: ventana de app seleccionada dependiendo la categoría
    #R: ninguna
    #Función que busca la aplicación por categoría
    def buscarCategoria(event):
        categoria = cbCategorias.get()
        if categoria.lower() == "Sin categoria":
            pass
        elif categoria.lower() == "online":
            crear()
        elif categoria.lower() == "retro":
            crear2()
        elif categoria.lower() == "historia":
            crear3()
        elif categoria.lower() == "mods":
            crear4()
        else:
            return None

    #Combobox para seleccionar categorías en la Tienda
    CATEGORIAS = ["Sin Categoria","Online","Retro","Historia","Mods"]
    cbCategorias = ttk.Combobox(canvas_tienda, values=CATEGORIAS)
    cbCategorias.set("Sin Categoria")
    cbCategorias.place(x=500, y=25)
    cbCategorias.bind("<<ComboboxSelected>>", buscarCategoria)

    #E: evento, en este cas, la tecla F1
    #S: Labels con idioma en inglés
    #R: ninguna
    #Funcion que cambia el Idioma
    def cambiarIdioma(event):
        global IDIOMA
        IDIOMA = 1 - IDIOMA
        bt_volverInstrucciones.config(text=diccionario[0][IDIOMA])
        lb_nombre.config(text=diccionario[1][IDIOMA])
        lb_servicio.config(text=diccionario[2][IDIOMA])
                         
    ventana_tienda.bind("<F1>", cambiarIdioma)
    

#Boton ir a Tienda
bt_irTienda= Button(canvas_idioma,
                    text="Continuar-Continue",
                    width=25, bg="darkblue", font=("Arial",18), fg="lightgrey" ,command=tienda)
bt_irTienda.place(x=70,y=400)

ventana_idioma.mainloop()
