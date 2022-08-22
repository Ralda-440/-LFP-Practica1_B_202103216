
cursos=[]     #Lista de Cursos


#Leer el archivo y Crea la lista de Cursos

def leer(ubicacion):                                    #Funcion leer que recibe como parámetro la ubicación del archivo 
    archivo = open(ubicacion,"r",encoding="utf-8")      #Abre el archivo
    for linea in archivo:                               #Lee línea a línea el archivo de cursos
        linea = linea.replace("\n","")                  #Quita el salto de línea
        if linea=="":                                   #Verifica que la línea no se encuentra vacía
            continue                                    #Si la línea esta vacía pasa al siguiente ciclo
        linea = linea.split(",")                        #Convierte los parámetros de un curso en una lista
        verificar(linea)
        cursos.append(linea)                            #Agrega el curso
    archivo.close                                       #Cierra el archivo

#Verifica si se repite un curso

def verificar(linea):
    if len(cursos)!=0:                               #Pregunta si la lista se encuentra vacía
        for curso in cursos:                         #Toma un curso de la lista de cursos
            if curso[0]==linea[0]:                   #Verifica si se repite
                cursos.remove(curso)                 #Si se repite elimina el curso de la lista

#Busca Curso por Código

def buscar(codigo):
    if len(cursos)!=0:                     #Verifica si la lista de cursos esta vacía
        for curso in cursos:               #Recorre la lista de cursos
            if curso[0]==str(codigo):      #Verifica el Código del curso
                return curso               #Si el curso coincide lo devuelve
    return None                            #Si el curso no existe devuelve None

#Agregar Curso

def agregar(curso):
    verificar(curso)        #Verifica si el curso existe
    cursos.append(curso)    

#Eliminar un curso por Código 

def eliminar(codigo):                   
    try:    
        cursos.remove(buscar(codigo))     #Busca y elimina el curso con el Código
        return True                       #Retorna True si fue eliminado con éxito
    except ValueError:
        return False                      #Retorna False indicando que el curso no existe
        
#----------------------------------------------------------------------------------------------------------
#CONTEO DE CREDITOS

#Creditos aprobados

def aprobados():
    creditos=0 
    if len(cursos)!=0:                     #Verifica si la lista esta vacía
        for curso in cursos:               #Recorre la lista cursos
            if int(curso[6])==0:           #Verifica que el curso este aprobado
                creditos+=int(curso[5])    #Si esta aprobado suma los créditos
        return creditos                    #Retorna los créditos totales
    return creditos                        #Retorna créditos que vale cero 

#Creditos Cursando

def cursando():
    creditos=0
    if len(cursos)!=0:                     #Verifica si la lista esta vacía
        for curso in cursos:               #Recorre la lista cursos
            if int(curso[6])==1:           #Verifica que el curso este en estado cursando
                creditos+=int(curso[5])    #Si se esta cursando suma los créditos
        return creditos                    #Retorna los créditos totales
    return creditos                        #Retorna créditos que vale cero 

#Creditos Pendientes

def pendientes():
    creditos=0
    if len(cursos)!=0:                                  #Verifica si la lista esta vacía
        for curso in cursos:                            #Recorre la lista cursos
            if int(curso[3])==1 and int(curso[6])==-1:  #Verifica que el curso este en estado pendiente y que sea obligatorio 
                creditos+=int(curso[5])                 #Suma los créditos
        return creditos                                 #Retorna los créditos totales
    return creditos                                     #Retorna créditos que vale cero 

#Creditos hasta semestre N

def hasta_N(N):
    creditos=0                                  
    if len(cursos)!=0:                                 #Verifica si la lista esta vacía
        for curso in cursos:                           #Recorre la lista cursos
            if int(curso[3])==1 and int(curso[4])<=N:  #Verifica que el curso sea obligatorio y el semestre menor o igual a N
                creditos+=int(curso[5])                #Suma los créditos
        return creditos                                #Retorna los créditos totales
    return creditos                                    #Retorna créditos que vale cero

#Creditos del Semestre

def semestre(N):
    aprobados=0
    asignados=0
    pendientes=0

    if len(cursos)==0:                          #Verifica si la lista esta vacía
        return [0,0,0]                          #Retorna una lista que indica cero creditos

    for curso in cursos:                        #Recorre la lista cursos
        if int(curso[4])!=N:                    #Verifica que el curso pertenezca al semestre
            continue                            #Si no pertenece pasa al siguiente curso
        match int(curso[6]):                    #Verifica eel Estado del curso
            case 0 :
                aprobados+=int(curso[5])        #Suma los créditos si esta aprobado
            case 1 :
                asignados+=int(curso[5])        #Suma los créditos si esta cursando
            case -1 :
                pendientes+=int(curso[5])       #Suma los créditos si esta pendiente
    return [aprobados,asignados,pendientes]     #Retorna la suma total en una lista