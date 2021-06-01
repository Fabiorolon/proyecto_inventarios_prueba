from tkinter import ttk
from tkinter import *
from tkinter import messagebox
import sqlite3

#---------------FUNCION QUE CREA LA CONEXION DE LA BASE DE DATOS Y CREA LAS TABLAS DE LA BBDD--------------------------------------------------
#---------------FUNCION QUE CREA LA CONEXION DE LA BASE DE DATOS Y CREA LAS TABLAS DE LA BBDD--------------------------------------------------

def conexionBBDD():
    miConexion=sqlite3.connect("DDBBpruebaAbril.db")
    miCursor=miConexion.cursor()
    try:
        miCursor.execute('''
            CREATE TABLE IF NOT EXISTS empleados(
            idempleado INTEGER PRIMARY KEY NOT NULL,
            nombre VARCHAR(50) NOT NULL,
            apellidos VARCHAR(30) NOT NULL,
            direccion VARCHAR(100),
            telefono_fijo VARCHAR(20),
            celular VARCHAR(20),
            sexo VARCHAR(5),
            fecha_nacimiento DATE,
            cargo VARCHAR(30),
            email VARCHAR(30),
            fecha_ingreso DATE NOT NULL,
            fecha_retiro DATE,
            salario DECIMAL(10,2),
            observaciones TEXT(250))           
            ''')
        miCursor.execute('''
            CREATE TABLE IF NOT EXISTS usuarios(
            idusuario INTEGER PRIMARY KEY NOT NULL,
            nombre VARCHAR(50) NOT NULL,
            apellidos VARCHAR(50) NOT NULL,
            usuario VARCHAR (50) NOT NULL,
            contrasena VARCHAR(50) NOT NULL,
            contrasena_autenticar VARCHAR(30),
            contrasena_facturar VARCHAR(30),
            fecha_registro DATE,
            idempleado INTEGER FOREIN KEY NOT NULL)
            ''')
        miCursor.execute('''
            CREATE TABLE IF NOT EXISTS proveedores(
            idproveedor INTEGER PRIMARY KEY NOT NULL,
            nombre CARCHAR(30) NOT NULL,
            apellidos VARCHAR(20) NOT NULL,            
            direccion VARCHAR(30),
            telefono_fijo VARCHAR (20),
            celular VARCHAR(20),
            email VARCHAR(30),
            fecha_registro DATE NOT NULL,
            idproducto INTEGER FOREIN KEY NOT NULL)
            ''')
        miCursor.execute('''
            CREATE TABLE IF NOT EXISTS clientes(
            idcliente INTEGER PRIMARY KEY NOT NULL,
            nombre VARCHAR(30) NOT NULL,
            apellidos VARCHAR(20) NOT NULL,
            direccion VARCHAR(30),
            telefono_fijo VARCHAR (20),
            celular VARCHAR(20),
            email VARCHAR(30),
            fecha_regisro DATE NOT NULL)
            ''')
        miCursor.execute('''
            CREATE TABLE IF NOT EXISTS productos(
            idproducto VARCHAR(50) PRIMARY KEY NOT NULL,
            nombre VARCHAR(100) NOT NULL,
            descripcion TEXT,
            marca VARCHAR(50) NOT NULL,
            precio DECIMAL(10,0) NOT NULL,
            costo DECIMAL (10,0),
            stok INTEGER,
            idproveedor INTEGER FOREIN KEY NOT NULL)     
            ''')
        miCursor.execute('''
            CREATE TABLE IF NOT EXISTS compras(
            idcompra INTEGER AUTO INCREMENT,
            fecha DATE NOT NULL,
            cantidad_pro INTEGER NOT NULL,
            total DECIMAL (10,2),
            idproveedor INTEGER FOREIN KEY NOT NULL)
            ''')
        miCursor.execute('''
            CREATE TABLE IF NOT EXISTS detcompras(
            iddetcompras INTEGER AUTO INCREMENT,
            cantidad_ind INTEGER NOT NULL,
            precio DECIMAL (10,2) NOT NULL,
            subtotal DECIMAL (10,2))
            ''')
        miCursor.execute('''
            CREATE TABLE IF NOT EXISTS ventas(
            idventa INTEGER AUTO INCREMENT,
            consecutivo INTEGER,
            fecha DATE,
            cantidad_dto INTEGER,
            total DECIMAL(10,2),
            idempleado INTEGER FOREIN KEY NOT NULL,
            idcliente INTEGER FOREIN KEY,
            idproducto FOREIN KEY VARCHAR(50) NOT NULL)
            ''')
       
        messagebox.showinfo("BBDD", "BBDD creada con exito")

    except:
        messagebox.showwarning("¡Atención!", "La BBDD ya existe")

    miConexion.close()

#-------CREACION DE LA PANTALLA 3 PARA ACCEDER A LA BASE DE DATOS desde la primera pantalla, SE PODRIA SUPRIMIR POR QUE ESTA FUNCION TAMBIEN ESTA EN LA PANTALLA 2 DE REGISTRO-------------------------    

def PantallaBBDD():
    global pantalla3
    pantalla3 = Toplevel(pantalla)
    pantalla3.geometry("400x250")
    pantalla3.title("Frolon Soluciones Tecnologicas")
    #pantalla3.iconbitmap("logo_rio.ico")
    #pantalla3.config(bg="red")
    pantalla3.resizable(False, False)

    Label(pantalla3, text="Por favor conecte la base de datos", bg="navy", fg="white", width="300", height="3", font=("calibri", 15)).pack()
    Label(pantalla3, text="").pack()

    Button(pantalla3, text="Conectar", height="3", width="30", command=conexionBBDD).pack()
    Label(pantalla3).pack()
    Button(pantalla3, text="Salir", height="3", width="30", command=salirAplicacion).pack()

#--------CREACION DE LA PANTALLA PRINCIPAL DE INICIO AL SISTEMA DE INFORMACION--------------.............-------------------

def menu_pantalla():
    global pantalla
    pantalla=Tk()
    pantalla.geometry("390x400")
    pantalla.title('Frolon "Soluciones Tecnologicas"')
    #pantalla.iconbitmap("logo_rio.ico")
    #pantalla.config(bg="lightgreen")
    pantalla.resizable(False, False)

    #image=PhotoImage(file="logotipo.gif")
    #image=image.subsample (4,5)
    #label=Label(image=image)
    #abel.pack()

    Label(text="Bienvenido \n Ingreso al Sistema", bg="navy", fg="white", width="300", height="2", font=("calibri", 15)).pack()
    Label(text="", height="4").pack()

    Button(text="Conectar la BBDD", height="2", width="30",  command = PantallaBBDD).pack()
    Label(text="").pack()

    Button(text="Iniciar Sesion", height="3", width="30", font=("impact", 13), command = inicio_sesion).pack()
    Label(text="").pack()

    #Button(text="Registrar un Nuevo Usuario", height="3", width="30", command = registrarUsuario).pack()
    #Label(text="").pack()

    pantalla.mainloop()

#------------------CREACION PANTALLA 1 Y FUNCIONES DE INICIO DE SESION------------------------------------------------------------------------------

def inicio_sesion():
    global pantalla1
    pantalla1 = Toplevel(pantalla)
    pantalla1.geometry("300x300")
    pantalla1.title("Inicio de Sesión")
    #pantalla1.iconbitmap("logo_rio.ico")
    #pantalla.config(bg="red")
    pantalla1.resizable(False, False)
    pantalla1.grab_set()

    Label(pantalla1, text="Ingrese su Usuario y Contraseña\n a continuación", bg="navy", fg="white", width="250", height="2", font=("calibri", 15)).pack()
    Label(pantalla1, text="").pack()

    global nombreusuario
    global contrasenausuario

    nombreusuario=StringVar()
    contrasenausuario=StringVar()

    global nombre_usuario_entry
    global contrasena_usuario_entry

    Label(pantalla1, text="Usuario", font=("calibri", 15)).pack()
    nombre_usuario_entry = Entry(pantalla1, font=("calibri", 15), textvariable=nombreusuario)
    nombre_usuario_entry.pack()
    nombre_usuario_entry.focus()
    Label(pantalla1).pack()

    Label(pantalla1, text="Contraseña", font=("calibri", 15)).pack()
    contrasena_usuario_entry = Entry(pantalla1, show="*", font=("calibri", 15), textvariable=contrasenausuario)
    contrasena_usuario_entry.pack()
    Label(pantalla1).pack()

    #Button(pantalla1, text="Aceptar", font=("Arial", 17), command=validacion_datos).pack()
    

    #Button(pantalla1, text="Aceptar", height="3", width="30", command=validacion_datos).pack()
    #Label(pantalla1).pack()
    #Button(pantalla1, text="Cancelar", height="3", width="30", command=cancelarAccion).pack()

    miFrame=Frame(pantalla1)
    miFrame.pack()

    botonAceptar=Button(miFrame, text="Aceptar", font=("Arial", 17), command=validacion_datos)
    botonAceptar.grid(row=1, column=0, sticky="e", padx=10, pady=10)

    botonCancelarr=Button(miFrame, text="Cancelar", font=("Arial", 17),  command=cancelarAccion)
    botonCancelarr.grid(row=1, column=1, sticky="e", padx=10, pady=10)

#---------------PANTALLA AUTENTICACION DE USURIOS PARA ACCEDER A LA TABLA DE USUARIO--------------------------

def autenticacionUsuario():
    global pantalla6
    pantalla6 = Toplevel(pantalla4)
    pantalla6.geometry("300x300")
    pantalla6.title("Autenticacion de usuario")
    #pantalla6.iconbitmap("logo_rio.ico")
    #pantalla6.config(bg="red")
    pantalla6.resizable(True, True)
    pantalla6.grab_set()
    
    Label(pantalla6, text="Ingrese su Usuario y Contraseña\n a continuación", bg="navy", fg="white", width="300", height="3", font=("calibri", 15)).pack()
    #Label(pantalla6, text="").pack()
    
    global nombreusuario
    global contrasenaautenticacion

    nombreusuario=StringVar()
    contrasenaautenticacion=StringVar()

    global nombre_usuario_entry
    global contrasena_autenticar_entry

    Label(pantalla6, text="Usuario",  height="2", width="10", font=("impact", 15)).place(x=20, y=90)
    nombre_usuario_entry = Entry(pantalla6, font=("Arial", 12), textvariable=nombreusuario)
    nombre_usuario_entry.place(x=130, y=105, height="27", width="130")
    nombre_usuario_entry.focus()

    Label(pantalla6, text="Contraseña",  height="2", width="10", font=("impact", 15)).place(x=20, y=130)
    contrasena_autenticar_entry = Entry(pantalla6, show="*", font=("Arial", 12), textvariable=contrasenaautenticacion)
    contrasena_autenticar_entry.place(x=130, y=145, height="27", width="130")

    Button(pantalla6, text="Continuar", height="1", width="10", font=("impact", 13), command=validacion_datos_autenticacion).place(x=40, y=215)
    Button(pantalla6, text="Cancelar", height="1", width="10", font=("impact", 13), command=cancelarAccionAutenticacion).place(x=150, y=215)
    
    '''miFrame=Frame(pantalla6)
    miFrame.pack()

    botonAceptar=Button(miFrame, text="Aceptar", font=("impact", 13), command=validacion_datos)
    botonAceptar.grid(row=1, column=0, sticky="e", padx=10, pady=130)

    botonCancelarr=Button(miFrame1, text="Cancelar", font=("impact", 13), command=cancelarAccion)
    botonCancelarr.grid(row=1, column=1, sticky="e", padx=10, pady=130)'''
   
    '''Label(pantalla6, text="Usuario").pack()
    nombre_usuario_entry = Entry(pantalla6, textvariable=nombreusuario_verify)
    nombre_usuario_entry.pack()
    Label(pantalla6).pack()

    Label(pantalla6, text="Contraseña autenticación").pack()
    contrasena_autenticar_entry = Entry(pantalla6, show="*", textvariable=contrasenaautenticacion_verify)
    contrasena_autenticar_entry.pack()
    Label(pantalla6).pack()

    Button(pantalla6, text="Continuar", command=validacion_datos_autenticacion).pack()'''


def autenticacionUsuarioEmpleado():
    global pantalla8
    pantalla8 = Toplevel(pantalla4)
    pantalla8.geometry("400x250")
    pantalla8.title("Autenticacion de usuario")
    #pantalla8.iconbitmap("logo_rio.ico")
    #pantalla8.config(bg="red")
    pantalla8.resizable(True, True)

    Label(pantalla8, text="Por favor ingrese su Usuario y Contraseña\n a continuación", bg="navy", fg="white", width="300", height="3", font=("calibri", 15)).pack()
    Label(pantalla8, text="").pack()

    global nombreusuario
    global contrasenaautenticacion

    nombreusuario=StringVar()
    contrasenaautenticacion=StringVar()

    #global nombre_usuario_entry
    #global contrasena_autenticar_entry

    Label(pantalla8, text="Usuario").pack()
    nombre_usuario = Entry(pantalla8, textvariable=nombreusuario)
    nombre_usuario.pack()
    Label(pantalla8).pack()

    Label(pantalla8, text="Contraseña autenticación").pack()
    contrasena_autenticar = Entry(pantalla8, show="*", textvariable=contrasenaautenticacion)
    contrasena_autenticar.pack()
    Label(pantalla8).pack()

    Button(pantalla8, text="Continuar", command=validacion_datos_autenticacionEmpleado).pack()


#-----------FUNCION QUE VALIDA USUARIO PARA ACEDER A LA BASE DE DATOS Y AL RESTO DEL SISTEMA-----------------------------------------------------------------

def validacion_datos():
    miConexion=sqlite3.connect("DDBBpruebaAbril.db")
    miCursor=miConexion.cursor()
    miCursor.execute("SELECT usuario FROM usuarios WHERE usuario = '"+nombreusuario.get()+"' and contrasena = '"+contrasenausuario.get()+"' ")
    if miCursor.fetchall():
        menuPrincipal()
        #messagebox.showinfo(title="Inicio sesión", message="Inicio de sesión exitoso")
    else:
        messagebox.showinfo(title="Inicio sesión", message="Usuario y/o contraseña incorrecta")
    miCursor.close()

def validacion_datos_autenticacion():
    miConexion=sqlite3.connect("DDBBpruebaAbril.db")
    miCursor=miConexion.cursor()
    miCursor.execute("SELECT usuario FROM usuarios WHERE usuario = '"+nombreusuario.get()+"' and contrasena_autenticar = '"+contrasenaautenticacion.get()+"' ")
    if miCursor.fetchall():
        registrarUsuario()
        #messagebox.showinfo(title="Inicio sesión", message="Inicio de sesión exitoso")
    else:
        messagebox.showinfo(title="Atenticacion", message="Usuario y/o contraseña incorrecta")
    miCursor.close()

def validacion_datos_autenticacionEmpleado():
    miConexion=sqlite3.connect("DDBBpruebaAbril.db")
    miCursor=miConexion.cursor()
    miCursor.execute("SELECT usuario FROM usuarios WHERE usuario = '"+nombreusuario.get()+"' and contrasena_autenticar = '"+contrasenaautenticacion.get()+"' ")
    if miCursor.fetchall():
        registrarEmpleado()
        #messagebox.showinfo(title="Inicio sesión", message="Inicio de sesión exitoso")
    else:
        messagebox.showinfo(title="Atenticacion", message="Usuario y/o contraseña incorrecta")
    miCursor.close()


#-----------FUNCION PARA CREAR LA PANTALLA DEL MENU PRINCIPAL PARA ACCEDER A TODAS LAS FUNCIONES DEL SISTEMA------------------------------

def menuPrincipal():
    global pantalla4
    pantalla.withdraw()
    pantalla1.withdraw()
    pantalla4=Toplevel(pantalla1)
    pantalla4.geometry("500x620")
    pantalla4.title("Menu Principal")
    #pantalla4.iconbitmap("logo_rio.ico")
    #pantalla4.config(bg="red")
    pantalla4.resizable(True, True)

    barraMenu=Menu(pantalla4)
    pantalla4.config(menu=barraMenu, width=300, height=300)

    bbddMenu=Menu(barraMenu, tearoff=0)
    bbddMenu.add_command(label="Conectar BBDD", command=conexionBBDD)
    bbddMenu.add_command(label="Salir", command=salirAplicacion)

    borrarMenu=Menu(barraMenu, tearoff=0)
    borrarMenu.add_command(label="Borrar campos")

    crudMenu=Menu(barraMenu, tearoff=0)
    crudMenu.add_command(label="Crear")
    crudMenu.add_command(label="Leer")
    crudMenu.add_command(label="Actualizar")
    crudMenu.add_command(label="Borrar")

    ayudaMenu=Menu(barraMenu, tearoff=0)
    ayudaMenu.add_command(label="Licencia")
    ayudaMenu.add_command(label="A cerca de...")

    barraMenu.add_cascade(label="Menu", menu=bbddMenu)
    barraMenu.add_cascade(label="Borrar", menu=borrarMenu)
    barraMenu.add_cascade(label="CRUD", menu=crudMenu)
    barraMenu.add_cascade(label="Ayuda", menu=ayudaMenu)

    Label(pantalla4, text="Componentes de la base de datos", bg="purple", fg="white", width="300", height="4", font=("calibri", 15)).pack()
    Label(pantalla4, text="", height="2").pack()

    miFrame=Frame(pantalla4)
    miFrame.pack()

    botonProducto=Button(miFrame, text="Productos",  height="1", width="15")
    botonProducto.grid(row=1, column=0, sticky="e", padx=10, pady=10)

    botonCliente=Button(miFrame, text="Clientes",  height="1", width="15")
    botonCliente.grid(row=1, column=1, sticky="e", padx=10, pady=10)

    botonProveedor=Button(miFrame, text="Proveedores", height="1", width="15")
    botonProveedor.grid(row=1, column=2, padx=10, pady=10)

    botonCompra=Button(miFrame, text="Compras", height="1", width="15")
    botonCompra.grid(row=2, column=0, padx=10, pady=10)

    botonVenta=Button(miFrame, text="Ventas", height="1", width="15")
    botonVenta.grid(row=2, column=1, padx=10, pady=10)

    botonEmpleado=Button(miFrame, text="Empleados", height="1", width="15", command = autenticacionUsuarioEmpleado)
    botonEmpleado.grid(row=2, column=2, padx=10, pady=10)

    botonUsuario=Button(miFrame,text="Usuarios", height="1", width="15", command = autenticacionUsuario)
    botonUsuario.grid(row=3, column=0, padx=10, pady=10)

    Label(pantalla4, text="Modulos principales del sistema ", bg="Aqua", fg="black", width="300", height="2", font=("calibri", 15)).pack()
    Label(pantalla4, text="", height="2").pack()
    
    #DDBB ferreteria1

    miFrame1=Frame(pantalla4)
    miFrame1.pack()

    #Button(miFrame1,text="Registrar Nuevo Usuario", height="3", width="30", command = registrarUsuario).pack()
    #Label(miFrame1, text="").pack()

    Button(miFrame1, text="Modificar la BBDD", height="2", width="30").pack()
    Label(miFrame1, text="").pack()

    Button(miFrame1, text="Consultar", height="2", width="30").pack()
    Label(miFrame1, text="").pack()

    Button(miFrame1, text="Facturar productos", height="2", width="30").pack()
    Label(miFrame1, text="").pack()

    pantalla.mainloop()

#-------------FUNCION PARA CREACION DE LA PANTALLA REGISTRO EMPLEADOS Y SUS CAMPOS--------------------------------------
   
def registrarEmpleado():
    global pantalla5
    pantalla5=Toplevel(pantalla4)
    pantalla8.withdraw()
    pantalla5.geometry("500x700")
    pantalla5.title("Empleados")
    #pantalla5.iconbitmap("logo_rio.ico")
    #pantalla5.config(bg="red")
    pantalla5.resizable(True, True)
    pantalla5.grab_set()

    
    barraMenu=Menu(pantalla5)
    pantalla5.config(menu=barraMenu, width=300, height=300)

    borrarMenu=Menu(barraMenu, tearoff=0)
    borrarMenu.add_command(label="Limpiar campos", command=limpiarCamposEmpleado)

    crudMenu=Menu(barraMenu, tearoff=0)
    crudMenu.add_command(label="Crear", command=crearEmpleado)
    crudMenu.add_command(label="Leer", command=leerEmpleado)
    crudMenu.add_command(label="Actualizar", command=actualizarEmpleado)
    crudMenu.add_command(label="Borrar", command=eliminarEmpleado)

    ayudaMenu=Menu(barraMenu, tearoff=0)
    ayudaMenu.add_command(label="Licencia")
    ayudaMenu.add_command(label="A cerca de...")

    barraMenu.add_cascade(label="Borrar", menu=borrarMenu)
    barraMenu.add_cascade(label="CRUD", menu=crudMenu)
    barraMenu.add_cascade(label="Ayuda", menu=ayudaMenu)
 
    Label(pantalla5, text="Ingrese nuevos empleados, consulte \ny actualice información en el sistema", bg="navy", fg="white", width="300", height="2", font=("calibri", 15)).pack()
    #Label(pantalla5, text="").pack()

    miFrame=Frame(pantalla5)
    miFrame.pack()

    global Idempleado
    global nombre
    global apellidos
    global direccion
    global telefono
    global celular
    global sexo
    global fechaNacimiento
    global cargo
    global email
    global fechaingreso
    global fecharetiro
    global salario
    global observaciones

    Idempleado=StringVar()
    nombre=StringVar()
    apellidos=StringVar()
    direccion=StringVar()
    telefono=StringVar()
    celular=StringVar()
    sexo=StringVar()
    fechaNacimiento=StringVar()
    cargo=StringVar()
    email=StringVar()
    fechaingreso=StringVar()
    fecharetiro=StringVar()
    salario=StringVar()
    observaciones=StringVar()
        
#-------------------AQUI COMIENZAN LOS TEXTOS LABEL DE LA PANTALLA ------------------------------------------

    idEmpleadoLabel=Label(miFrame, text="Id")
    idEmpleadoLabel.grid(row=0, column=0, padx=10, pady=10)

    NombreEmpleadoLabel=Label(miFrame, text="Nombre")
    NombreEmpleadoLabel.grid(row=1, column=0, padx=10, pady=10)

    ApellidosLabel=Label(miFrame, text="Apellidos")
    ApellidosLabel.grid(row=2, column=0, padx=10, pady=10)

    DireccionLabel=Label(miFrame, text="Direccion")
    DireccionLabel.grid(row=3, column=0, padx=10, pady=10)

    TelefonoLabel=Label(miFrame, text="Telefono fijo")
    TelefonoLabel.grid(row=4, column=0, padx=10, pady=10)

    CelularLabel=Label(miFrame, text="Numero de Celular")
    CelularLabel.grid(row=5, column=0, padx=10, pady=10)

    SexoLabel=Label(miFrame, text="Sexo")
    SexoLabel.grid(row=6, column=0, padx=10, pady=10)

    FechaNacimientoLabel=Label(miFrame, text="Fecha de nacimiento")
    FechaNacimientoLabel.grid(row=7, column=0, padx=10, pady=10)

    CargoLabel=Label(miFrame, text="Cargo")
    CargoLabel.grid(row=8, column=0, padx=10, pady=10)

    EmailLabel=Label(miFrame, text="Email")
    EmailLabel.grid(row=9, column=0, padx=10, pady=10)
 
    FechaIngresoLabel=Label(miFrame, text="Fecha de ingreso")
    FechaIngresoLabel.grid(row=10, column=0, padx=10, pady=10)

    FechaRetiroLabel=Label(miFrame, text="Fecha de Retiro")
    FechaRetiroLabel.grid(row=11, column=0, padx=10, pady=10)

    SalarioLabel=Label(miFrame, text="Salario")
    SalarioLabel.grid(row=12, column=0, padx=10, pady=10)

    ObservacionesLabel=Label(miFrame, text="Observaciones")
    ObservacionesLabel.grid(row=13, column=0, padx=10, pady=10)

#--------------------aqui comienza los campos Entry de la pantalla 5-----------------------------------------------------
    
    cuadroIdEmpleado=Entry(miFrame, textvariable=Idempleado)
    cuadroIdEmpleado.grid(row=0, column=1, padx=10, pady=10)

    cuadroNombre=Entry(miFrame, textvariable=nombre)
    cuadroNombre.grid(row=1, column=1, padx=10, pady=10)

    cuadroApellidos=Entry(miFrame, textvariable=apellidos)
    cuadroApellidos.grid(row=2, column=1, padx=10, pady=10)

    cuadroDireccion=Entry(miFrame, textvariable=direccion)
    cuadroDireccion.grid(row=3, column=1, padx=10, pady=10)

    cuadroTelefono=Entry(miFrame, textvariable=telefono)
    cuadroTelefono.grid(row=4, column=1, padx=10, pady=10)

    cuadroCelular=Entry(miFrame, textvariable=celular)
    cuadroCelular.grid(row=5, column=1, padx=10, pady=10)

    cuadroSexo=Entry(miFrame, textvariable=sexo)
    cuadroSexo.grid(row=6, column=1, padx=10, pady=10)

    cuadroFecha=Entry(miFrame, textvariable=fechaNacimiento)
    cuadroFecha.grid(row=7, column=1, padx=10, pady=10)

    cuadroCargo=Entry(miFrame, textvariable=cargo)
    cuadroCargo.grid(row=8, column=1, padx=10, pady=10)

    cuadroEmail=Entry(miFrame, textvariable=email)
    cuadroEmail.grid(row=9, column=1, padx=10, pady=10)

    cuadroFecha=Entry(miFrame, textvariable=fechaingreso)
    cuadroFecha.grid(row=10, column=1, padx=10, pady=10)

    cuadroFecha=Entry(miFrame, textvariable=fecharetiro)
    cuadroFecha.grid(row=11, column=1, padx=10, pady=10)

    cuadroSalario=Entry(miFrame, textvariable=salario)
    cuadroSalario.grid(row=12, column=1, padx=10, pady=10)

    cuadroObservaciones=Entry(miFrame, textvariable=observaciones)
    cuadroObservaciones.grid(row=13, column=1, padx=10, pady=10)

    
    miFrame1=Frame(pantalla5)
    miFrame1.pack()

    botonCrear=Button(miFrame1, text="Create", command=crearEmpleado)
    botonCrear.grid(row=1, column=0, sticky="e", padx=10, pady=10)

    botonBorrar=Button(miFrame1, text="Delete", command=eliminarEmpleado)
    botonBorrar.grid(row=1, column=2, sticky="e", padx=10, pady=10)

    botonLeer=Button(miFrame1, text="Read", command=leerEmpleado)
    botonLeer.grid(row=1, column=1, padx=10, pady=10)

    botonActualizar=Button(miFrame1, text="Update", command=actualizarEmpleado)
    botonActualizar.grid(row=1, column=3, padx=10, pady=10)

#-------------------------------CREACION DE LA PANTALLA 2 REGISTRO DE USUARIOS---------------------------------------------------------------------    

def registrarUsuario():
    global pantalla2
    pantalla6.withdraw()
    pantalla2=Toplevel(pantalla)
    pantalla2.geometry("400x530")
    pantalla2.title("Usuarios")
    #pantalla2.iconbitmap("logo_rio.ico")
    #pantalla2.config(bg="red")
    pantalla2.resizable(True, True)
    pantalla2.grab_set()
 
    Label(pantalla2, text="Ingresar, Actualizar, Consultar y Borrar \n información de Usuarios en el sistema", bg="navy", fg="white", width="300", height="2", font=("calibri", 15)).pack()
    Label(pantalla2, text="").pack()

#--------------COMIENZO BARRA MENU DE LA PANTALLA 2------------------------------------------------------------------

    barraMenu=Menu(pantalla2)
    pantalla2.config(menu=barraMenu, width=300, height=300)

    #bbddMenu=Menu(barraMenu, tearoff=0)
    #bbddMenu.add_command(label="Conectar", command=conexionBBDD)
    #bbddMenu.add_command(label="Salir", command=salirAplicacion)

    borrarMenu=Menu(barraMenu, tearoff=0)
    borrarMenu.add_command(label="Limpiar campos", command=limpiarCamposUsuarios)

    crudMenu=Menu(barraMenu, tearoff=0)
    crudMenu.add_command(label="Crear", command=crearusuario)
    crudMenu.add_command(label="Leer", command=leerUsuario)
    crudMenu.add_command(label="Actualizar", command=actualizar)
    crudMenu.add_command(label="Borrar", command=eliminar)

    ayudaMenu=Menu(barraMenu, tearoff=0)
    ayudaMenu.add_command(label="Licencia")
    ayudaMenu.add_command(label="A cerca de...")

    #barraMenu.add_cascade(label="BBDD", menu=bbddMenu)
    barraMenu.add_cascade(label="Borrar", menu=borrarMenu)
    barraMenu.add_cascade(label="CRUD", menu=crudMenu)
    barraMenu.add_cascade(label="Ayuda", menu=ayudaMenu)

#---------------COMIENZO DE CAMPOS-----------------------------------------------------------------------

    miFrame=Frame(pantalla2)
    miFrame.pack()

#------------------FUNCIONES PARA LOS CAMPOS DE TEXTO DE LA TABLA USUARIOS PANTALLA 2-------------------------------------------    

    global Id
    global nombre
    global apellidos
    global usuario
    global contrasena
    global contrasenaautenticacion
    global contrasenafacturar
    global fecharegistro
    global Idempleado
    
    Id=StringVar()
    nombre=StringVar()
    apellidos=StringVar()
    usuario=StringVar()
    contrasena=StringVar()
    contrasenaautenticacion=StringVar()
    contrasenafacturar=StringVar()
    fecharegistro=StringVar()
    Idempleado=StringVar()
    

#-----------AQUI COMIENZAN LOS CUADROS DE TEXTO DE LA PANTALLA 2---------------------------------------------------------------------------------- 
   
    cuadroId=Entry(miFrame, textvariable=Id)
    cuadroId.grid(row=0, column=1, padx=10, pady=10)

    cuadroNombre=Entry(miFrame, textvariable=nombre)
    cuadroNombre.grid(row=1, column=1, padx=10, pady=10)

    cuadroApellido=Entry(miFrame, textvariable=apellidos)
    cuadroApellido.grid(row=2, column=1, padx=10, pady=10)

    cuadroUsuario=Entry(miFrame, textvariable=usuario)
    cuadroUsuario.grid(row=3, column=1, padx=10, pady=10)

    cuadroContrasena=Entry(miFrame, textvariable=contrasena)
    cuadroContrasena.grid(row=4, column=1, padx=10, pady=10)
    cuadroContrasena.config(show="*")

    cuadroContrasenaAutenticar=Entry(miFrame, textvariable=contrasenaautenticacion)
    cuadroContrasenaAutenticar.grid(row=5, column=1, padx=10, pady=10)
    cuadroContrasenaAutenticar.config(show="*")

    cuadroContrasenaFacturar=Entry(miFrame, textvariable=contrasenafacturar)
    cuadroContrasenaFacturar.grid(row=6, column=1, padx=10, pady=10)
    cuadroContrasenaFacturar.config(show="*")

    cuadroFecha=Entry(miFrame, textvariable=fecharegistro)
    cuadroFecha.grid(row=7, column=1, padx=10, pady=10)

    cuadroIdEmpleado=Entry(miFrame, textvariable=Idempleado)
    cuadroIdEmpleado.grid(row=8, column=1, padx=10, pady=10)
    
#-------------------AQUI COMIENZAN LOS TEXTOS LABEL DE LA PANTALLA 2-----------------------------------------------------------------------------

    idLabel=Label(miFrame, text="Id usuario")
    idLabel.grid(row=0, column=0, padx=10, pady=10)

    nombreLabel=Label(miFrame, text="Nombre")
    nombreLabel.grid(row=1, column=0, padx=10, pady=10)

    apellidosLabel=Label(miFrame, text="Apellidos")
    apellidosLabel.grid(row=2, column=0, padx=10, pady=10)

    usuarioLabel=Label(miFrame, text="Usuario")
    usuarioLabel.grid(row=3, column=0, padx=10, pady=10)

    contrasenaLabel=Label(miFrame, text="Contraseña")
    contrasenaLabel.grid(row=4, column=0, padx=10, pady=10)

    contrasenaAutenticarLabel=Label(miFrame, text="Contraseña autenticación")
    contrasenaAutenticarLabel.grid(row=5, column=0, padx=10, pady=10)

    contrasenaFacturarLabel=Label(miFrame, text="Contraseña facturar")
    contrasenaFacturarLabel.grid(row=6, column=0, padx=10, pady=10)

    fingresoLabel=Label(miFrame, text="Fecha Registro")
    fingresoLabel.grid(row=7, column=0, padx=10, pady=10)

    idEmpleadoLabel=Label(miFrame, text="Id empleado")
    idEmpleadoLabel.grid(row=8, column=0, padx=10, pady=10)

    miFrame1=Frame(pantalla2)
    miFrame1.pack()

    botonCrear=Button(miFrame1, text="Crear", command=crearusuario)
    botonCrear.grid(row=1, column=0, sticky="e", padx=10, pady=10)

    botonBorrar=Button(miFrame1, text="Eliminar", command=eliminar)
    botonBorrar.grid(row=1, column=2, sticky="e", padx=10, pady=10)

    botonLeer=Button(miFrame1, text="Consultar", command=leerUsuario)
    botonLeer.grid(row=1, column=1, padx=10, pady=10)

    botonActualizar=Button(miFrame1, text="Actualizar", command=actualizar)
    botonActualizar.grid(row=1, column=3, padx=10, pady=10)


#---------FUNCION QUE PERMITE SALIR DE MANERA CORRECTA DE LA APLICACION Y DESTRUYE LAS VENTANAS DESDE EL MENU DE LA BASE DE DATOS--------------

def salirAplicacion():
    valor=messagebox.askquestion("Salir", "Seguro deseas salir de la aplicación")
    #if valor=="True":
    if valor=="yes":
        pantalla.destroy()

def cancelarAccion():
    valor=messagebox.askquestion("Salir", "Seguro deseas cancelar la operación")
    #if valor=="True":
    if valor=="yes":
        pantalla1.destroy()

def cancelarAccionAutenticacion():
    valor=messagebox.askquestion("Salir", "Seguro deseas cancelar la operación")
    #if valor=="True":
    if valor=="yes":
        pantalla6.destroy()

#-------FUNCION QUE PERMITE INSERTAR DATOS EN LAS TABLAS DE LA BBDD COMO ASIGNAR USUARIOS Y CONTRASEÑAS PARA VALIDACION ENTRE OTROA------------

def crearusuario():
    miConexion=sqlite3.connect("DDBBpruebaAbril.db")
    miCursor=miConexion.cursor()
    sql = "INSERT INTO usuarios     (idusuario, nombre, apellidos, usuario, contrasena, contrasena_autenticar, contrasena_facturar, fecha_registro, idempleado) VALUES ('{0}','{1}','{2}','{3}','{4}','{5}','{6}','{7}','{8}')".format(Id.get(), nombre.get(), apellidos.get(), usuario.get(),  contrasena.get(), contrasenaautenticacion.get(), contrasenafacturar.get(), fecharegistro.get(), Idempleado.get())
    
    try:
        miCursor.execute(sql)
        miConexion.commit()
        messagebox.showinfo("BBDD usuarios", "Regitro insertado con exito")    

    except:
        miConexion.rollback()
        messagebox.showinfo("BBDD usuarios", "No registrado")
    miConexion.close()


 
def crearEmpleado():
    miConexion=sqlite3.connect("DDBBpruebaAbril.db")
    miCursor=miConexion.cursor()

    sql = "INSERT INTO empleados (idempleado, nombre, apellidos, direccion, telefono_fijo, celular, sexo, fecha_nacimiento, cargo, email, fecha_ingreso, fecha_retiro, salario, observaciones) VALUES ('{0}','{1}','{2}','{3}','{4}','{5}','{6}','{7}','{8}','{9}','{10}','{11}','{12}','{13}')".format(Idempleado.get(), nombre.get(), apellidos.get(), direccion.get(),  telefono.get(), celular.get(), sexo.get(), fechaNacimiento.get(), cargo.get(), email.get(), fechaingreso.get(), fecharetiro.get(), salario.get(), observaciones.get())
    
    try:
        miCursor.execute(sql)
        miConexion.commit()
        messagebox.showinfo("BBDD Empleado", "Regitro insertado con exito")    

    except:
        miConexion.rollback()
        messagebox.showinfo("BBDD Empleado", "No registrado")
    miConexion.close()

#-------------------FUNCION QUE PERMITE LIMPIAR LOS CAMPOS DE LAS TABLAS EN LA tuple BBDD------------------------------------------

def limpiarCamposUsuarios():
    Id.set(""), nombre.set(""), apellidos.set(""), usuario.set(""), contrasena.set(""), contrasenaautenticacion.set(""),contrasenafacturar.set(""), fecharegistro.set(""), Idempleado.set("")

def limpiarCamposEmpleado():
    Idempleado.set(""), nombre.set(""), apellidos.set(""), direccion.set(""), telefono.set(""), celular.set(""), sexo.set(""), fechaNacimiento.set(""), cargo.set(""), email.set(""), fechaingreso.set(""), fecharetiro.set(""), salario.set(""), observaciones.set("")

#-------------------FRUNCION QUE PERMITE ELIMINAR DATOS INSERTADOS EN LAS TABLAS DE LA BBDD----------------------------------------------------------

def eliminar():
    miConexion=sqlite3.connect("DDBBpruebaAbril.db")
    miCursor=miConexion.cursor()
    miCursor.execute("DELETE FROM usuarios WHERE idusuario=" + Id.get())

    miConexion.commit()
    messagebox.showinfo("BBDD", "Registro borrado con éxito")

def eliminarEmpleado():
    miConexion=sqlite3.connect("DDBBpruebaAbril.db")
    miCursor=miConexion.cursor()
    miCursor.execute("DELETE FROM empleados WHERE idempleado=" + Idempleado.get())

    miConexion.commit()
    messagebox.showinfo("BBDD", "Registro borrado con éxito")

#------------------FUNCION QUE PERMITE RECUPERAR DATOS DE LA TABLA USUARIOS----------------------------------------------------------------------

def leerUsuario():
    miConexion=sqlite3.connect("DDBBpruebaAbril.db")
    miCursor=miConexion.cursor()
    miCursor.execute("SELECT * FROM usuarios WHERE idusuario=" + Id.get())
    elUsuario=miCursor.fetchall()
    for Usuario in elUsuario:
        
        Id.set(Usuario[0]), nombre.set(Usuario[1]), apellidos.set(Usuario[2]), usuario.set(Usuario[3]), 
        contrasena.set(Usuario[4]),  contrasenaautenticacion.set(Usuario[5]), contrasenafacturar.set(Usuario[6]), fecharegistro.set(Usuario[7])
        
    miConexion.commit()   

def leerEmpleado():
    miConexion=sqlite3.connect("DDBBpruebaAbril.db")
    miCursor=miConexion.cursor()
    miCursor.execute("SELECT * FROM empleados WHERE idempleado=" + Idempleado.get())
    elEmpleado=miCursor.fetchall()
    for empleado in elEmpleado:
        
        Idempleado.set(empleado[0]), nombre.set(empleado[1]), apellidos.set(empleado[2]), direccion.set(empleado[3]),
        telefono.set(empleado[4]), celular.set(empleado[5]), sexo.set(empleado[6]), fechaNacimiento.set(empleado[7]), cargo.set(empleado[8]), email.set(empleado[9]),  fechaingreso.set(empleado[10]), fecharetiro.set(empleado[11]), salario.set(empleado[12]), observaciones.set(empleado[13])

    miConexion.commit()  

#------------------------FUNCION QUE PERMITE ACTUALIZAR DATOS LAS TABLAS DE LA BBDD---------------------------------------------------------------

def actualizar():
    miConexion=sqlite3.connect("DDBBpruebaAbril.db")
    miCursor=miConexion.cursor()
    miCursor.execute("UPDATE usuarios SET nombre='"+nombre.get()+"', apellidos='"+apellidos.get ()+
        "', usuario='"+usuario.get()+"', contrasena='"+contrasena.get()+"', contrasena_autenticar='"+contrasenaautenticacion.get()+
        "', contrasena_facturar='"+contrasenafacturar.get()+"', fecha_registro='"+fecharegistro.get()+"' WHERE idusuario=" + Id.get())

    miConexion.commit()
    messagebox.showinfo("BBDD", "Registro actualizado con éxito")

def actualizarEmpleado():
    miConexion=sqlite3.connect("DDBBpruebaAbril.db")
    miCursor=miConexion.cursor()
    miCursor.execute("UPDATE empleados SET nombre='"+nombre.get()+"', apellidos='"+apellidos.get()+"', direccion='"+direccion.get()+
        "', telefono_fijo='"+telefono.get()+"', celular='"+celular.get()+"', sexo='"+sexo.get()+"', fecha_nacimiento='"+fechaNacimiento.get()+ "', cargo='"+cargo.get()+
        "', email='"+email.get()+"', fecha_ingreso='"+fechaingreso.get()+"', fecha_retiro='"+fecharetiro.get()+"', salario='"+salario.get()+ 
        "' WHERE idempleado=" + Idempleado.get())

    miConexion.commit()
    messagebox.showinfo("BBDD", "Registro actualizado con éxito")



menu_pantalla()