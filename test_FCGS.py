#imported libraries, for the GUI, serial etc
import tkinter as tk
import tk_tools
import serial 
import serial 

#f_angle is a float number, i_angle is a int value.
ser = serial.Serial('COM3',baudrate= 9600, timeout = 1)
while 1:
    s_angle = ser.readline().decode('ascii')
    try:
        f_angle = float(s_angle)
        i_angle = int(f_angle)
        print("Converted integer:", i_angle)
    except ValueError:
    # Handle the case where the input string is not a valid number
        print("Callibrating...")


    
    root = tk.Tk()

# Sets the title of the window
    root.title("FCGS")

# Sets the dimensions of the window (width x height)
    root.geometry("700x700")
#creates the gauge 
    rs = tk_tools.RotaryScale(root, max_value=360.0, size=100, unit='/degree pitch')
    rs.grid(row=350, column=350)

    rs.set_value(i_angle)

# Starts the loop
    root.mainloop()


