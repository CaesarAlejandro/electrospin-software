import machine
import Config
pin2 = Pin(2, Pin.OUT)
#Funcion que hace el motor moverse hacia adelante en secuencias de un paso completo.
def move_on1():
    Config.pinDir.on()
    Config.pinM0.off()
    Config.pinM1.off()
    Config.pinM2.off()

    for i in range(0 , 200):
        Config.pinStep.on()
        pin2.on()
        time.sleep_ms(10)
        Config.pinStep.off()
        pin2.on()
        time.sleep_ms(10)

#Funcion para la secuencia de medio paso (half)

def move_on2():
    Config.pinDir.on()
#Al activar solo el pin M0, segun la tabla de verdad del fabricante
#Obtenemos la secuencia de medio paso.
    Config.pinM0.on()
    Config.pinM1.off()
    Config.pinM2.off()

    for i in range(0 , 400):
        Config.pinStep.on()
        Config.time.sleep_ms(10)
        Config.pinStep.off()
        Config.time.sleep_ms(10)

#Funcion para secuencia de 1/4 de paso.

def move_on3():
    Config.pinDir.on()
    Config.pinM0.off()
    Config.pinM1.on()
    Config.pinM2.off()


    for i in range(0 , 800):
        Config.pinStep.on()
        time.sleep_ms(10)
        Config.pinStep.off()
        time.sleep_ms(10)


#Secuencia de 1/8 de pasos.

def move_on5():
    Config.pinDir.on()
    Config.pinM0.on()
    Config.pinM1.on()
    Config.pinM2.off()


    for i in range(0 , 1600):
        Config.pinStep.on()
        time.sleep_ms(10)
        Config.pinStep.off()
        time.sleep_ms(10)


#Secuencia de 1/16 de pasos.

def move_on6():
    Config.pinDir.on()
    Config.pinM0.on()
    Config.pinM1.on()
    Config.pinM2.on()


    for i in range(0 , 200):
        Config.pinStep.on()
        time.sleep_ms(10)
        Config.pinStep.off()
        time.sleep_ms(10)

while True:
    move_on1
