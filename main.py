from gpiozero import servo
from time import sleep

servo = servo(17)

while True:
	servo.mid()
	print("mid")
	sleep(0.5)
	servo.min()
	print("min")
	sleep(1)
	servo.mid()
	print("mid")
	sleep(0.5)
	servo.max()
	print("max")
	sleep(1)