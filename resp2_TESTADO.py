#############################################################
#  ########\                                                #
#  ##  _____|                                               #
#  ## |       ######\####\   #######\                       #
#  #####\     ##  _##  _##\ ##  _____|                      #
#  ##  __|    ## / ## / ## |## /                            #
#  ## |       ## | ## | ## |## |                            #
#  ########\  ## | ## | ## |\#######\                       #
#  \________| \__| \__| \__| \_______|                      #
#    Ércio       Marcelo       Cainã                        #
#                                                           #
#  Desenvolver um circuito e programar para que pisque      # 
#  um LED 10 vezes no primeiro segundo,                     #
#  fique ligado durante 1 segundo e assim sucessivamente.   #
#                                                           # 
#  Autores: Marcelo Josué Telles,                           #
#           Ércio Luis Dorneles Berna,                      #
#           Cainã Silva da Costa                            #
#                                                           #
#  Data: 03/06/2017                                         #
#############################################################
import RPi.GPIO as GPIO
import time
GPIO.setmode(GPIO.BOARD)
pin_to_circuit = 12
try:
    GPIO.setup(pin_to_circuit, GPIO.OUT)
    while(1):
        j=0
        while j<10:
            GPIO.output(pin_to_circuit,1)
            print("***LIGADO***")
            time.sleep(.05)
            GPIO.output(pin_to_circuit,0)
            print("---DESLIGADO---")
            time.sleep(.05)
            j+=1
        GPIO.output(pin_to_circuit,1)
        print("***LIGADO***")	
        time.sleep(1)
        j=0
except KeyboardInterrupt:
    print ("Fim")
    pass
finally:
    GPIO.cleanup()
