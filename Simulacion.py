#UNIVERSIDAD DEL VALLE DE GUATEMALA
#NOMBRE: BORIS CIFUENTES DE LEON CARNET: 14150 (TRABAJE INDIVIDUAL, LYENETTE ME AUTORIZO)
#ALGORITMOS Y ESTRUCTURAS DE DATOS
#HOJA DE TRABAJO #5
#FECHA: 27/08/2015

#LIMBRERIAS USADAS PARA LA EJECUCION CORRECTA DEL PROGRAMA
import simpy
import random
import math


def proceso(env, tiempo, nombre, ram, memoria, instrucciones, instruccionesxtiempo):

    #SE USAN PARA GUARDAR EL TIEMPO DE EJECUCUION DE CADA PROCESO
    global tiempoIndividual
    global tiempoTOTAL

    
    #TIEMPO DE INGRESO DEL PROCESO
    yield env.timeout(tiempo)
    print('El nombre del proceso: %s la cantidad de memoriaoria  necesaria  es: %d el tiempo en el que entra es: %f ' % (nombre, memoria, env.now))

    #TIEMPO DEL PROCESO
    tiempoLlegada = env.now 
    
    
    #MEMORIA DEL PROCESO
    yield ram.get(memoria)
 



    #CICLO PARA EJECUTAR LAS INSTURCCIONES DEL PROCESO
    condicion = 0    
    while condicion < 1:

    
        with cpu.request() as req:
            yield req
            
            if instrucciones>=instruccionesxtiempo:
                instrucciones = instrucciones - instruccionesxtiempo
                yield env.timeout(1)

            else:
                condicion=1

                

       #ESPERA 
        entraEspera = random.randint(1,2)

        #TIEMPO DE ESPERA 1 VA DIRECTO AL WAITNG
        if entraEspera == 1:
            
         #WAITING
            with waiting.request() as req2:
                yield req2
                
                #suponemos espera de 1 unidad de tiempo en cola de operaciones i/o
                yield env.timeout(1)                
                print('t: %f - %s (waiting) realizadas operaciones (i/o)' % (env.now, nombre))

 

    

    yield ram.put(memoria)
    print('t: %f - %s (terminated) finaliza, retorna -> %d de ram' % (env.now, nombre, memoria))


  
    tiempoIndividual.append(env.now - tiempoLlegada)
    tiempoTOTAL += (env.now - tiempoLlegada)  


#LISTA
tiempoIndividual=[]
#MEMORIA DEL CPU QUE SE MANIPULA
memoriaRAM=100
#INSTRUCCIONES POR UNIDAD DE TIEMPO SE MANIPULA
instruccionesxtiempo = 3.0
#TIEMPO DE LOS PROCESOS
tiempoTOTAL = 0.0 

#PROCESOS A EJECUTAR
cantProcesos = 25

#SE CREA SIMULACION
env = simpy.Environment()

#COLA DE LA MEMORIA RAM
ram = simpy.Container(env, init=memoriaRAM, capacity=memoriaRAM) 

#COLA DE ACCESO PARA CPU
cpu = simpy.Resource (env, capacity=1)
#COLA PARA ACCESO A OPERACIONES
waiting = simpy.Resource (env, capacity=1) 

#CREA SEMILLA USADA EN RANDOM
random.seed(40)

#SE MANIPULA EL INTERVALO
interval = 10


#CICLO PARA CREAR LA CANTIDAD DE PROCESOS
for i in range(cantProcesos):
    tiempo = random.expovariate(1.0 / interval)
    #CANTIDAD DE INSTRUCCIONES
    instrucciones = random.randint(1,10)
    #CANTDAD DE MEMORIA
    memoria = random.randint(1,10) 
    env.process(proceso(env, tiempo, 'Proceso %d' % i, ram, memoria, instrucciones, instruccionesxtiempo))

#SE CORRE SIMULACION
env.run()
print "El PROMEDIO DE TIEMPO ES ", tiempoTOTAL / cantProcesos

#DESVIACION ESTANDAR
temp=0
for i in tiempoIndividual:
    temp+=(i-(tiempoTOTAL / cantProcesos))**2

des=math.sqrt(temp/cantProcesos)
print "LA DESVIACION ESTANDAR ES: ", des
