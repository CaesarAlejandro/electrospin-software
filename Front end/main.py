import machine
import Config
from adelante import move_on1
from atras import back

'''
html = """<!DOCTYPE html>
<html lang="es">
  <head>   
    <link href="estiloRay.css" rel="stylesheet">

  </head>
    
  <body> 
    <main id="apertura1">
    <h1>Bienvenido a la interfaz de la Appi</h1> 
    <br><hr>
    </main>
    <main id="apertura2">
      
      <form action="/enviar-orden">
        <h2>Presione el siguiente boton para detener el movimiento de la aguja</h2><br>
          
        <button type="submit" class="boton"> 
          <span class="express">Detener</span>
        </button>
         

        <h2>Presione el siguiente boton para mover la aguja hacia adelante</h2><br>
          
        <button type="submit" class="boton">
          <span class="express">Avazar</span>
        </button>
        
        <h2>Presione el siguiente boton para mover la aguja hacia atras</h2><br> 
      
        <button type="submit" class="boton">
          <span class="express">Retroceder</span>
        </button>
      </form>   
      <!-- Esta parte del codigo hay que pulirla-->
     <h2>Eliga la velocidad de movimiento de la aguja</h2>
      
      <form action="/definir-velocidad" class="letra">
        
        <label for="Maxima velocidad">
          <input id="Maxima velocidad" type="radio" name="Maxima velocidad-Minima velocidad-Elegir velocidad">Maxima velocidad 
        </label><br>
        
        <label for="Minima velocidad" class="letra">
          <input id="Minima velocidad" type="radio" name="Maxima velocidad-Minima velocidad-Elegir velocidad">Minima velocidad
        </label><br>

        <label for="Elegir velocidad" class="letra">
          <input id="Elegir velocidad" type="radio" name="Maxima velocidad-Minima velocidad-Elegir velocidad">Elegir velocidad
          <input type="text" placeholder="Especifique la velocidad deseada required">
          <button type="submit">enviar</button> 
        </label><br>

      </form>

        
        
      
     
    </main>
    
  </body>
    
</html>""""
import socket
addr = socket.getaddrinfo('0.0.0.0', 80)[0][-1]

s = socket.socket()
s.bind(addr)
s.listen(1)

print('listening on', addr)

while True:
    cl, addr = s.accept()
    print('client connected from', addr)
    cl_file = cl.makefile('rwb', 0)
    while True:
        line = cl_file.readline()
        if not line or line == b'\r\n':
            break
    rows = ['<tr><td>%s</td><td>%d</td></tr>' % (str(p), p.value()) for p in pins]
    response = html % '\n'.join(rows)
    cl.send('HTTP/1.0 200 OK\r\nContent-type: text/html\r\n\r\n')
    cl.send(response)
    cl.close()'''
pinled = Pin(2 , Pin.OUT)
pinDir = Pin(33, Pin.OUT)
pinStep = Pin(25, Pin.OUT)
pinM2 = Pin(34, Pin.OUT)
pinM0 = Pin(35, Pin.OUT)
pinM1 = Pin(32, Pin.OUT)
pinEnable = Pin(14, Pin.OUT)
while True:
  pinled.on()
  move_on1()
  pinled.on
  back()