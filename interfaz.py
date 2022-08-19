from tkinter import *
from tkinter import ttk
from tkinter import filedialog
from tkinter.messagebox import showerror, showinfo, showwarning
from Cursos import *

class interfaz():
    def __init__(self):
        #conf Ventana
        self.menu = Tk()
        self.menu.resizable(False,False)
        self.menu.title("Menu")
        self.menu.geometry("500x500+"+str((self.menu.winfo_screenwidth()-500)//2)+"+"+str((self.menu.winfo_screenheight()-500)//2))
        self.menu.attributes("-topmost",True)
        #conf Frame
        self.marco=Frame(self.menu,borderwidth=10,relief="sunken")
        self.marco.place(x=20,y=20,width=460,height=460)
        #conf componentes del Frame
        self.info = Label(self.marco,text="Lenguajes Formales Y De Programacion\n\nNombre : Sergio Saul Ralda Mejia\n\nCarne : 202103216")
        self.info.place(x=95,y=20,width=250,height=100)
        self.bcargar=Button(self.marco,text="Cargar Archivo",command=self.ir_carga_archivo) 
        self.bcargar.place(x=170,y=150,width=100,height=25)
        self.bgestionar=Button(self.marco,text="Gestionar Cursos",command=self.ir_gestion_cursos)
        self.bgestionar.place(x=170,y=195,width=100,height=25)
        self.conteo=Button(self.marco,text="Conteo de Creditos",command=self.ir_conteo_creditos)
        self.conteo.place(x=160,y=240,width=120,height=25)
        self.salir=Button(self.marco,text="Salir",command=self.menu.destroy)
        self.salir.place(x=170,y=285,width=100,height=25)
        #Inicia la ventana Menu
        self.menu.mainloop()

        #Cierra el menu y abre ventana conteo de creditos
    def ir_conteo_creditos(self):
        self.menu.destroy()
        self.conteo_creditos()

        #Cierra conteo de creditos y regresa a menu
    def regresar_conteo(self):
        self.contar.destroy()
        interfaz()

        #Cuenta creditos hasta semestre N y corrobora que se un semestre valido
    def contar_hastN(self):
        try:
            N=int(self.Esemestre.get())
            if N<1:
                int("")
        except ValueError:
            self.lcanthastaN.config(text="---")
            showerror(title="Error",message="Semestre Invalido")
            return None
        creditos=str(hasta_N(N))
        self.lcanthastaN.config(text=creditos)
        showinfo(title="Mensaje",message="Creditos Contados con Exito")

        #Cuenta creditos del semestre N y corrobora que es un semestre valido
    def contar_N(self):
        try:
            N=int(self.Esemestre2.get())
            if N<1:
                int("")
        except ValueError:
            self.lcantN.config(text="---")
            showerror(title="Error",message="Semestre Invalido")
            return None
        creditos=semestre(N)
        creditos="#Aprobados: "+str(creditos[0])+"   #Asignados: "+str(creditos[1])+"   #Pendientes: "+str(creditos[2])
        self.lcantN.config(text=creditos)
        showinfo(title="Mensaje",message="Creditos Contados con Exito")

        #ventana de conteo de Creditos
    def conteo_creditos(self):
        #conf ventana
        self.contar= Tk()
        self.contar.resizable(False,False)
        self.contar.title("Conteo de Creditos")
        self.contar.geometry("500x500+"+str((self.contar.winfo_screenwidth()-500)//2)+"+"+str((self.contar.winfo_screenheight()-500)//2))
        self.contar.attributes("-topmost",True)
        #conf Frame
        marco=Frame(self.contar,border=10, relief="sunken")
        marco.place(x=20,y=20,width=460,height=460)
        #conf elementos
        bregresar=Button(marco,text="Regresar",command=self.regresar_conteo)
        bregresar.place(x=0,y=410,width=100,height=30)
        laprobados=Label(marco,text="Creditos Aprobados:")
        laprobados.place(x=125,y=55,width=110,height=30)
        self.lcantaprobados=Label(marco,text=str(aprobados()))
        self.lcantaprobados.place(x=255,y=55,width=50,height=30)
        lcursando=Label(marco,text="Creditos Cursando:")
        lcursando.place(x=125,y=105,width=110,height=30)
        self.lcantcursando=Label(marco,text=str(cursando()))
        self.lcantcursando.place(x=255,y=105,width=50,height=30)
        lpendientes=Label(marco,text="Creditos Pendientes:")
        lpendientes.place(x=125,y=155,width=110,height=30)
        self.lcantpendientes=Label(marco,text=str(pendientes()))
        self.lcantpendientes.place(x=255,y=155,width=50,height=30)
        lhastaN=Label(marco,text="Creditos Obligatorios Hasta Semestre N:")
        lhastaN.place(x=55,y=205,width=250,height=30)
        self.lcanthastaN=Label(marco,text="---")
        self.lcanthastaN.place(x=335,y=205,width=50,height=30)
        lsemestre=Label(marco,text="Semestre:")
        lsemestre.place(x=65,y=255,width=100,height=30)
        self.Esemestre=Entry(marco)
        self.Esemestre.place(x=195,y=255,width=50,height=30)
        Bcontar=Button(marco,text="Contar",command=self.contar_hastN)
        Bcontar.place(x=275,y=255,width=100,height=30)
        lN=Label(marco,text="Creditos del Semestre:")
        lN.place(x=10,y=305,width=115,height=30)
        self.lcantN=Label(marco,text="---")
        self.lcantN.place(x=125,y=305,width=315,height=30)
        lsemestre2=Label(marco,text="Semestre:")
        lsemestre2.place(x=65,y=355,width=100,height=30)
        self.Esemestre2=Entry(marco)
        self.Esemestre2.place(x=195,y=355,width=50,height=30)
        Bcontar2=Button(marco,text="Contar",command=self.contar_N)
        Bcontar2.place(x=275,y=355,width=100,height=30)
        #inicia la ventana de conteo de creditos
        self.contar.mainloop()
        

        #Cierra el menu y agre la ventana de cargar de archivo
    def ir_carga_archivo(self):
        self.menu.destroy()
        self.cargar("")

        #Cierra la ventana de carga y vuelve al Menu
    def regresar_menu(self):
        self.carga.destroy()
        interfaz()

        #Toma el directorio del archivo
    def seleccionar(self):
        self.carga.destroy()
        self.ruta=filedialog.askopenfilename(initialdir="/",title="Seleccionar Archivo",filetypes=(("LFP files","*.LFP"),("all files","*.*")))
        self.cargar(self.ruta)

        #Proceso para leer y almacenar los cursos del archivo
    def cargar_archivo(self,ruta):
        try:
            leer(ruta)
            #print("El Archivo Si Existe")
            showinfo(title="Mensaje",message="Archivo Cargado Correctamente")
            self.regresar_menu()
        except FileNotFoundError:
            #print("El Archivo No Existe")
            showerror(title="Error",message="El Archivo NO Existe")

    #Ventana Para cargar el archivo
    def cargar(self,ruta):
        #conf ventana
        self.carga = Tk()
        self.carga.resizable(False,False)
        self.carga.title("Seleccionar Archivo")
        self.carga.geometry("500x250+"+str((self.carga.winfo_screenwidth()-500)//2)+"+"+str((self.carga.winfo_screenheight()-250)//2))
        self.carga.attributes("-topmost",True)
        #conf Frame
        self.marco2=Frame(self.carga,border=10, relief="sunken")
        self.marco2.place(x=20,y=20,width=460,height=210)
        #Conf componentes
        self.bseleccionar=Button(self.marco2,text="...",command=self.seleccionar)
        self.bseleccionar.place(x=365,y=40,width=30,height=30)
        self.truta=Entry(self.marco2)
        self.truta.insert(0,ruta)
        self.truta.place(x=45,y=40,width=300,height=30)
        self.baceptar=Button(self.marco2,text="Cargar Archivo",command= lambda: self.cargar_archivo(self.truta.get()))
        self.baceptar.place(x=170,y=100,width=100,height=30)
        self.bregresar=Button(self.marco2,text="Regresar",command= self.regresar_menu)
        self.bregresar.place(x=0,y=160,width=100,height=30)
        #Inicia la ventana para cargar el Archivo
        self.carga.mainloop()

    #Cierra el menu y abre la ventana de gestion de cursos
    def ir_gestion_cursos(self):
        self.menu.destroy()
        self.gestion_cursos()
     
    #Cierra gestion y regresa a Menu
    def regresar_menu_gestion(self):
        self.gestion.destroy()
        interfaz()

    #Ventana de Gestion de Cursos
    def gestion_cursos(self):
        #conf ventana
        self.gestion = Tk()
        self.gestion.resizable(False,False)
        self.gestion.title("Gestionar Cursos")
        self.gestion.geometry("500x500+"+str((self.gestion.winfo_screenwidth()-500)//2)+"+"+str((self.gestion.winfo_screenheight()-500)//2))
        self.gestion.attributes("-topmost",True)
        #conf Frame
        self.marco3=Frame(self.gestion,border=10, relief="sunken")
        self.marco3.place(x=20,y=20,width=460,height=460)
        #conf Elementos Frame
        self.blistar=Button(self.marco3,text="Listas Cursos",command=self.ir_listar_cursos)
        self.blistar.place(x=170,y=115,width=100,height=30)
        self.bmostrar=Button(self.marco3,text="Mostrar Cursos",command=self.ir_mostrar_cursos)
        self.bmostrar.place(x=170,y=165,width=100,height=30)
        self.bagregar=Button(self.marco3,text="Agregar Curso",command=self.ir_agregar_curso)
        self.bagregar.place(x=170,y=215,width=100,height=30)
        self.beditar=Button(self.marco3,text="Editar Curso",command=self.ir_editar_curso)
        self.beditar.place(x=170,y=265,width=100,height=30)
        self.beliminar=Button(self.marco3,text="Eliminar Curso",command=self.ir_eliminar_curso)
        self.beliminar.place(x=170,y=315,width=100,height=30)
        self.bregresar2=Button(self.marco3,text="Regresar",command=self.regresar_menu_gestion)
        self.bregresar2.place(x=0,y=410,width=100,height=30)
        #Inicia la venta para Gestion de Archivos
        self.gestion.mainloop()

        #Cierra la ventana gestion y abre la ventana eliminar curso
    def ir_eliminar_curso(self):
        self.gestion.destroy()
        self.eliminar_curso()

        #Cierra eliminar curso y abre gestion de cursos
    def regresar_eliminar(self):
        self.eliminar.destroy()
        self.gestion_cursos()

        #Elimina el curso con el codigo ingresado
    def eliminar_elcurso(self):
        codigo=self.Ecodigo.get()
        if codigo!="":
            if eliminar(codigo):
                self.Ecodigo.delete(0,END)
                showinfo(title="Mensaje",message="Curso Eliminado con Exito")
            else:
                showerror(title="Error",message="El Curso no Existe")
        else:
            showwarning(title="Advertencia",message="Ingrese un Codigo")

        #Ventana Para eliminar el curso
    def eliminar_curso(self):
        #conf ventana
        self.eliminar=Tk()
        self.eliminar.resizable(False,False)
        self.eliminar.title("Eliminar Curso")
        self.eliminar.geometry("500x200+"+str((self.eliminar.winfo_screenwidth()-500)//2)+"+"+str((self.eliminar.winfo_screenheight()-200)//2))
        self.eliminar.attributes("-topmost",True)
        #conf Frame
        self.marco6=Frame(self.eliminar,border=10, relief="sunken")
        self.marco6.place(x=20,y=20,width=460,height=160)
        #cont elementos
        lcodigo=Label(self.marco6,text="Codigo del Curso")
        lcodigo.place(x=70,y=35,width=100,height=30)
        self.Ecodigo=Entry(self.marco6)
        self.Ecodigo.place(x=210,y=35,width=150,height=30)
        Beliminar=Button(self.marco6,text="Eliminar",command=self.eliminar_elcurso)
        Beliminar.place(x=170,y=75,width=100,height=30)
        Bregresar=Button(self.marco6,text="Regresar",command=self.regresar_eliminar)
        Bregresar.place(x=0,y=110,width=100,height=30)
        #Inicia la ventana eliminar curso
        self.eliminar.mainloop()

        #Cierra la ventana gestion y abre la ventana editar curso
    def ir_editar_curso(self):
        self.gestion.destroy()
        self.editar_curso()

        #Cierra la ventana editar y regresa a gestion de cursos
    def regresar_editar(self):
        self.editar.destroy()
        self.gestion_cursos()

        #Buscar el curso que se quiere editar y lo muestra
    def buscar_editar(self):
        if self.Ecodigo.get()!="":
            curso=buscar(self.Ecodigo.get())
            if curso!=None:
                #Limpia las entradas
                self.Enombre.delete(0,END)
                self.Eprerequisito.delete(0,END)
                self.Eobligatorio.delete(0,END)
                self.Esemestre.delete(0,END)
                self.Ecreditos.delete(0,END)
                self.Eestado.delete(0,END)
                #agregar a las entradas
                self.Enombre.insert(0,curso[1])
                self.Eprerequisito.insert(0,curso[2])
                self.Eobligatorio.insert(0,curso[3])
                self.Esemestre.insert(0,curso[4])
                self.Ecreditos.insert(0,curso[5])
                self.Eestado.insert(0,curso[6])
            else:
                showwarning(title="Advertencia", message="Curso No Encontrado")
        else:
            showwarning(title="Advertencia",message="Ingrese Un Codigo")

        #Buscar el curso y lo edita
    def editar_elcurso(self):
        codigo=self.Ecodigo.get()
        if codigo!="":
            curso=buscar(codigo)
            if curso!=None:
                curso=[codigo,self.Enombre.get(),self.Eprerequisito.get(),self.Eobligatorio.get(),self.Esemestre.get(),self.Ecreditos.get(),self.Eestado.get()]
                agregar(curso)
                self.Ecodigo.delete(0,END)
                self.Enombre.delete(0,END)
                self.Eprerequisito.delete(0,END)
                self.Eobligatorio.delete(0,END)
                self.Esemestre.delete(0,END)
                self.Ecreditos.delete(0,END)
                self.Eestado.delete(0,END)
                showinfo(title="Mensaje",message="Curso Editado Con Exito")
            else:
                showwarning(title="Advertencia",message="El curso no Existe")
        else:
            showwarning(title="Advertencia",message="Ingrese un Codigo")


        #Ventana para editar curso
    def editar_curso(self):
        #conf venta
        self.editar = Tk()
        self.editar.resizable(False,False)
        self.editar.title("Editar Curso")
        self.editar.geometry("500x500+"+str((self.editar.winfo_screenwidth()-500)//2)+"+"+str((self.editar.winfo_screenheight()-500)//2))
        self.editar.attributes("-topmost",True)
        #conf Frame
        self.marco6=Frame(self.editar,border=10, relief="sunken")
        self.marco6.place(x=20,y=20,width=460,height=460)
        #conf elementos
        self.lcodigo=Label(self.marco6,text="Codigo")
        self.lcodigo.place(x=50,y=30,width=100,height=30)
        self.Ecodigo=Entry(self.marco6)
        self.Ecodigo.place(x=160,y=30,width=100,height=30)
        self.Bbuscar=Button(self.marco6,text="Buscar",command=self.buscar_editar)
        self.Bbuscar.place(x=270,y=30,width=100,height=30)
        self.lnombre=Label(self.marco6,text="Nombre")
        self.lnombre.place(x=55,y=80,width=100,height=30)
        self.Enombre=Entry(self.marco6)
        self.Enombre.place(x=185,y=80,width=200,height=30)
        self.lprerequisito=Label(self.marco6,text="Pre Requisito")
        self.lprerequisito.place(x=55,y=130,width=100,height=30)
        self.Eprerequisito=Entry(self.marco6)
        self.Eprerequisito.place(x=185,y=130,width=200,height=30)
        self.lobligatorio=Label(self.marco6,text="Obligatorio")
        self.lobligatorio.place(x=55,y=180,width=100,height=30)
        self.Eobligatorio=Entry(self.marco6)
        self.Eobligatorio.place(x=185,y=180,width=200,height=30)
        self.lsemestre=Label(self.marco6,text="Semestre")
        self.lsemestre.place(x=55,y=230,width=100,height=30)
        self.Esemestre=Entry(self.marco6)
        self.Esemestre.place(x=185,y=230,width=200,height=30)
        self.lcreditos=Label(self.marco6,text="Creditos")
        self.lcreditos.place(x=55,y=280,width=100,height=30)
        self.Ecreditos=Entry(self.marco6)
        self.Ecreditos.place(x=185,y=280,width=200,height=30)
        self.lestado=Label(self.marco6,text="Estado")
        self.lestado.place(x=55,y=330,width=100,height=30)
        self.Eestado=Entry(self.marco6)
        self.Eestado.place(x=185,y=330,width=200,height=30)
        self.beditar_curso=Button(self.marco6,text="Editar",command=self.editar_elcurso)
        self.beditar_curso.place(x=170,y=380,width=100,height=30)
        self.bregresar_editar=Button(self.marco6,text="Regresar",command=self.regresar_editar)
        self.bregresar_editar.place(x=0,y=410,width=100,height=30)
        #iniciar ventana editar curso
        self.editar.mainloop()


        #Cierra gestion de curso y abre agregar curso
    def ir_agregar_curso(self):
        self.gestion.destroy()
        self.agregar_curso()

        #Cierra agregar curso y regresa a gestion de cursos
    def regresar_gestion_agregar(self):
        self.agregar.destroy()
        self.gestion_cursos()

        #Agregar curso a la lista de cursos y verifica que no se repita
    def insertar_curso(self):
        curso=[self.Ecodigo.get(),self.Enombre.get(),self.Eprerequisito.get(),self.Eobligatorio.get(),self.Esemestre.get(),self.Ecreditos.get(),self.Eestado.get()]
        #for dato in curso:
            #if dato=="":
                #showwarning(title="Advertencia",message="Rellene Todos los Campos")
                #return None
        if curso[0]=="":
            showwarning(title="Advertencia",message="Ingrese Un Codigo Como Minimo")
            return None
        agregar(curso)
        self.Ecodigo.delete(0,END)
        self.Enombre.delete(0,END)
        self.Eprerequisito.delete(0,END)
        self.Eobligatorio.delete(0,END)
        self.Esemestre.delete(0,END)
        self.Ecreditos.delete(0,END)
        self.Eestado.delete(0,END)
        showinfo(title="Mensaje",message="Curso Aagregado con Exito")

    #Ventana para Agegar curso
    def agregar_curso(self):
        #conf venta
        self.agregar = Tk()
        self.agregar.resizable(False,False)
        self.agregar.title("Agregar Curso")
        self.agregar.geometry("500x500+"+str((self.agregar.winfo_screenwidth()-500)//2)+"+"+str((self.agregar.winfo_screenheight()-500)//2))
        self.agregar.attributes("-topmost",True)
        #conf Frame
        self.marco6=Frame(self.agregar,border=10, relief="sunken")
        self.marco6.place(x=20,y=20,width=460,height=460)
        #conf elementos
        self.lcodigo=Label(self.marco6,text="Codigo")
        self.lcodigo.place(x=55,y=30,width=100,height=30)
        self.Ecodigo=Entry(self.marco6)
        self.Ecodigo.place(x=185,y=30,width=200,height=30)
        self.lnombre=Label(self.marco6,text="Nombre")
        self.lnombre.place(x=55,y=80,width=100,height=30)
        self.Enombre=Entry(self.marco6)
        self.Enombre.place(x=185,y=80,width=200,height=30)
        self.lprerequisito=Label(self.marco6,text="Pre Requisito")
        self.lprerequisito.place(x=55,y=130,width=100,height=30)
        self.Eprerequisito=Entry(self.marco6)
        self.Eprerequisito.place(x=185,y=130,width=200,height=30)
        self.lobligatorio=Label(self.marco6,text="Obligatorio")
        self.lobligatorio.place(x=55,y=180,width=100,height=30)
        self.Eobligatorio=Entry(self.marco6)
        self.Eobligatorio.place(x=185,y=180,width=200,height=30)
        self.lsemestre=Label(self.marco6,text="Semestre")
        self.lsemestre.place(x=55,y=230,width=100,height=30)
        self.Esemestre=Entry(self.marco6)
        self.Esemestre.place(x=185,y=230,width=200,height=30)
        self.lcreditos=Label(self.marco6,text="Creditos")
        self.lcreditos.place(x=55,y=280,width=100,height=30)
        self.Ecreditos=Entry(self.marco6)
        self.Ecreditos.place(x=185,y=280,width=200,height=30)
        self.lestado=Label(self.marco6,text="Estado")
        self.lestado.place(x=55,y=330,width=100,height=30)
        self.Eestado=Entry(self.marco6)
        self.Eestado.place(x=185,y=330,width=200,height=30)
        self.bagregar_curso=Button(self.marco6,text="Agregar",command=self.insertar_curso)
        self.bagregar_curso.place(x=170,y=380,width=100,height=30)
        self.bregresar_agregar=Button(self.marco6,text="Regresar",command=self.regresar_gestion_agregar)
        self.bregresar_agregar.place(x=0,y=410,width=100,height=30)
        #iniciar ventana agregar curso
        self.agregar.mainloop()

        #Cierra Gestion y Abre mostrar cursos
    def ir_mostrar_cursos(self):
        self.gestion.destroy()
        self.mostrar_cursos()

        #Regresa a gestion de cursos y cierra mostrar cursos
    def regresar_gestion_mostrar(self):
        self.mostrar.destroy()
        self.gestion_cursos()

        #Buscar el curso y lo inserta en la tabla
    def buscar_curso(self):
        registros=self.tabla2.get_children()
        for registro in registros:
            self.tabla2.delete(registro)
        self.curso=buscar(self.codigo.get())
        if self.curso!=None:
            self.obligatorio=lambda a=str(self.curso[3]): "Si" if (a=="1") else "No"
            self.estado=lambda a=str(self.curso[6]): "Aprobado" if (a=="0") else ("Cursando" if (a=="1") else "Pendiente")
            self.prerrequisito=lambda a=str(self.curso[2]): str(self.curso[2]) if(a!="") else "Ninguno"
            self.tabla2.insert("",END,text=str(self.curso[0]),values=(str(self.curso[1]),self.prerrequisito(),self.obligatorio(),str(self.curso[4]),str(self.curso[5]),self.estado()))
        else:
            showerror(title="Error",message="Curso No Econtrado")

        #Mouestra el curso por codigo
    def mostrar_cursos(self):
        #conf vetana
        self.mostrar= Tk()
        self.mostrar.resizable(False,False)
        self.mostrar.title("Mostrar Cursos")
        self.mostrar.geometry("980x240+"+str((self.mostrar.winfo_screenwidth()-980)//2)+"+"+str((self.mostrar.winfo_screenheight()-240)//2))
        self.mostrar.attributes("-topmost",True)
        #conf Frame
        self.marco5=Frame(self.mostrar,border=10, relief="sunken")
        self.marco5.place(x=20,y=20,width=940,height=160)
        #conf componentes
        self.codigo=Entry(self.marco5)
        self.codigo.place(x=365,y=15,width=60,height=30)
        self.buscar=Button(self.marco5,text="Buscar Curso",command=self.buscar_curso)
        self.buscar.place(x=455,y=15,width=100,height=30)
        self.tabla2=ttk.Treeview(self.marco5,columns=("#1","#2","#3","#4","#5","#6"))
        self.tabla2.column("#0",width=70,anchor=CENTER)
        self.tabla2.heading("#0",text="CODIGO")
        self.tabla2.column("#1",anchor=CENTER,width=250)
        self.tabla2.heading("#1",text="NOMBRE")
        self.tabla2.column("#2",anchor=CENTER,width=250)
        self.tabla2.heading("#2",text="PRERREQUISITOS") 
        self.tabla2.column("#3",anchor=CENTER,width=90)
        self.tabla2.heading("#3",text="OBLIGATORIO")
        self.tabla2.column("#4",anchor=CENTER,width=70)
        self.tabla2.heading("#4",text="SEMESTRE")
        self.tabla2.column("#5",anchor=CENTER,width=70)
        self.tabla2.heading("#5",text="CREDITOS")
        self.tabla2.column("#6",anchor=CENTER,width=120)
        self.tabla2.heading("#6",text="ESTADO")
        self.tabla2.place(x=0,y=65,height=60)
        self.regresarmostrar=Button(self.mostrar,text="Regresar",command=self.regresar_gestion_mostrar)
        self.regresarmostrar.place(x=440,y=195,width=100,height=30)
        #Inicia la venta para mostrar curso
        self.mostrar.mainloop()


        #Cerrar gestion y abrir listado de cursos
    def ir_listar_cursos(self):
        self.gestion.destroy()
        self.listar_cursos()

        #Cerrar listado de cursos y regresar a gestion
    def regresar_gestion(self):
        self.listar.destroy()
        self.gestion_cursos()

    def listar_cursos(self):
        #conf ventana
        self.listar = Tk()
        self.listar.resizable(False,False)
        self.listar.title("Listado de Cursos")
        self.listar.geometry("980x640+"+str((self.listar.winfo_screenwidth()-980)//2)+"+"+str((self.listar.winfo_screenheight()-600)//2))
        self.listar.attributes("-topmost",True)
        #conf Frame
        self.marco4=Frame(self.listar,border=10, relief="sunken")
        self.marco4.place(x=20,y=20,width=942,height=560)
        #conf tabla y boton Regresar
        self.tabla=ttk.Treeview(self.marco4,columns=("#1","#2","#3","#4","#5","#6"))
        self.tabla.column("#0",width=70,anchor=CENTER)
        self.tabla.heading("#0",text="CODIGO")
        self.tabla.column("#1",anchor=CENTER,width=250)
        self.tabla.heading("#1",text="NOMBRE")
        self.tabla.column("#2",anchor=CENTER,width=250)
        self.tabla.heading("#2",text="PRERREQUISITOS") 
        self.tabla.column("#3",anchor=CENTER,width=90)
        self.tabla.heading("#3",text="OBLIGATORIO")
        self.tabla.column("#4",anchor=CENTER,width=70)
        self.tabla.heading("#4",text="SEMESTRE")
        self.tabla.column("#5",anchor=CENTER,width=70)
        self.tabla.heading("#5",text="CREDITOS")
        self.tabla.column("#6",anchor=CENTER,width=120)
        self.tabla.heading("#6",text="ESTADO")
        self.bregresar_gestion=Button(self.listar,text="Regresar",command=self.regresar_gestion)
        self.bregresar_gestion.place(x=440,y=595,width=100,height=30)
        for curso in cursos:
            self.obligatorio=lambda a=str(curso[3]): "Si" if (a=="1") else "No"
            self.estado=lambda a=str(curso[6]): "Aprobado" if (a=="0") else ("Cursando" if (a=="1") else "Pendiente")
            self.prerrequisito=lambda a=str(curso[2]): str(curso[2]) if(a!="") else "Ninguno"
            self.tabla.insert("",END,text=str(curso[0]),values=(str(curso[1]),self.prerrequisito(),self.obligatorio(),str(curso[4]),str(curso[5]),self.estado()))
        self.tabla.place(x=0,y=0,height=540)
        #Inicia la ventana para el listado de cursos
        self.listar.mainloop()

interfaz()