
import simpy
import random
import math


def proceso(env, tiempo, nombre, ram, memoria, instrucciones, instruccionesxtiempo):

    
    global tiempoIndividual
    global tiempoTOTAL

    
    
    yield env.timeout(tiempo)
    print('El nombre del proceso: %s la cantidad de memoriaoria  necesaria  es: %d el tiempo en el que entra es: %f ' % (nombre, memoria, env.now))

    
    tiempoLlegada = env.now 
    
    
    
    yield ram.get(memoria)
 




    condicion = 0    
    while condicion < 1:

    
        with cpu.request() as req:
            yield req
            
            if instrucciones>=instruccionesxtiempo:
                instrucciones = instrucciones - instruccionesxtiempo
                yield env.timeout(1)

            else:
                condicion=1

                

       
        entraEspera = random.randint(1,2)

        
        if entraEspera == 1:
            
        
            with waiting.request() as req2:
                yield req2
                
               
                yield env.timeout(1)                
                print('t: %f - %s (waiting) realizadas operaciones (i/o)' % (env.now, nombre))

 

    

    yield ram.put(memoria)
    print('t: %f - %s (terminated) finaliza, retorna -> %d de ram' % (env.now, nombre, memoria))


  
    tiempoIndividual.append(env.now - tiempoLlegada)
    tiempoTOTAL += (env.now - tiempoLlegada)+
    
tiempoIndividual=[]

memoriaRAM=100
instruccionesxtiempo = 3.0

tiempoTOTAL = 0.0 

cantProcesos = 25
env = simpy.Environment()

ram = simpy.Container(env, init=memoriaRAM, capacity=memoriaRAM) 

#COLA DE ACCESO PARA
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
