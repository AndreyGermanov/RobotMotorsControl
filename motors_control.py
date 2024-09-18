import RPi.GPIO as GPIO
from time import sleep

# Установка режима GPIO
GPIO.setmode(GPIO.BCM)

# GPIO PIN, к которому подключен двигатель
motor_pin = 18

# Перевести PIN в режим вывода (OUT)
GPIO.setup(motor_pin, GPIO.OUT)

# Установка частоты ШИМ (PWM)
freq = 1000

# Создание объекта PWM для работы через указанный PIN
# и на указанной частоте
pwm = GPIO.PWM(motor_pin, freq)

# Запуск PWM с рабочим циклом 50%
pwm.start(50)

# Запуск двигателя на разных скоростях
for speed in range(0,100,10):
    pwm.ChangeDutyCycle(speed)
    sleep(5)
    
pwm.ChangeDutyCycle(100)

# Остановка двигателя
pwm.stop()

# Сброс GPIO
GPIO.cleanup()