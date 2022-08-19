cursos=[]                                            #Lista de Cursos

#Leer el archivo y Crea lista de Cursos
def leer(ubicacion):                                 #Funcion leer que recibe la ubiacion de este 
    archivo = open(ubicacion,"r")                    #Abre el archivo
    for linea in archivo:                            #Lee linea a linea el archivo de cursos
        linea = linea.replace("\n","")               #Quita el salto de linea
        if linea=="":
            continue
        linea = linea.split(",")                     #Convierte los parametros del un curso en una lista
        verificar(linea)
        cursos.append(linea)                         #Agrega el curso
    archivo.close                                    #Cierra el archivo

#Verifica si se repite un curso
def verificar(linea):
    if len(cursos)!=0:                               #Pregunta si la lista se encuentra vacia
        for curso in cursos:                         #Toma un curso de la lista de cursos
            if curso[0]==linea[0]:                   #Verifica si se repite
                cursos.remove(curso)

#Busca Curso por codigo
def buscar(codigo):
    if len(cursos)!=0:
        for curso in cursos:
            if curso[0]==str(codigo):
                return curso
    return None

#Agrega y verifica si se repite un curso. Tambien Funciona para editar un curso 
def agregar(curso):
    verificar(curso)
    cursos.append(curso)

#Eliminar un curso por codigo y Devuel True si se elimino y False si no existe el elemento a eliminar
def eliminar(codigo):
    try:    
        cursos.remove(buscar(codigo))
        return True
    except ValueError:
        return False
        
#----------------------------------------------------------------------------------------------------------
#CONTEO DE CREDITOS

#Creditos aprobados
def aprobados():
    creditos=0
    if len(cursos)!=0:
        for curso in cursos:
            if int(curso[6])==0:
                creditos+=int(curso[5])
        return creditos
    return creditos

#Creditos Cursando
def cursando():
    creditos=0
    if len(cursos)!=0:
        for curso in cursos:
            if int(curso[6])==1:
                creditos+=int(curso[5])
        return creditos
    return creditos

#Creditos Pendientes
def pendientes():
    creditos=0
    if len(cursos)!=0:
        for curso in cursos:
            if int(curso[3])==1 and int(curso[6])==-1:
                creditos+=int(curso[5])
        return creditos
    return creditos

#Creditos hasta semestre N
def hasta_N(N):
    creditos=0
    if len(cursos)!=0:
        for curso in cursos:
            if int(curso[3])==1 and int(curso[4])<=N:
                creditos+=int(curso[5])
        return creditos
    return creditos

#Creditos del Semestre
def semestre(N):
    aprobados=0
    asignados=0
    pendientes=0

    if len(cursos)==0:
        return [0,0,0]

    for curso in cursos:
        if int(curso[4])!=N:
            continue
        match int(curso[6]):
            case 0 :
                aprobados+=int(curso[5])
            case 1 :
                asignados+=int(curso[5])
            case -1 :
                pendientes+=int(curso[5])
    return [aprobados,asignados,pendientes]      