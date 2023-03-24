# Treadmill dashboard
# Auther: Didula Induwara
from asyncio import sleep
import time
import tkinter as tk
from tkinter import StringVar, ttk
# walking  :- (0.1 x speed) + (1.8 x speed x grade) + 3.5
# runnig   :- (0.2 x speed) + (0.9 x speed x grade) + 3.5
# steps    :- (speed x time) / (height x 0.413 x 0.01)

FLAG = False

def caloriesBurned(speed, grade, weight, time):
    factor1 = 0
    factor2 = 0

    # walking
    if speed <= 3.7/2.237:
        factor1 = 0.1
        factor2 = 1.8
    # running
    else:
        factor1 = 0.2
        factor2 = 0.9       

    return ((factor1*speed) + (factor2*speed*grade*0.01) + 3.5)*weight*0.005*time



def numberOfSteps(speed, time, height):
    return round((speed*time)/(height*0.01*0.413))


def stop():
    global FLAG
    FLAG = False

def start():
    global FLAG
    global startTime

    FLAG = True
    startTime = time.time()
    
# main window
window = tk.Tk()
window.title("TreadMill")

# main frame
frame = tk.Frame(window, padx= 10, pady=10)
frame.pack()

calory_burned = ''
num_of_steps = ''

def Treadmill():
    global calory_burned
    global FLAG
    if FLAG:
        try:
            speed = float(speedEntry.get())
            grade = float(gradeEntry.get())
            weight = float(weightEntry.get())
            height = float(heightEntry.get())

            timeSpent = time.time() - startTime
            calory_burned = str(round(caloriesBurned(speed, grade, weight, timeSpent), 3))
            num_of_steps = numberOfSteps(speed, timeSpent, height)
            cal_results.config(text=calory_burned)
            step_results.config(text=num_of_steps)
            print("\r "+str(caloriesBurned(speed, grade, weight, time.time() - startTime)) + "         "+calory_burned, end='')
        except:
            print("Enter correct values")
            FLAG = False


        
    # recursive call
    window.after(1000, Treadmill)




# frame 1
treadmill_info_frame = tk.LabelFrame(frame, text = "Treadmill info", padx=5, pady=5)
treadmill_info_frame.grid(row=0, column=0)

speed = tk.Label(treadmill_info_frame, text = "Speed (m/s)")
speed.grid(row=0, column=0)

grade = tk.Label(treadmill_info_frame, text = "Grade (%)")
grade.grid(row=0, column=1)

speedEntry = tk.Entry(treadmill_info_frame)
gradeEntry = tk.Entry(treadmill_info_frame)
speedEntry.grid(row=1, column=0)
gradeEntry.grid(row=1, column=1)


for widget in treadmill_info_frame.winfo_children():
    widget.grid_configure(padx=10, pady=5)




# frame2
user_info_frame = tk.LabelFrame(frame, text = "User Info", padx=5, pady=5)
user_info_frame.grid(row=1, column=0)
weight = tk.Label(user_info_frame, text = "Weight (kg)")
weight.grid(row=0, column=0)

height = tk.Label(user_info_frame, text = "Height (cm)")
height.grid(row=0, column=1)

weightEntry = tk.Entry(user_info_frame)
heightEntry = tk.Entry(user_info_frame)

weightEntry.grid(row=1, column=0)
heightEntry.grid(row=1, column=1)

for widget in user_info_frame.winfo_children():
    widget.grid_configure(padx=10, pady=5)



# frame 3
results_frame = tk.LabelFrame(frame, text="Results")
results_frame.grid(row=2, column=0, padx=10,pady=10)

Calories_burned = tk.Label(results_frame, text = "Calories burned (cal)")
Calories_burned.grid(row=0, column=0)

steps = tk.Label(results_frame, text = "Steps")
steps.grid(row=0, column=1)

cal_results  = tk.Label(results_frame, font=("Arial", 20), bg = "black", fg="white", width= 8)
cal_results.grid(row=1, column=0)

step_results  = tk.Label(results_frame, font=("Arial", 20), bg = "black", fg="white", width=8)
step_results.grid(row=1, column=1)

for widget in results_frame.winfo_children():
    widget.grid_configure(padx=10, pady=5)



# frame 4
button_frame = tk.LabelFrame(frame, border=0)
button_frame.grid(row=3, column=0)

startButton = tk.Button(button_frame, text='start', command=start)
startButton.grid(row=0, column=0)

stopButton = tk.Button(button_frame, text='stop', command=stop)
stopButton.grid(row=0, column=1)

for widget in button_frame.winfo_children():
    widget.grid_configure(padx=10, pady=10)


window.after(1000, Treadmill)
window.mainloop()