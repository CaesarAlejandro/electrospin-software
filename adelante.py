#libreria que falicita el desarrollo web
from flask import Flask, jsonify, request
import machine
import Config

#instancia de clase flask que permite manipular el decorador @app. de mas adelante
app = Flask(__name__)

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

#Esta parte es una funcion que lo que hace es mandar un paquete para que se active una de las cinco funciones de movimiento dependiente del valor del selector

@app.route('establecer_velocidad', methonds=['POST'])
def establecer_velocidad():
 datos = request.json
 velocidad = datos['velocidad']

 if velocidad == 'pasoCompleto':
      resultado = move_on1()

 elif velocidad == 'medioPaso':
     resultado = move_on2()

 elif velocidad == 'cuartoDePaso':
     resultado = move_on3()
 
 elif velocidad == 'octavoDePaso':
     resultado = move_on5()

 elif velocidad == 'dieciseisAvosPaso':
     velocidad = move_on6()

 return jsonify({'mensaje': 'velodidad establecida a ' + velocidad, 'resultado': resultado})
 

while True:
    move_on1

