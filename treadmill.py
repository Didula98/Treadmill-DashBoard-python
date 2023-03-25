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
    global action

    # walking
    if speed <= 3.7/2.237:
        factor1 = 0.1
        factor2 = 1.8
        action = "Walking"
    # running
    else:
        factor1 = 0.2
        factor2 = 0.9 
        action = "Running"      

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
frame = tk.Frame(window, border=5, bg="#B3B6B7", highlightbackground="#292e2e", highlightthickness=10)
frame.pack()

LHS = tk.Frame(frame, bg="#B3B6B7")
LHS.grid(row=0, column=0, padx=5,pady=5)

RHS = tk.Frame(frame, bg="#B3B6B7")
RHS.grid(row=0, column=1, padx=5,pady=5)

calory_burned = ''
num_of_steps = ''
action = ''

def Treadmill():
    global action
    global num_of_steps
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
            action_result.config(text=action)
            print("\r "+str(caloriesBurned(speed, grade, weight, time.time() - startTime)) + "         "+calory_burned, end='')
        except:
            action = "Enter correct values!"
            action_result.config(text=action)
            print("Enter correct values")
            FLAG = False


        
    # recursive call
    window.after(1000, Treadmill)




# frame 1
treadmill_info_frame = tk.Frame(LHS)
treadmill_info_frame.grid(row=0, column=0, padx=5,pady=5)


speed = tk.Label(treadmill_info_frame, text = "Speed (m/s)", font=("Arial", 15))
speed.grid(row=0, column=0)

grade = tk.Label(treadmill_info_frame, text = "Grade (%)", font=("Arial", 15))
grade.grid(row=0, column=1)

speedEntry = tk.Entry(treadmill_info_frame, font=("Arial", 15))
gradeEntry = tk.Entry(treadmill_info_frame, font=("Arial", 15))
speedEntry.grid(row=1, column=0)
gradeEntry.grid(row=1, column=1)


for widget in treadmill_info_frame.winfo_children():
    widget.grid_configure(padx=10, pady=10)




# frame2
user_info_frame = tk.Frame(LHS)
user_info_frame.grid(row=1, column=0, padx=5,pady=5)
weight = tk.Label(user_info_frame, text = "Weight (kg)", font=("Arial", 15))
weight.grid(row=0, column=0)

height = tk.Label(user_info_frame, text = "Height (cm)", font=("Arial", 15))
height.grid(row=0, column=1)

weightEntry = tk.Entry(user_info_frame, font=("Arial", 15))
heightEntry = tk.Entry(user_info_frame, font=("Arial", 15))

weightEntry.grid(row=1, column=0)
heightEntry.grid(row=1, column=1)

for widget in user_info_frame.winfo_children():
    widget.grid_configure(padx=10, pady=10)



# frame 3
results_frame = tk.Frame(RHS)
results_frame.grid(row= 0,column=0, padx=5,pady=5)

Calories_burned = tk.Label(results_frame, text = "Calories burned (cal)", font=("Arial", 15))
Calories_burned.grid(row=0, column=0)

steps = tk.Label(results_frame, text = "Steps", font=("Arial", 15))
steps.grid(row=2, column=0)

cal_results  = tk.Label(results_frame, font=("Arial", 20), bg = "#292e2e", fg="white", width= 12)
cal_results.grid(row=1, column=0)

step_results  = tk.Label(results_frame, font=("Arial", 20), bg = "#292e2e", fg="white", width=12)
step_results.grid(row=3, column=0)

for widget in results_frame.winfo_children():
    widget.grid_configure(padx=10, pady=8)



# frame 4
button_frame = tk.Frame(frame, bg="#B3B6B7")
button_frame.grid(row=1, column=0)

startButton = tk.Button(button_frame, text='Start', command=start, border=1, activebackground='#AED6F1', bg="#D6EAF8", font=("Arial", 15))
startButton.grid(row=0, column=0)

stopButton = tk.Button(button_frame, text='Stop', command=stop, border=1, activebackground='#F1948A', bg="#FADBD8", font=("Arial", 15))
stopButton.grid(row=0, column=1)

for widget in button_frame.winfo_children():
    widget.grid_configure(padx=10, pady=10)


action_frame = tk.Frame(frame)
action_frame.grid(row=1, column=1)

action_result = tk.Label(action_frame, font=("Arial", 10), bg = "#292e2e", fg="white", width= 20, padx=5, pady=5)
action_result.grid(row=0, column=0)

window.after(1000, Treadmill)
window.mainloop()