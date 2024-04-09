import machine
import Config

def back():

    Config.pinDir.off()

    for i in range(0 , 200):
        Config.pinStep.on()
        time.sleep_ms(10)
        Config.pinStep.off()
        time.sleep_ms(10)
        


