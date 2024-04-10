
from flask import Flask, jsonify, request
import machine
import Config

app = Flask(__name__)

def back():

    Config.pinDir.off()

    for i in range(0 , 200):
        Config.pinStep.on()
        time.sleep_ms(10)
        Config.pinStep.off()
        time.sleep_ms(10)

#al igual que en adelante.py, esta funcion lo que hace en mandar mandar al html un json con la funcion para hacer que vaya para atras

@app.route('retroceso', methonds = ['POST'])
def retroceso():
  datos = request.json
  velocidad = datos['velocidad']

  if velocidad == 'pasoCompleto':
     resultado = back()
  else:
     resultado = 'velocidad no reconocida'

  return jsonify({'mensaje': 'accion realizada.', 'resultado': resultado}) 

#esto simplemente se encarga de que el programa se ejecute bien
if __name__ ==  '__main__':
   app.run(debug = True)
