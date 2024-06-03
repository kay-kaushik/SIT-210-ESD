import requests
import serial
import time
from datetime import datetime, timedelta
import tkinter as tk
from tkinter import PhotoImage
import RPi.GPIO as GPIO

# IFTTT URL
ifttt_url = "https://maker.ifttt.com/trigger/need_water/with/key/fxpHNgIezl9k1iNw-qJ9R0Hn6-Xr1Iw7qsnk3GYEMHh"

# initialising variables and initial setup
timeNow = datetime.now()
currDate = timeNow.strftime("%Y-%m-%d")
messageSent = [currDate, False]
relayPin = 11
GPIO.setmode(GPIO.BOARD)
GPIO.setup(relayPin, GPIO.OUT)

# Initialize sunlight accumulation variables
totalLightToday = 0
startOfToday = datetime.now().replace(hour = 0, minute = 0, second = 0, microsecond = 0)

def send_ifttt_notification():
    try:
        response = requests.post(ifttt_url)
        if response.status_code == 200:
            print("IFTTT notification sent successfully.")
        else:
            print(f"Failed to send IFTTT notification. Status code: {response.status_code}")
    except Exception as e:
        print(f"Error sending IFTTT notification: {e}")

def numExtractor(element):
    numericPart = element.split(":")
    return float(numericPart[1])

def open_serial_port():
    try:
        ser = serial.Serial(serial_port, baud_rate, timeout=1)
        print(f"Opened serial port {serial_port} at {baud_rate} baud.")
        return ser
    except serial.SerialException as e:
        print(f"Error opening serial port: {e}")
        return None

# Initialize the serial port
serial_port = '/dev/ttyS0'  
baud_rate = 9600
ser = open_serial_port()

# Create tkinter window
window = tk.Tk()
window.title("Plant Health")

# Create a label to display the received data
data_label = tk.Label(window, text="No data received yet", font=("Helvetica", 16))
data_label.grid(row = 0, column = 2)

hLabel = tk.Label(window, text="No data received yet", font=("Helvetica", 16))
hLabel.grid(row = 1, column = 1, pady = 20)

tLabel = tk.Label(window, text="No data received yet", font=("Helvetica", 16))
tLabel.grid(row = 1, column = 2, pady = 20)

lLabel = tk.Label(window, text="No data received yet", font=("Helvetica", 16))
lLabel.grid(row = 1, column = 3, pady = 20)

sLabel = tk.Label(window, text="No data received yet", font=("Helvetica", 16))
sLabel.grid(row = 1, column = 4)

warningLabel = tk.Label(window, text="", font=("Helvetica", 16))
warningLabel.grid(row = 2, column = 3)

tsLabel = tk.Label(window, text= str(totalLightToday), font=("Helvetica", 16))
tsLabel.grid(row = 2, column = 1)



# Load plant image
try:
    happyPlant = PhotoImage(file="/home/kartikkaushik/Desktop/plantKeepAlive/images/happyPlant.png")
    sadPlant = PhotoImage(file="/home/kartikkaushik/Desktop/plantKeepAlive/images/sadPlant.png")
    plant_label = tk.Label(window, image=happyPlant)
    plant_label.grid(row = 3, column = 2)
except Exception as e:
    print(f"Error loading image: {e}")



def resetSunlight():
    global totalLightToday, startOfToday
    totalLightToday = 0
    startOfToday = datetime.now().replace(hour = 0, minute = 0, second = 0, microsecond = 0)

def read_serial():
    global ser, totalLightToday, startOfToday
    if ser and ser.is_open:
        try:
            # Read data from serial port
            raw_data = ser.readline()
            try:
                data = raw_data.decode('utf-8').strip()
                if data:
                    # Update the label with the received data
                    dataList = data.split(",")
                    print(dataList)
                    try:
                        sVal = numExtractor(dataList[-1])
                        hLabel.config(text = dataList[0])
                        tLabel.config(text = dataList[1])
                        lLabel.config(text = dataList[2])
                        sLabel.config(text = dataList[3])
                        data_label.config(text=data)
                    
                    # Accumulate sunlight value 
                    # basil plants need 10000 lux to 20000 lux per day 
                        totalLightToday += numExtractor(dataList[2])
                        tsLabel.config(text="total lux received: " + str(round(totalLightToday)) + " lux")
                    
                        if sVal < 300:
                            plant_label.config(image = sadPlant)
                            sLabel.grid(row = 1, column = 4, pady = 20)
                            warningLabel.config(text = "water the plant asap")
                            GPIO.output(relayPin, GPIO.HIGH)
                            print("turning water on!!")
                            time.sleep(5)
                            print("turning water off!!")
                            GPIO.output(relayPin, GPIO.LOW)
                            if not messageSent[1]:
                                send_ifttt_notification()
                                messageSent[1] = True
                        else:
                            messageSent[1] = False
                            plant_label.config(image = happyPlant)
                            warningLabel.config(text = "The plant is healthy and growing")
                    except IndexError as e:
                        print(f"index error occured: {e}")

            except UnicodeDecodeError as e:
                print(f"Decode error: {e}. Raw data: {raw_data}")
        except serial.SerialException as e:
            print(f"Serial error: {e}")
            ser.close()
            ser = None
            time.sleep(1)
            ser = open_serial_port()

    # Reset the daily sunlight accumulation at the start of a new day
    if datetime.now() >= startOfToday + timedelta(days=1):
        resetSunlight()

    window.after(1000, read_serial)

# Start reading from the serial port
read_serial()

try:
    window.mainloop()
except KeyboardInterrupt:
    print("Keyboard interrupt received. Closing serial port.")
    if ser:
        ser.close()
    print("Serial port closed.")
