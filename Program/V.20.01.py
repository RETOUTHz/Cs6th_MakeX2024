"""
V.20.01
"""
#import
import novapi
from mbuild import power_manage_module
from mbuild.encoder_motor import encoder_motor_class
from mbuild import power_expand_board
from mbuild import gamepad
from mbuild.smartservo import smartservo_class
from mbuild.ranging_sensor import ranging_sensor_class
from mbuild.smart_camera import smart_camera_class
from mbuild.led_matrix import led_matrix_class
from mbuild.button import button_class
import mbuild
import time
import math

en = {
    "LF": encoder_motor_class("M2", "INDEX1"), #Left_Front wheel
    "LB": encoder_motor_class("M1", "INDEX1"), #Lef_Back wheel
    "RF": encoder_motor_class("M4", "INDEX1"), #Right_Front wheel 
    "RB": encoder_motor_class("M6", "INDEX1")  #Right_Back wheel
}

sv = {
    "s6" : smartservo_class("M6","INDEX1")
}
"""
AUTO SECLET
จะใช้autoตัวไหน #comment ออก
"""
def select():
    Auto.Left_block_auto()
    #Auto.Right_block_auto()
    #Auto.Emergency()


"""
RANGGING
"""
debug = led_matrix_class("PORT2","INDEX1")
lk = ranging_sensor_class("PORT4", "INDEX1")
bk = ranging_sensor_class("PORT2", "INDEX3")
rk = ranging_sensor_class("PORT2", "INDEX2")
fk = ranging_sensor_class("PORT2", "INDEX1")


left_forward_wheel = encoder_motor_class("M2", "INDEX1")
right_forward_wheel = encoder_motor_class("M5", "INDEX1")
left_back_wheel = encoder_motor_class("M1", "INDEX1")
right_back_wheel = encoder_motor_class("M6", "INDEX1")

MAX_SPEED = 255
SPEED_MULTIPLIER = 1
"""
SYSTEM
"""
def feed(a:int,b:int,c:int,d:int):
    debug.show("FEED",wait = False)
    power_expand_board.set_power("DC7",a)
    power_expand_board.set_power("DC1",b)
    power_expand_board.set_power("DC2",c)
    power_expand_board.set_power("DC5",d)

def point_de_shoot():
    debug.show("SHOOT IN",wait = False)
    sv["s6"].move_to(0,50)

def point_in_shoot_():
    debug.show("SHOOT DE",wait = False)
    sv["s6"].move_to(50,50)

def blush(a:int,b:int):
    debug.show("BLUSHLESS",wait = False)
    power_expand_board.set_power("BL1",a)
    power_expand_board.set_power("BL2",b)

def load(a:int,b:int,c:int):
    debug.show("YING",wait = False)
    power_expand_board.set_power("DC2",a)
    power_expand_board.set_power("DC7",b)
    power_expand_board.set_power("DC5",c)
    time.sleep(0.1)
    power_expand_board.set_power("DC2",0)
    power_expand_board.set_power("DC7",0)
    power_expand_board.set_power("DC5",0)


def stop_all():
    debug.show("STMO",wait = False)
    power_expand_board.set_power("DC1",0)
    power_expand_board.set_power("DC2",0)
    power_expand_board.set_power("DC3",0)
    power_expand_board.set_power("DC4",0)
    power_expand_board.set_power("DC5",0)
    power_expand_board.set_power("DC6",0)
    power_expand_board.set_power("DC7",0)
    power_expand_board.set_power("DC8",0)

def lift(a:int): 
    debug.show("LIFT",wait = False)
    power_expand_board.set_power("DC8",a)
    time.sleep(0.1)
    power_expand_board.set_power("DC8",-5)

def tp(a:int):
    power_expand_board.set_power("DC7",a)

def gripper(a:int):
    power_expand_board.set_power("DC2",a)
    time.sleep(0.1)
    power_expand_board.set_power("DC2",10)

def forward(a:int):
    en["RF"].set_power(-a)
    en["RB"].set_power(-a)
    en["LB"].set_power(a)
    en["LF"].set_power(a)

def forward_speed(a: int):
    en["RF"].set_speed(-a)
    en["RB"].set_speed(-a)
    en["LB"].set_speed(a)
    en["LF"].set_speed(a)

def backward(a:int):
    en["RF"].set_power(a)
    en["RB"].set_power(a)
    en["LB"].set_power(-a)
    en["LF"].set_power(-a)

def backward_speed(a:int):
    en["RF"].set_speed(a)
    en["RB"].set_speed(a)
    en["LB"].set_speed(-a)
    en["LF"].set_speed(-a)

def turn_left(a:int):
    en["RF"].set_power(-a)
    en["RB"].set_power(-a)
    en["LB"].set_power(-a)
    en["LF"].set_power(-a)

def turn_left_speed(a:int):
    en["RF"].set_speed(-a)
    en["RB"].set_speed(-a)
    en["LB"].set_speed(-a)
    en["LF"].set_speed(-a)

def turn_right(a:int):
    en["RF"].set_power(a)
    en["RB"].set_power(a)
    en["LB"].set_power(a)
    en["LF"].set_power(a)

def turn_right_speed(a:int):
    en["RF"].set_speed(a)
    en["RB"].set_speed(a)
    en["LB"].set_speed(a)
    en["LF"].set_speed(a)

def left(a:int):
    en["RF"].set_power(-a)
    en["RB"].set_power(a)
    en["LB"].set_power(a)
    en["LF"].set_power(-a)

def left_speed(a:int):
    en["RF"].set_speed(-a)
    en["RB"].set_speed(a)
    en["LB"].set_speed(a)
    en["LF"].set_speed(-a)


def right(a:int):
    en["RF"].set_power(a-20)
    en["RB"].set_power(-a)
    en["LB"].set_power(-a)
    en["LF"].set_power(a-20)

def right_speed(a:int):
    en["RF"].set_speed(a)
    en["RB"].set_speed(-a)
    en["LB"].set_speed(-a)
    en["LF"].set_speed(a)


def stop_moving():
    en["RF"].set_power(0)
    en["RB"].set_power(0)
    en["LB"].set_power(0)
    en["LF"].set_power(0)

def red_servo():
    if sv["s6"].get_value("current") > 1250:
        sv["s6"].set_power(0)

def gripper_a(a:int):
    power_expand_board.set_power("DC2",a)

def lift_a(a:int,b:int):
    power_expand_board.set_power("DC8",-a)
    time.sleep(b)
    power_expand_board.set_power("DC8",-5)

# Hello ChatGPT
class PID:
    def __init__(self, Kp, Ki, Kd, setpoint=0):
        self.Kp = Kp  # Proportional gain
        self.Ki = Ki  # Integral gain
        self.Kd = Kd  # Derivative gain
        self.setpoint = setpoint  # Desired value (target)
        self.integral = 0  # Sum of errors over time
        self.previous_error = 0  # Previous error (used for derivative)

    def update(self, current_value):
        # Calculate the error (setpoint - current value)
        error = self.setpoint - current_value
        
        # Proportional term
        P = self.Kp * error
        
        # Integral term
        self.integral += error
        I = self.Ki * self.integral

        # Derivative term
        derivative = error - self.previous_error
        D = self.Kd * derivative

        # Calculate the output
        output = P + I + D

        # Save the current error for the next update
        self.previous_error = error

        return output

    def set_setpoint(self, setpoint):
        """ Update the target setpoint for the PID controller """
        self.setpoint = setpoint
        self.integral = 0  # Reset the integral to avoid wind-up
        self.previous_error = 0  # Reset previous error to avoid a large derivative spike


class motors:
    
    def drive(lf: int, lb: int, rf: int, rb: int):
        en["LF"].set_speed(lf)
        en["LB"].set_speed(lb)
        en["RF"].set_speed(-rf)
        en["RB"].set_speed(-rb)

    def stop():
        motors.drive(0, 0, 0, 0)
        
class util:
    def restrict(val, minimum, maximum):
        return max(min(val, maximum), minimum)

"""
For more information and explanation, please visit:
https://github.com/neumann-lab/holonomic-mecanum/
"""
class holonomic:        
    pids = {
        "lf": PID(Kp=1, Ki=0, Kd=0),
        "lb": PID(Kp=1, Ki=0, Kd=0),
        "rf": PID(Kp=1, Ki=0, Kd=0),
        "rb": PID(Kp=1, Ki=0, Kd=0),
    }
    
    """
    Holonomic driving system for mecanum.
    vx, the desired x velocity
    vy, the desired y velocity
    wL, the desired angular velocity
    deadzone, the deadzone where the value lower than this value will be set to 0
    pid, enable pid control
    """
    def drive(vx, vy, wL, deadzone=5, pid=False):
        global SPEED_MULTIPLIER
        # Create a deadzone so that if the joystick isn't moved perfectly,
        # the controller can still make the robot move perfectly.
        if math.fabs(vx) < math.fabs(deadzone):
            vx = 0
        if math.fabs(vy) < math.fabs(deadzone):
            vy = 0
        if math.fabs(wL) < math.fabs(deadzone):
            wL = 0
            
        # Calculation for the wheel speed
        # Visit https://github.com/neumann-lab/holonomic-mecanum/blob/main/th.md for the formula
        vFL = (vx + vy + wL) * SPEED_MULTIPLIER
        vFR = (-(vx) + vy - wL) * SPEED_MULTIPLIER
        vBL = (-(vx) + vy + wL) * SPEED_MULTIPLIER
        vBR = (vx + vy - wL) * SPEED_MULTIPLIER
        
        # Sliding check to not interfere with the normal movement, incase of tuning specific power
        if math.fabs(vx) > math.fabs(vy):
            vFL *= 1
            vFR *= 1
            vBL *= 1
            vBR *= 1
        
        # A PID implemention.
        # Reminder: This will significantly delay your movement.
        # Please only use this option only when you need a precise movement.
        # For example: Automatic Stage.
        if pid:            
            # Left Forward
            holonomic.pids["lf"].set_setpoint(vFL)
            vFL = holonomic.pids["lf"].update(-left_forward_wheel.get_value("speed"))
            # Left Back
            holonomic.pids["lb"].set_setpoint(vBL)
            vBL = holonomic.pids["lb"].update(-left_back_wheel.get_value("speed"))
            # Right Forward
            holonomic.pids["rf"].set_setpoint(vFR)
            vFR = holonomic.pids["rf"].update(right_forward_wheel.get_value("speed"))
            # Right Back
            holonomic.pids["rb"].set_setpoint(vBR)
            vBR = holonomic.pids["rb"].update(right_back_wheel.get_value("speed"))
        # Velocity
        vFL = util.restrict(vFL, -MAX_SPEED, MAX_SPEED)
        vFR = util.restrict(vFR, -MAX_SPEED, MAX_SPEED)
        vBL = util.restrict(vBL, -MAX_SPEED, MAX_SPEED)
        vBR = util.restrict(vBR, -MAX_SPEED, MAX_SPEED)
        # Drive motor
        motors.drive(vFL, vBL, vFR, vBR)
        
    def move_forward(power):
        holonomic.drive(0, power, 0)
        
    def move_backward(power):
        holonomic.drive(0, -power, 0)
        
    def slide_right(power):
        holonomic.drive(power, 0, 0)
        
    def slide_left(power):
        holonomic.drive(-power, 0, 0)
        
    def turn_right(power):
        holonomic.drive(0, 0, power)
        
    def turn_left(power):
        holonomic.drive(0, 0, -power)

    def move_forward_until(distance, basePower=30, kP=0, kI=0, kD=0):
        pid = PID(Kp=kP, Ki=kI, Kd=kD)
        pid.set_setpoint(distance)
        while bk.get_distance() < distance:
            power = pid.update(bk.get_distance())
            debug.show(power, wait=False)            
            holonomic.move_forward(basePower + power)
            
    def move_backward_until(distance, basePower=30, kP=0, kI=0, kD=0):
        pid = PID(Kp=kP, Ki=kI, Kd=kD)
        pid.set_setpoint(distance)
        while bk.get_distance() > distance:
            debug.show(bk.get_distance(), wait=False)            
            power = pid.update(bk.get_distance())
            holonomic.move_backward(basePower + power)
    
    def move_forward_until_left(distance, basePower=30, kP=0, kI=0, kD=0):
        pid = PID(Kp=kP, Ki=kI, Kd=kD)
        pid.set_setpoint(distance)
        while fk.get_distance() < distance:
            debug.show(bk.get_distance(), wait=False)            
            power = pid.update(bk.get_distance())
            holonomic.move_forward(basePower + power)


"""
AUTO
"""
class Auto():
    def Right_block_auto():
        lift_a(100,1.7) # lift up phase 1
        while not fk.get_distance() > 140 or bk.get_distance() < 12: #forward until phase 1
            debug.show(fk.get_distance(), wait=False)
            holonomic.move_backward(140)
        stop_moving()
        holonomic.slide_left(100)#set 0
        time.sleep(1)
        stop_moving()
        gripper_a(-100) # gripper off phase 1
        lift_a(-100,0.5) # lift down phase 1
        time.sleep(0.5)
        holonomic.move_backward(100)
        time.sleep(0.6)
        stop_moving()
        gripper_a(100) # gripper on phase 1
        time.sleep(0.5)
        while not fk.get_distance() < 130: #backward until phase 1
            debug.show(fk.get_distance(), wait=False)
            holonomic.move_forward(140)
        stop_moving()
        gripper_a(-100) #gripper off phase 1
        time.sleep(1)
        stop_all()
        lift_a(100,1) #lift up phase 2
        holonomic.slide_left(100) #set 0
        time.sleep(0.7)
        stop_moving()
        while not rk.get_distance() > 40: #slide right until phase 2
            debug.show(rk.get_distance(), wait=False)
            holonomic.slide_right(120)
        stop_moving()
        while not fk.get_distance() > 155 or bk.get_distance() < 2: #backward until phase 2
            debug.show(fk.get_distance(), wait=False)
            holonomic.move_backward(100)
        stop_moving()
        holonomic.move_backward(50)
        time.sleep(0.6)
        stop_moving()
        lift_a(-100,0.6) # lift down phase 2
        gripper_a(100) # gripper on phase 2
        time.sleep(1)
        while not fk.get_distance() < 130: #backward until phase 2
            debug.show(fk.get_distance(), wait=False)
            holonomic.move_forward(140)
        stop_moving()
        stop_all()
    
    def Left_block_auto():
        lift_a(100,1.9) # lift up phase 1
        while not fk.get_distance() > 140 or bk.get_distance() < 12: #forward until phase 1
            debug.show(fk.get_distance(), wait=False)
            holonomic.move_backward(200)
        stop_moving()
        holonomic.slide_right(100)#set 0
        time.sleep(1.3)
        stop_moving()
        gripper_a(-100) # gripper off phase 1
        lift_a(-100,0.6) # lift down phase 1
        time.sleep(0.5)
        holonomic.move_backward(100)
        time.sleep(0.3)
        stop_moving()
        gripper_a(100) # gripper on phase 1
        time.sleep(0.8)
        while not fk.get_distance() < 135: #backward until phase 1
            debug.show(fk.get_distance(), wait=False)
            holonomic.move_forward(140)
        stop_moving()
        gripper_a(-100) #gripper off phase 1
        time.sleep(1)
        stop_all()
        lift_a(100,1) #lift up phase 2
        holonomic.slide_right(100) # set 0
        time.sleep(1)
        stop_moving()
        while not rk.get_distance() > 40: #slide left until phase 2
            debug.show(rk.get_distance(), wait=False)
            holonomic.slide_left(120)
        stop_moving()
        while not fk.get_distance() > 150 or bk.get_distance() < 2: #backward until phase 2
            debug.show(fk.get_distance(), wait=False)
            holonomic.move_backward(70)
        stop_moving()
        holonomic.move_backward(50)
        time.sleep(0.8)
        stop_moving()
        lift_a(-100,0.7) # lift down phase 2
        gripper_a(100) # gripper on phase 2
        time.sleep(1)
        while not fk.get_distance() < 130: #backward until phase 2
            debug.show(fk.get_distance(), wait=False)
            holonomic.move_forward(140)
        stop_moving()
        holonomic.turn_right(100)
        time.sleep(1)
        stop_moving()
        stop_all()

    def Emergency():
        forward(30)
        feed(90,100,0,0)
        time.sleep(3.3)
        stop_moving()
        time.sleep(3)
        stop_all()
    
        
"""
MANUAL
"""
class manual():
    def controler():
        if not gamepad.get_joystick("Rx") == 0:
            en["RF"].set_power(gamepad.get_joystick("Rx") / (1.95 * -1))
            en["RB"].set_power(gamepad.get_joystick("Rx") / (1.95 * -1))
            en["LB"].set_power(gamepad.get_joystick("Rx") / (1.95 * -1))
            en["LF"].set_power(gamepad.get_joystick("Rx") / (1.95 * -1))
            #power_expand_board.set_power("DC6",-100)


        # elif not gamepad.get_joystick("Lx") == 0:
        #     en["RF"].set_power(gamepad.get_joystick("Lx") / (1.5 * -1))
        #     en["RB"].set_power(gamepad.get_joystick("Lx") / (1.5))
        #     en["LB"].set_power(gamepad.get_joystick("Lx") / (1.5))
        #     en["LF"].set_power(gamepad.get_joystick("Lx") / (1.5 * -1))
        #     #power_expand_board.set_power("DC8",(gamepad.get_joystick("Lx") / (1.7 * -1)))#LF

        elif not gamepad.get_joystick("Lx") == 0:
            en["RF"].set_speed(gamepad.get_joystick("Lx") / (0.1 * -1))
            en["RB"].set_speed(gamepad.get_joystick("Lx") / (0.05))
            en["LB"].set_speed(gamepad.get_joystick("Lx") / (0.1))
            en["LF"].set_speed(gamepad.get_joystick("Lx") / (0.1 * -1))
            #power_expand_board.set_power("DC8",(gamepad.get_joystick("Lx") / (1.7 * -1)))#LF
    
        elif not gamepad.get_joystick("Ly") == 0:
            en["LB"].set_power(gamepad.get_joystick("Ly") / 1.7)
            en["LF"].set_power(gamepad.get_joystick("Ly") / (1.635 * 1))
            en["RF"].set_power(gamepad.get_joystick("Ly") / (1.635* -1))
            en["RB"].set_power(gamepad.get_joystick("Ly") / (1.7 * -1))
            #power_expand_board.set_power("DC6",(gamepad.get_joystick("Ly") / 1.7))#tp
        
        elif gamepad.is_key_pressed("N1"):
            feed(90,100,0,0)

        elif gamepad.is_key_pressed("N2"):
            load(100,100,100)
        
        elif gamepad.is_key_pressed("N3"):
            load(-100,-50,-100)
        
        elif gamepad.is_key_pressed("N4"):
            sv["s6"].move_to(-75,50)
        
        elif gamepad.is_key_pressed("R1"):
            blush(100,100)
        
        elif gamepad.is_key_pressed("R2"):
            blush(0,0)

        elif gamepad.is_key_pressed("L1"):
            stop_all()
            sv["s6"].move_to(-90,50)
        
        elif gamepad.is_key_pressed("L2"):
            feed(-100,-60,-100,-100)
        
        elif gamepad.is_key_pressed("≡"):
            sv["s6"].move_to(-55,50)
            power_expand_board.set_power("BL1",80)
            power_expand_board.set_power("BL2",80)
        
        elif gamepad.is_key_pressed("+"):
            sv["s6"].move_to(-110,40)
            power_expand_board.set_power("BL1",80)
            power_expand_board.set_power("BL2",80)

        elif gamepad.is_key_pressed("Up"):
            lift(-100)

        elif gamepad.is_key_pressed("Down"):
            lift(80)

        elif gamepad.is_key_pressed("Left"):
            gripper(-100)

        elif gamepad.is_key_pressed("Right"):
            gripper(100)

        else:
            en["RF"].set_power(0)
            en["RB"].set_power(0)
            en["LB"].set_power(0)
            en["LF"].set_power(0) 
            power_expand_board.set_power("DC5",0)

"""
MAIN
"""

while True:
    time.sleep(0.001)
    if power_manage_module.is_auto_mode():
        select()
        while not not power_manage_module.is_auto_mode():
            pass
    else:
        manual.controler()
        red_servo()
