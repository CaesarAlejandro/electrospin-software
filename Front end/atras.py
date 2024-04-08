import machine
import boot

def back():

    boot.pinDir.off()

    for i in range(0 , 200):
        boot.pinStep.on()
        time.sleep_ms(10)
        boot.pinStep.off()
        time.sleep_ms(10)
        


