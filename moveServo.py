from gpiozero import AngularServo
# ~ from guizero import App, Slider, Text

# ~ app=App(title="Servo_GUI", layout="grid")
# ~ s = AngularServo(12, min_angle=-90, max_angle=90)
# ~ s1 = AngularServo(13, min_angle=-90, max_angle=90)

# ~ def update_text():
    # ~ s.angle = int(slider.value)
    # ~ print("motor1: ", s.angle)
    # ~ s1.angle = int(slider1.value)
    # ~ print("motor2: ",s1.angle)
    
# ~ slider =Slider(app, start=-90, end=90, command=update_text, grid=[1,2])
# ~ slider1 =Slider(app, start=-90, end=90, command=update_text, grid=[2,2])


# ~ Text(app, "M1",grid=[1,1])
# ~ Text(app, "M2",grid=[2,1])
# ~ app.display()


import pigpio
import curses
pi=pigpio.pi()

screen = curses.initscr()
curses.noecho()
curses.cbreak()
screen.keypad(True)

s = AngularServo(12, min_angle=-90, max_angle=90)
s1 = AngularServo(13, min_angle=-90, max_angle=90)

if __name__ == '__main__':

    while True:

        Char = screen.getch()


        if Char== ord('w'):
            # ~ pi.set_servo_pulsewidth(16, 1600)
            if s1.angle < 90:
                s1.angle += 1
            # ~ print ("rotate up")

        if Char==ord('s'):
            # ~ pi.set_servo_pulsewidth(16,1600)
            if s1.angle > (-90):
                s1.angle -= 1
            # ~ print (" rotate down")

        if Char==ord('a'):
            # ~ pi.set_servo_pulsewidth(12, 1600)
            # ~ pi.set_servo_pulsewidth(13, 0)
            if s.angle < 90:
                s.angle += 1
            # ~ print ("turn left")

        if Char==ord('d'):
            # ~ pi.set_servo_pulsewidth(12, 0)
            # ~ pi.set_servo_pulsewidth(13, 1400)
            if s.angle > (-90):
                s.angle -= 1
            # ~ print ("turn right")
        print(s.angle, ' ', s1.angle, '\n')
        
            
