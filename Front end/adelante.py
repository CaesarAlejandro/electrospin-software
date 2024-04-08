import machine
import boot

#Funcion que hace el motor moverse hacia adelante en secuencias de un paso completo.
def move_on1():
    boot.pinDir.on()
    boot.pinM0.off()
    boot.pinM1.off()
    boot.pinM2.off()

    for i in range(0 , 200):
        boot.pinStep.on()
        time.sleep_ms(10)
        boot.pinStep.off()
        time.sleep_ms(10)

#Funcion para la secuencia de medio paso (half)

def move_on2():
    boot.pinDir.on()
#Al activar solo el pin M0, segun la tabla de verdad del fabricante
#Obtenemos la secuencia de medio paso.
    boot.pinM0.on()
    boot.pinM1.off()
    boot.pinM2.off()

    for i in range(0 , 400):
        boot.pinStep.on()
        boot.time.sleep_ms(10)
        boot.pinStep.off()
        boot.time.sleep_ms(10)

#Funcion para secuencia de 1/4 de paso.

def move_on3():
    boot.pinDir.on()
    boot.pinM0.off()
    boot.pinM1.on()
    boot.pinM2.off()


    for i in range(0 , 800):
        boot.pinStep.on()
        time.sleep_ms(10)
        boot.pinStep.off()
        time.sleep_ms(10)


#Secuencia de 1/8 de pasos.

def move_on5():
    boot.pinDir.on()
    boot.pinM0.on()
    boot.pinM1.on()
    boot.pinM2.off()


    for i in range(0 , 1600):
        boot.pinStep.on()
        time.sleep_ms(10)
        boot.pinStep.off()
        time.sleep_ms(10)


#Secuencia de 1/16 de pasos.

def move_on6():
    boot.pinDir.on()
    boot.pinM0.on()
    boot.pinM1.on()
    boot.pinM2.on()


    for i in range(0 , 200):
        boot.pinStep.on()
        time.sleep_ms(10)
        boot.pinStep.off()
        time.sleep_ms(10)
