# necessary libraries
import RPi.GPIO as GPIO
import tkinter as tk

GPIO.setmode(GPIO.BOARD)

# function which sets up GPIO pins
def ledSetup(led):
	GPIO.setup(led, GPIO.OUT)
	GPIO.output(led,GPIO.LOW)

# led pin initialisation code
blue = 19
yellow = 21
red = 23

ledSetup(blue)
ledSetup(yellow)
ledSetup(red)

# creating tkinter window 
window = tk.Tk()
window.title("LED CONTROLER")


#led ON function which turns on the led based on the ledVar value 
def ledOn():
	currLed = ledVar.get()
	if currLed == "blue":
		GPIO.output(blue, GPIO.HIGH)
		GPIO.output(red, GPIO.LOW)
		GPIO.output(yellow, GPIO.LOW)
	elif currLed == "yellow":
		GPIO.output(yellow, GPIO.HIGH)
		GPIO.output(red, GPIO.LOW)
		GPIO.output(blue, GPIO.LOW)
	elif currLed == "red":
		GPIO.output(red, GPIO.HIGH)
		GPIO.output(blue, GPIO.LOW)
		GPIO.output(yellow, GPIO.LOW)
	

# exit code
def exit():
	GPIO.cleanup()
	window.destroy()

# variable to store the value of led 
ledVar = tk.StringVar(value = "off")

# tkinter radiobuttons creation 
blueButton = tk.Radiobutton(window, text = "Turn on Blue LED" ,variable = ledVar,  
value = "blue" , command = ledOn, bg = "blue")
blueButton.grid(row = 0, column = 1)
yellowButton = tk.Radiobutton(window, text = "Turn on Yellow LED" , variable = ledVar,
value = "yellow",command = ledOn, bg = "yellow")
yellowButton.grid(row = 0, column = 2)
redButton = tk.Radiobutton(window, text = "Turn on red LED", variable = ledVar,
value = "red" ,command = ledOn, bg = "red")
redButton.grid(row = 0, column = 3)
exitButton = tk.Button(window, text = "EXIT" , 
command = exit, bg = "green")
exitButton.grid(row = 2, column = 2)

window.mainloop()
