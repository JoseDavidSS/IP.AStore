from tkinter import *
from tkinter import messagebox
import time
import random
import os
import random
import time

#funcion que valida la contraseña ingresada
#E: Entry password
#S: ventana principal de administradores o mensaje de error
#R: el entry debe contener información para ser verificada
def validar_password():
    if password.get()=="admin":
        ventana_principal()
        password.delete(0,100)
    else:
        messagebox.showwarning("Cuidado","Contraseña incorrecta")

#################################################################################################################################

#Lista de texto en Inglés y en Español
diccionario=[["Inicio de Sesión en Mantenimiento AStore", "Sign in Maintaince AStore"],
             ["Bienvenido al programa de Administradores de AStore,\n Por favor ingrese su contrseña:", "Welcome to the Administrator program of AStore,\n Insert your password please"],
             ["Valida Contraseña", "Check Password"],
             ["Si es vendedor, puede consultar sus aplicaciones aquí,\n Presione el siguiente botón:", "If you are an app seller, you can check\nyour apps right here:"],
             ["Ver Apps", "Check apps"]]

#Constantes para cambiar de Idioma
IDIOMA = 0
ESP = 0
ENG = 1
#Constantes de cada texto en la interfaz
ID_titulo=0
ID_lbBienvenida=1
ID_lbContraseña=2

#Funcion que cambia el Idioma
#E: event que es la tecla F1
#S: Label con idioma en inglés o español
#R: ninguna
def cambiarIdioma(event):
    global IDIOMA
    IDIOMA = 1 - IDIOMA
    sesion.title(diccionario[0][IDIOMA])
    lb_sesion.config(text=diccionario[1][IDIOMA])
    bt_admin.config(text=diccionario[2][IDIOMA])
    lb_siesVendedor.config(text=diccionario[3][IDIOMA])
    bt_verApps.config(text=diccionario[4][IDIOMA])

#funcion para cargar imagen
def loadImage(name):
    path = os.path.join("imagenes", name)
    img = PhotoImage(file=path)
    return img

#################################################################################################################################

#Crear ventana Inicio de Sesión
sesion=Tk()
sesion.title(diccionario[0][IDIOMA])
sesion.minsize(1080,720)
sesion.resizable(width=NO, height=NO)

#Crear Canvas de la ventana de Inicio de Sesión
canvas_sesion=Canvas(sesion,width=1080,height=720,bg="Darkblue")
canvas_sesion.place(x=-2,y=-2)
canvas_sesion.pack()

#Fondo del Canvas de la ventana de Inicio de Sesión
fondo1=loadImage("fondo_naranja.gif")
fondo_matrix=Label(canvas_sesion, image=fondo1)
fondo_matrix.place(x=-1, y=0)

#Label de Inicio de Sesion
lb_sesion=Label(canvas_sesion,text=diccionario[1][IDIOMA],
                font=("Arial",22), width=42,bg="orange")
lb_sesion.place(x=165,y=50)

#Entrada de contraseña en Inicio de sesión
password=Entry(canvas_sesion,font=("MS Outlook",18), width=20,bg="orange")
password.place(x=400,y=150)

#Boton de validar contraseña
bt_admin=Button(canvas_sesion,text=diccionario[2][IDIOMA],font=("Arial",17),width=18,bg="orange",
                command=validar_password)
bt_admin.place(x=399,y=190)

#Label por si es vendedor
lb_siesVendedor=Label(canvas_sesion,text=diccionario[3][IDIOMA],
                font=("Arial",22), width=46,bg="orange")
lb_siesVendedor.place(x=150,y=450)

######################################################################################################################

#Abrir ventana de consulta de apps
def ventana_consulta():
    sesion.withdraw()
    ventana_consulta=Toplevel()
    ventana_consulta.title("Ventana de Consulta de Apps de AStore")
    ventana_consulta.minsize(1080,720)
    ventana_consulta.resizable(width=NO, height=NO)
    ventana_consulta.configure(background="dark turquoise")

    #canvas de ventana de Consulta
    canvas_consulta=Canvas(ventana_consulta, width = 1080, height =720,bg="purple")
    canvas_consulta.place(x = -1, y = 0)

    #Fondo del Canvas de la ventana principal
    global fondo4
    fondo4=loadImage("fondo_morado.gif")
    fondo_2=Label(canvas_consulta, image=fondo4)
    fondo_2.place(x=-1, y=0)

    #Label de Consultar Apps
    lb_consultarApps=Label(canvas_consulta,text="Digíte el ID de vendedor:",
                font=("Arial",18),width=20,bg="white")
    lb_consultarApps.place(x=22,y=20)

    #Label por si no conoce el ID del vendedor para Consultar Apps
    lb_consultarApps2=Label(canvas_consulta,
                            text="-Ingrese su ID: \n -Si no conoce su ID, por favor \n contactar con el Administrador",
                            font=("Arial",18),
                            width=24,
                            bg="white")
    lb_consultarApps2.place(x=22,y=20)

    #ENTRADA del ID del vendedor
    id_vendedor=Entry(canvas_consulta,font=("Arial",30), width=14,bg="#F78181")
    id_vendedor.place(x=377,y=36)

    #E: Es llamada por un botón
    #S: Información de las aplicaciones
    #R: lo buscado debe estar en la lista de apps
    #Función que busca apps por ID de vendedor
    def buscar_apps():
        fileApps = open("apps.txt", "r")
        listaApps=fileApps.readlines()
        buscar_apps_aux(listaApps,0)
        fileApps.close()
            
    def buscar_apps_aux(listaApps,contador):
        idVendedor = str(id_vendedor.get())
        idVendedor = idVendedor.lower()
        largo = len(listaApps)
        eje_x=20
        eje_y=175
        if idVendedor != "":
            return buscar_apps_aux2(listaApps, largo, idVendedor, contador, eje_x, eje_y)
        else:
            lb_errorBuscar=Label(canvas_consulta,font=("Arial",18),bg="red",fg="white",text="Error, revise los datos e\nintentelo nuevamente")
            lb_errorBuscar.place(x=460, y=145)

    def buscar_apps_aux2(listaApps, largo, idVendedor, contador, eje_x, eje_y):
        if contador != largo:
            listaApps[contador] = listaApps[contador].replace("\n", "  ").split(";")
            if idVendedor == listaApps[contador][0]:
                lb_datosVendedor = Label(canvas_consulta,text=
                                         "Nombre:"+listaApps[contador][10]+
                                         ", ID vendedor:"+listaApps[contador][0]+
                                         ", ID producto:"+listaApps[contador][1]+
                                         ", Categoría:"+listaApps[contador][2]+
                                         ", Descripción:"+listaApps[contador][3]+
                                         ", Precio:"+listaApps[contador][4]+ ",\n"
                                         " Estado:"+listaApps[contador][5]+
                                         ", Sc1:"+listaApps[contador][6]+
                                         ", Sc2:"+listaApps[contador][7]+
                                         ", Descargas Internacionales:"+listaApps[contador][8]+
                                         ", Descargas Nacionales:"+listaApps[contador][9],
                                         font=("Arial",14),bg="purple", fg="white")
                lb_datosVendedor.place(x=eje_x, y=eje_y)
                buscar_apps_aux2(listaApps, largo, idVendedor, contador+1, eje_x, eje_y+60)
            else:
                return buscar_apps_aux2(listaApps, largo, idVendedor, contador+1, eje_x, eje_y)
        else:
            lb_errorBuscar=Label(canvas_consulta,font=("Arial",18),bg="purple",fg="white",
                                 text="Estas son todas las aplicaciones de este vendedor")
            lb_errorBuscar.place(x=20, y=610)

    #Label Informacion de aplicaciones
    lb_consultarApps3=Label(canvas_consulta,text="Información de aplicaciones:",
                font=("Arial",18),width=24,bg="white")
    lb_consultarApps3.place(x=370,y=130)

    #Boton para Buscar aplicaciones por vendedor
    bt_buscarApps= Button(canvas_consulta,text="Buscar Apps",width=25,bg="purple",
                                font=("Arial",18), fg="white", command=buscar_apps)
    bt_buscarApps.place(x=700,y=37)

    #cerrar Ventana Consulta
    def cerrar_ventanaConsulta():
        ventana_consulta.destroy()
        sesion.deiconify()

    #Boton para volver a la ventana de Sesión
    bt_volverSesion2= Button(canvas_consulta,text="Regresar",width=20,bg="purple",
                                font=("Arial",18), fg="white", command=cerrar_ventanaConsulta)
    bt_volverSesion2.place(x=400,y=660)

######################################################################################################################

#Abrir Ventana Principal
def ventana_principal():
    sesion.withdraw()
    ventana_principal=Toplevel()
    ventana_principal.title("Ventana Principal de Mantnimiento AStore")
    ventana_principal.minsize(1080,720)
    ventana_principal.resizable(width=NO, height=NO)
    ventana_principal.configure(background="dark turquoise")

    #canvas de Ventana Principal
    canvas_principal=Canvas(ventana_principal, width = 1080, height =720)
    canvas_principal.place(x = -1, y = 0)

    #Fondo del Canvas de la ventana principal
    global fondo2
    fondo2=loadImage("fondo_naranja.gif")
    fondo_2=Label(canvas_principal, image=fondo2)
    fondo_2.place(x=-1, y=0)

    #cerrar Ventana Principal (cerrar sesión)
    def cerrar_ventanaPrincipal():
        ventana_principal.destroy()
        sesion.deiconify()

#*********************************************************************************************************************************************

    #Abrir Ventana de configuracion de vendedores
    def ventana_vendedor():
        ventana_principal.withdraw()
        ventana_vendedor=Toplevel()
        ventana_vendedor.title("Configuración de vendedores AStore")
        ventana_vendedor.minsize(1080,720)
        ventana_vendedor.resizable(width=NO, height=NO)
        ventana_vendedor.configure(background="dark turquoise")

        #canvas de Ventana Vendedor
        canvas_vendedor=Canvas(ventana_vendedor, width = 1080, height =720)
        canvas_vendedor.place(x = -1, y = 0)
        canvas_vendedor.configure(background="darkred")

        #Fondo del Canvas de la ventana principal
        global fondo3
        fondo3=loadImage("fondo_rojo.gif")
        fondo_3=Label(canvas_vendedor, image=fondo3)
        fondo_3.place(x=-1, y=0)

        #cerrar Ventana Vendedor
        def cerrar_ventanaVendedor():
            ventana_vendedor.destroy()
            ventana_principal.deiconify()

        #Boton para Cerrar ventana vendedor (volver a ventana principal)
        bt_volverPrincipal= Button(canvas_vendedor,text="Volver a ventana Principal",bg="darkorange",
                            font=("Arial",18),command=cerrar_ventanaVendedor)
        bt_volverPrincipal.place(x=400,y=650)

        #Label de Agregar vendedor
        lb_agregarVendedor=Label(canvas_vendedor,text="Agregar vendedor",
                        font=("Arial",20), width=15,bg="Darkred",fg="white")
        lb_agregarVendedor.place(x=65,y=20)

        #Label de Nombre del vendedor
        lb_nombreVendedor=Label(canvas_vendedor,text="Nombre de vendedor:",
                        font=("Arial",20), width=20,bg="#FF0000")
        lb_nombreVendedor.place(x=22,y=70)

        #Label de Correo del vendedor
        lb_correoVendedor=Label(canvas_vendedor,text="Correo de vendedor:",
                        font=("Arial",20), width=20,bg="#FF0000")
        lb_correoVendedor.place(x=22,y=165)

        #Label de Sitio Web del vendedor
        lb_sitioWeb=Label(canvas_vendedor,text="Sitio Web:",
                        font=("Arial",20), width=20,bg="#FF0000")
        lb_sitioWeb.place(x=22,y=255)

        #ENTRADA del nombre del Vendedor
        nombre_vendedorRegistro=Entry(canvas_vendedor,font=("Arial",18), width=25,bg="#F78181")
        nombre_vendedorRegistro.place(x=20,y=110)

        #ENTRADA del correo del Vendedor
        correo_vendedorRegistro=Entry(canvas_vendedor,font=("Arial",18), width=25,bg="#F78181")
        correo_vendedorRegistro.place(x=20,y=205)

        #ENTRADA del SitoWeb del Vendedor
        sitio_webRegistro=Entry(canvas_vendedor,font=("Arial",18), width=25,bg="#F78181")
        sitio_webRegistro.place(x=20,y=295)

        #Label de Buscar vendedor
        lb_buscarVendedor=Label(canvas_vendedor,text="Buscar vendedor",
                                font=("Arial",20), width=20,bg="darkred",fg="white")
        lb_buscarVendedor.place(x=731,y=20)

        #Label de busqueda por nombre del vendedor
        lb_idVendedor=Label(canvas_vendedor,text="Nombre del vendedor:",
                        font=("Arial",20), width=20,bg="#FF0000")
        lb_idVendedor.place(x=731,y=70)

        #Entrada del Nombre del Vendedor para su busqueda de ID
        nombre_vendedorBusqueda=Entry(canvas_vendedor,font=("Arial",18), width=25,bg="#F78181")
        nombre_vendedorBusqueda.place(x=729,y=110)

        #E: Entry del nombre, correo y página web de usuario
        #S: archivo txt con la información escrita del nuevo usuario
        #R: el nombre no debe de estar creado
        #funcion que registra a los vendedores nuevos
        def registro_vendedores():
            fileVendedor = open("vendedor.txt", "r")
            listaVendedores=fileVendedor.readlines()
            registro_vendedores_aux(listaVendedores,1)
            fileVendedor.close()
            
        #funcion auxiliar que verifica que todos los campos de las entradas sean llenados    
        def registro_vendedores_aux(listaVendedores,contador):
            nombre = str(nombre_vendedorRegistro.get())
            nombre = nombre.lower()
            correo = str(correo_vendedorRegistro.get())
            correo = correo.lower()
            sitioWeb = str(sitio_webRegistro.get())
            sitioWeb = sitioWeb.lower()
            largo = len(listaVendedores)
            id_vendedor = largo
            if nombre != "" and correo != "":
                return registro_vendedores_aux2(listaVendedores, largo, nombre, correo, sitioWeb, id_vendedor, contador)
            else:
                lb_errorBuscar=Label(canvas_vendedor,font=("Arial",18),bg="red",fg="white",text="Error, revise los datos e intentelo nuevamente")
                lb_errorBuscar.place(x=19, y=400)
                
        #funcion auxiliar que valida que no se repitan datos ya existentes y agrega la nueva información
        def registro_vendedores_aux2(listaVendedores, largo, nombre, correo, sitioWeb, id_vendedor, contador):
            if contador != largo:
                listaVendedores[contador] = listaVendedores[contador].replace("\n", "  ").split(";")
                if nombre == listaVendedores[contador][1] or correo == listaVendedores[contador][2]:
                    lb_datosDuplicados = Label(canvas_vendedor, font=("Arial",18), bg="red",fg="white",text= "Nombre o correo ya existentes para vendedor")
                    lb_datosDuplicados.place(x=19, y=400)
                else:
                    return registro_vendedores_aux2(listaVendedores, largo, nombre, correo, sitioWeb, id_vendedor, contador+1)
            else:
                fileVendedor = open("vendedor.txt", "a")
                fileVendedor.write(str(id_vendedor)+ ";" + nombre + ";" + correo + ";" + sitioWeb + "\n")
                fileVendedor.close
                ventana_vendedor.destroy()
                ventana_principal.deiconify()

        #*********************************************#
        #E: Entry de usuario
        #S: label con toda la información del usuario
        #R: nombre completo del vendedor en el entry
        #Función que busca a un vendedor por su nombre
        def buscar_vendedor():
            fileVendedor = open("vendedor.txt", "r")
            listaVendedores=fileVendedor.readlines()
            buscar_vendedor_aux(listaVendedores,1)
            fileVendedor.close()
            
        def buscar_vendedor_aux(listaVendedores,contador):
            nombre = str(nombre_vendedorBusqueda.get())
            nombre = nombre.lower()
            largo = len(listaVendedores)
            if nombre != "":
                return buscar_vendedor_aux2(listaVendedores, largo, nombre, contador)
            else:
                lb_errorBuscar=Label(canvas_vendedor,font=("Arial",18),bg="red",fg="white",text="Error, revise los datos e\nintentelo nuevamente")
                lb_errorBuscar.place(x=460, y=145)

        def buscar_vendedor_aux2(listaVendedores, largo, nombre, contador):
            if contador != largo:
                listaVendedores[contador] = listaVendedores[contador].replace("\n", "  ").split(";")
                if nombre == listaVendedores[contador][1]:
                    print (len(listaVendedores[contador]))
                    if len(listaVendedores[contador]) == 3:
                        lb_datosVendedor = Label(canvas_vendedor,text=
                                                 "ID del vendedor:"+listaVendedores[contador][0]+"\n"+
                                                 "Nombre Vendedor:"+listaVendedores[contador][1]+"\n"+
                                                 "Correo:"+listaVendedores[contador][2],font=("Arial",18),bg="red")
                        lb_datosVendedor.place(x=650,y=260)
                    else:
                        lb_datosVendedor = Label(canvas_vendedor,text=
                                                 "ID del vendedor:"+listaVendedores[contador][0]+"\n"+
                                                 "Nombre Vendedor:"+listaVendedores[contador][1]+"\n"+
                                                 "Correo:"+listaVendedores[contador][2]+"\n"+
                                                 "Sitio Web:"+listaVendedores[contador][3],font=("Arial",18),bg="red")
                        lb_datosVendedor.place(x=650,y=260)
                else:
                    return buscar_vendedor_aux2(listaVendedores, largo, nombre, contador+1)
            else:
                lb_errorBuscar=Label(canvas_vendedor,font=("Arial",18),bg="red",fg="white",text="Error, revise los datos e\nintentelo nuevamente")
                lb_errorBuscar.place(x=460, y=145)

        #***********************************************#

        #Label 
        lb_idVendedor2=Label(canvas_vendedor,font=("Arial",18),bg="red",text="ID del vendedor que desea eliminar:")
        lb_idVendedor2.place(x=675, y=440)
        
        #Entrada del ID del Vendedor para su eliminación
        id_vendedorEliminacion=Entry(canvas_vendedor,font=("Arial",18), width=25,bg="#F78181")
        id_vendedorEliminacion.place(x=710,y=475)
                
        #función para eliminar vendedores que no tengan aplicaciones en venta
        #E: Entry del id del vendedor
        #S: archivo txt sin la información del usuario
        #R: validar si el vendedor tiene apps activas
        def eliminar_vendedor(listaVendedor, listaApps):
            id_vendedor = int(id_vendedorEliminacion.get())
            id_app = id_vendedor
            id_vendedor = id_vendedor-1
            largo_listaApps = len(listaApps)
            
            if id_vendedor != "":
                return eliminar_vendedor_aux(listaVendedor, listaApps, largo_listaApps, id_vendedor, 0, id_app)
            else:
                lb_errorCrearDatos=Label(canvas_vendedor,bg="lightblue",font=("Arial",18),text="Error, revise los datos e intentelo nuevamente")
                lb_errorCrearDatos.place(x=22, y=610)
        
        def eliminar_vendedor_aux(listaVendedor, listaApps, largo_listaApps, id_vendedor, contador, id_app):
            
            listaVendedor[id_vendedor] = listaVendedor[id_vendedor].split(";")
            id_vendedor = listaVendedor[id_vendedor][0]
            
            listaApps[id_vendedor] = listaApps[id_app].replace("\n", "  ").split(";")
            id_vendedor2 = listaApps[contador][0]
            
            if contador == largo_listaApps:
                lb_vendedorEliminado=Label(canvas_vendedor,bg="lightblue",font=("Arial",18),text="Vendedor eliminado")
                lb_vendedorEliminado.place(x=22, y=610)
                
            elif id_vendedor == id_vendedor2:
                fileVendedor = open ("vendedor.txt","w")
                listaVendedor[id_vendedor].write("")
                fileVendedor.close()
                lb_vendedorPoseeApps=Label(canvas_vendedor,bg="lightblue",font=("Arial",18),text="El vendedor posee app en venta")
                lb_vendedorPoseeApps.place(x=22, y=610)
                
            else:
                eliminar_vendedor_aux(listaVendedor, listaApps, largo_listaApps, id_vendedor, contador+1)
    
        def eliminarVendedor():
            fileVendedor = open("vendedor.txt", "r")
            fileApps = open("apps.txt", "r")
            listaVendedor = fileVendedor.readlines()
            listaApps = fileApps.readlines()
            eliminar_vendedor(listaVendedor, listaApps)
            fileVendedor.close()
            fileApps.close()
            
        #Boton para crear el perfil del vendedor
        bt_crearVendedor= Button(canvas_vendedor,text="Crear perfil de Vendedor",bg="darkred",
                            font=("Arial",18),fg="white",width=23,command=registro_vendedores)
        bt_crearVendedor.place(x=18,y=345)

        #Boton para buscar vendedor
        bt_buscarIdVendedor= Button(canvas_vendedor,text="Buscar Vendedor",bg="darkred",
                            font=("Arial",18),fg="white",width=23, command=buscar_vendedor)
        bt_buscarIdVendedor.place(x=728,y=158)

        #Boton para eliminar vendedor
        bt_buscarIdVendedor= Button(canvas_vendedor,text="Eliminar Vendedor",bg="darkred",
                            font=("Arial",18),fg="white",width=23, command=eliminarVendedor)
        bt_buscarIdVendedor.place(x=710,y=510)

#*******************************************************************************************************************************************

    #Abrir Ventana de configuracion de apps
    def ventana_apps():
        ventana_principal.withdraw()
        ventana_apps=Toplevel()
        ventana_apps.title("Configuración de apps AStore")
        ventana_apps.minsize(1080,720)
        ventana_apps.resizable(width=NO, height=NO)
        ventana_apps.configure(background="dark turquoise")

        #canvas de Ventana Vendedor
        canvas_apps=Canvas(ventana_apps, width = 1080, height =720)
        canvas_apps.place(x = -1, y = 0)
        canvas_apps.configure(background="lightblue")

        #Fondo del Canvas de la ventana de configuración de apps
        global fondo5
        fondo5=loadImage("fondo_celeste.gif")
        fondo_5=Label(canvas_apps, image=fondo5)
        fondo_5.place(x=-1, y=0)

        #Label de Incluir Apps
        lb_incluirApps=Label(canvas_apps,text="Incluir Apps",
                        font=("Arial",18),width=20,bg="white")
        lb_incluirApps.place(x=22,y=10)

        #Label del ID de vendedor
        lb_idVendedorApps=Label(canvas_apps,text="ID del Vendedor:",
                        font=("Arial",18),width=20,bg="white")
        lb_idVendedorApps.place(x=22,y=50)

        #Entrada del ID de vendedor
        id_vendedorRegistroApps=Entry(canvas_apps,font=("Arial",18), width=22,bg="lightblue")
        id_vendedorRegistroApps.place(x=20,y=85)

        #Label del nombre del juego
        lb_nombreJuego=Label(canvas_apps,text="Nombre de la App:",
                        font=("Arial",18),width=20,bg="white")
        lb_nombreJuego.place(x=22,y=118)

        #Entrada del nombre del juego
        nombreJuego=Entry(canvas_apps,font=("Arial",18), width=22,bg="lightblue")
        nombreJuego.place(x=20,y=153)

        #Label de la categoria de la App
        lb_categoriaApps=Label(canvas_apps,text="Categoria de la App",
                        font=("Arial",18),width=20,bg="white")
        lb_categoriaApps.place(x=22,y=186)        

        #Entrada de la categoria de la App
        categoriaRegistroApps=Entry(canvas_apps,font=("Arial",18), width=22,bg="lightblue")
        categoriaRegistroApps.place(x=20,y=221)

        #Label de la descripcion de la App
        lb_descripcionApps=Label(canvas_apps,text="Descripcion de la App",
                        font=("Arial",18),width=20,bg="white")
        lb_descripcionApps.place(x=22,y=254)             

        #Entrada de la descripción de la App
        descripcionRegistroApps=Entry(canvas_apps,font=("Arial",18), width=22,bg="lightblue")
        descripcionRegistroApps.place(x=20,y=289)

        #Label del precio de la App
        lb_precioApps=Label(canvas_apps,text="Precio de la App",
                        font=("Arial",18),width=20,bg="white")
        lb_precioApps.place(x=22,y=322)           

        #Entrada del precio de la App
        precioRegistroApps=Entry(canvas_apps,font=("Arial",18), width=22,bg="lightblue")
        precioRegistroApps.place(x=20,y=357)

        #Label estado de la App
        lb_estadoApps=Label(canvas_apps,text="Estado de la App",
                        font=("Arial",18),width=20,bg="white")
        lb_estadoApps.place(x=22,y=390)           

        #Entrada del estado de la App
        estadoRegistroApps=Entry(canvas_apps,font=("Arial",18), width=22,bg="lightblue")
        estadoRegistroApps.place(x=20,y=425)

        #Label del nombre de screenshot1 de la App
        lb_sc1Apps=Label(canvas_apps,text="Nombre del Screenshot 1",
                        font=("Arial",18),width=20,bg="white")
        lb_sc1Apps.place(x=22,y=458)   

        #Entrada del nombre del archivo del screenshot 1 de la App
        sc1RegistroApps=Entry(canvas_apps,font=("Arial",18), width=22,bg="lightblue")
        sc1RegistroApps.place(x=20,y=493)

        #Label del nombre de screenshot1 de la App
        lb_sc2Apps=Label(canvas_apps,text="Nombre del Screenshot 2",
                        font=("Arial",18),width=20,bg="white")
        lb_sc2Apps.place(x=22,y=526)   

        #Entrada del nombre del archivo del screenshot 2 de la App
        sc2RegistroApps=Entry(canvas_apps,font=("Arial",18), width=22,bg="lightblue")
        sc2RegistroApps.place(x=20,y=561)
        
        #***************************************************************************#
        #E: Todos los entry para agregar las aplicaciones
        #S: archivo txt con la información escrita de cada app
        #R: la aplicación no debe de estar creada
        #funcion que registra las aplicaciones nuevas
        def registro_apps(listaApps):
            id_vendedor = str(id_vendedorRegistroApps.get())
            id_vendedor = id_vendedor.lower()
            
            categoria = str(categoriaRegistroApps.get())
            categoria = categoria.lower()
            
            descripcion = str(descripcionRegistroApps.get())
            descripcion = descripcion.lower()

            precio = str(precioRegistroApps.get())
            precio = precio.lower()

            estado = str(estadoRegistroApps.get())
            estado = estado.lower()

            sc1 = str(sc1RegistroApps.get())
            sc1 = sc1.lower()

            sc2 = str(sc2RegistroApps.get())
            sc2 = sc2.lower()

            nombre = str(nombreJuego.get())
            nombre = nombre.lower()
            
            largo = len(listaApps)
            id_producto = largo
            
            if id_vendedor != "" and categoria != "" and descripcion != "" and precio != "" and estado != "" and sc1 != "" and sc2 != "":
                return registro_apps_aux(listaApps, largo, id_vendedor, categoria, descripcion, precio, estado, sc1, sc2, nombre)
            else:
                lb_errorCrearDatos=Label(canvas_apps,bg="lightblue",font=("Arial",18),text="Error, revise los datos e intentelo nuevamente")
                lb_errorCrearDatos.place(x=22, y=610)
                
        #Función auxiliar de registro_apps
        def registro_apps_aux(listaApps, largo, id_vendedor, categoria, descripcion, precio, estado, sc1, sc2, nombre):
            id_producto = largo+1
            descargas = "0"
            descargas_internacional = "0"
            fileApps = open("apps.txt", "a")
            fileApps.write(str(id_vendedor)+ ";" +
                           str(id_producto) + ";" +
                            categoria + ";" +
                            descripcion + ";" +
                            precio + ";" +
                            estado + ";" +
                            sc1 + ";" +
                            sc2 + ";" +
                            descargas + ";" +
                            descargas_internacional + ";" +
                            nombre + "\n")
            fileApps.close
            ventana_apps.destroy()
            ventana_principal.deiconify()
            
        #Función que abre el archivo de texto y retorna registro_apps con argumento de listaApps que es la lista de Apps de apps.txt
        def abrir_archivo_apps():
            fileApps = open("apps.txt", "r")
            listaApps=fileApps.readlines()
            registro_apps(listaApps)
            fileApps.close()
            
        #***************************************************************************#
            
        #Label de eliminar aplicación
        lb_eliminarApps=Label(canvas_apps,text="Ingrese el ID del producto a eliminar:\nConsulte el ID en la\nVentana de Consulta de Apps de AStore ",
                        font=("Arial",18),width=32,bg="white")
        lb_eliminarApps.place(x=600,y=10)   

        #Entrada de ID de producto para su eliminación
        id_cambiarEstado=Entry(canvas_apps,font=("Arial",18), width=22,bg="lightblue")
        id_cambiarEstado.place(x=695,y=100)
        
        #E: Entry del id de producto de la aplicación
        #S: archivo txt de apps modificado de activo a inactivo, o viceversa
        #R: Entry completo
        #Funcion para cambiar estado de apps
        def cambiar_estado(listaApps):
            id_producto = id_cambiarEstado.get()
            if id_producto != "":
                return cambiar_estado_aux(id_producto, listaApps)
            else:
                lb_errorCrearDatos=Label(canvas_apps,bg="lightblue",font=("Arial",18),text="Error, revise los datos e intentelo nuevamente")
                lb_errorCrearDatos.place(x=400, y=610)
        #Funcion auxiliar de cambiar_estado
        def cambiar_estado_aux(id_producto, listaApps):
            id_producto = int(id_producto)-1
            listaApps[id_producto] = listaApps[id_producto].replace("\n", "  ").split(";")
            estado = listaApps[id_producto][5]
            
            if estado == "a":
                fileApps = open("apps.txt","w")
                estado.write("i")
                fileApps.close
                lb_vendedorEliminado=Label(canvas_apps,bg="lightblue",font=("Arial",18),text="App inactivada")
                lb_vendedorEliminado.place(x=22, y=610) 
            else:
                lb_vendedorEliminado=Label(canvas_apps,bg="lightblue",font=("Arial",18),text="App activada")
                lb_vendedorEliminado.place(x=22, y=610) 
        #Función que abre el archivo de texto y retorna cambiar_estado con argumento de listaApps que es la lista de Apps de apps.txt
        def abrir_archivo_apps2():
            fileApps = open("apps.txt", "r")
            listaApps=fileApps.readlines()
            cambiar_estado(listaApps)
            fileApps.close()
        
        #***************************************************************************#
        
        #cerrar Ventana Apps
        def cerrar_ventanaApps():
            ventana_apps.destroy()
            ventana_principal.deiconify()

        #Boton para agregar apps y volver
        bt_agregarApps= Button(canvas_apps,text="Agregar App y volver",bg="blue",fg="white",
                            font=("Arial",18),command=abrir_archivo_apps)
        bt_agregarApps.place(x=525,y=667)
        
        #Boton para cambiar estado de apps y volver
        bt_cambiarEstadoApps= Button(canvas_apps,text="Cambiar Estado de App y volver",bg="blue",fg="white",
                            font=("Arial",18), command=abrir_archivo_apps2)
        bt_cambiarEstadoApps.place(x=650,y=135)

        #Boton de Cerrar ventana apps (volver a ventana principal)
        bt_volverPrincipal= Button(canvas_apps,text="Volver a ventana Principal",bg="blue",fg="white",
                            font=("Arial",18),command=cerrar_ventanaApps)
        bt_volverPrincipal.place(x=775,y=667)

#*******************************************************************************************************************************************
# Elementos de la ventana principal

    #Label de Escoger una opción
    lb_sesion=Label(canvas_principal,text="Escoja una función",
                font=("Arial",22),width=20,bg="white")
    lb_sesion.place(x=370,y=75)

    #Label de Agregar o eliminar vendedor
    lb_sesion=Label(canvas_principal,text="Agregar, buscar o eliminar vendedor:",
                font=("Arial",18),width=29,bg="white")
    lb_sesion.place(x=65,y=300)

    #Label de Agregar o eliminar apps
    lb_sesion=Label(canvas_principal,text="Agregar o eliminar apps:",
                font=("Arial",18),width=25,bg="white")
    lb_sesion.place(x=625,y=300)

    #Boton Proceder de Agregar o eliminar vendedor
    bt_procederVendedor= Button(canvas_principal,text="Proceder",width=25,bg="darkorange",
                                font=("Arial",18),command=ventana_vendedor)
    bt_procederVendedor.place(x=90,y=350)

    #Boton Proceder de Agregar o eliminar apps
    bt_procederVendedor= Button(canvas_principal,text="Proceder",width=25,bg="darkorange",
                                font=("Arial",18),command=ventana_apps)
    bt_procederVendedor.place(x=625,y=350)

    #Boton de Cerrar Ventana Principal (cerrar sesión)
    bt_volverSesion= Button(canvas_principal,text="Cerrar sesión",bg="darkorange",
                            font=("Arial",18),command=cerrar_ventanaPrincipal)
    bt_volverSesion.place(x=450,y=650)

##################################################################################################

#Boton para ir a la ventana de consulta de apps
bt_verApps=Button(canvas_sesion,text=diccionario[4][IDIOMA],font=("Arial",17),
                  width=30,bg="orange", command=ventana_consulta)
bt_verApps.place(x=345,y=540)

sesion.bind("<F1>", cambiarIdioma)
sesion.mainloop()#Final del programa
