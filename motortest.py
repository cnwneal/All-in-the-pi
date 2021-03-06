import RPi.GPIO as GPIO
GPIO.setmode(GPIO.BOARD)
GPIO.setup(13, GPIO.OUT)

dc = 5

servo = GPIO.PWM(13,2000)
servo.start(10)
print('***Connect Battery & Press ENTER to start')
res = raw_input()
servo.ChangeDutyCycle(5)
print('***Press ENTER to start')
res = raw_input()


print ('increase > a | decrease > z | save Wh > n | set Wh > h|quit > 9')

cycling = True
try:
    while cycling:
        servo.ChangeDutyCycle(dc)
        res = raw_input()
        if res == 'a':
            dc = dc + 0.05
        if res == 'z':
            dc = dc - 0.05
        if res == 'h':
            mymotor.setWh()
        if res == '9':
            cycling = False
finally:
    # shut down cleanly
    servo.stop()
    print ("dc var setting is: ")
    print (dc)


print('***Press ENTER to quit')
res = raw_input()
servo.stop()
GPIO.cleanup()
