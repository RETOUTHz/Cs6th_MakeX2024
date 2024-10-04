
"""
________/\\\\\\\\\_________________________/\\\\\_________________/\\\_________        
 _____/\\\////////______________________/\\\\////_________________\/\\\_________       
  ___/\\\/____________________________/\\\///___________/\\\_______\/\\\_________      
   __/\\\______________/\\\\\\\\\\___/\\\\\\\\\\\_____/\\\\\\\\\\\__\/\\\_________      
    _\/\\\_____________\/\\\//////___/\\\\///////\\\__\////\\\////___\/\\\\\\\\\\__    
     _\//\\\____________\/\\\\\\\\\\_\/\\\______\//\\\____\/\\\_______\/\\\/////\\\_   
      __\///\\\__________\////////\\\_\//\\\______/\\\_____\/\\\_/\\___\/\\\___\/\\\_   
       ____\////\\\\\\\\\__/\\\\\\\\\\__\///\\\\\\\\\/______\//\\\\\____\/\\\___\/\\\_ 
        _______\/////////__\//////////_____\/////////_________\/////_____\///____\///__

        #พ่อน้องออนิว
        #แม่น้องออนิว
        #รถเดิมเดิมให้กูเดินดีกว่า
        #สัมศรีหวานเจี๊ยบ
        #freedom888
        #หมูไม่ขาดละหมาดไม่เคย
        #Cs 'SEX' th
        #หมูอยู่ในกระเพาอันเราะอยู่ในใจ

        © 2024 Pollayaaa, All Rights Reserved Coded With ❤️ By Pollayaaa
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

#Encode
en = {
    "LF": encoder_motor_class("M4", "INDEX1"), #Left_Front wheel
    "LB": encoder_motor_class("M1", "INDEX1"), #Lef_Back wheel
    "RF": encoder_motor_class("M5", "INDEX1"), #Right_Front wheel 
    "RB": encoder_motor_class("M6", "INDEX1")  #Right_Back wheel

}


#Servo
sv = {
    "s1": smartservo_class("M5","INDEX1"),
    "s2": smartservo_class("M6","INDEX1"),
    "s3": smartservo_class("M3","INDEX1"),
    "s4": smartservo_class("M4","INDEX1"),
    "s6": smartservo_class("M6","INDEX1")
}

#Roblox x Poolvila
feed = False
motor1 = 100
motor2 = 100
motor3 = 90
motor4 = 100
motor5 = 100
bl = 90
shooter_point1_angle_servo =  80
shooter_point2_angle_servo =  15

class control:
    def toggle_feed():
        global feed
        feed = not feed
        if feed:
            power_expand_board.set_power("DC1", 100)
        else:
            power_expand_board.set_power("DC1", 0)

#joys
class joys:
 def control ():
    global motor1 ,motor2 ,motor3,bl,shooter_point1_angle_servo,shooter_point2_angle_servo

    if gamepad.is_key_pressed("N1"):
        manual.feed()

    elif gamepad.is_key_pressed("N2"):
        power_expand_board.set_power("DC5", -100)

    elif gamepad.is_key_pressed("N3"):
        power_expand_board.set_power("DC5", 100)

    elif gamepad.is_key_pressed("N4"):
        manual.feed()

    elif gamepad.is_key_pressed("L1"):
        power_expand_board.stop("DC1")
        power_expand_board.stop("DC2")
        power_expand_board.stop("DC3")
        power_expand_board.stop("DC4")

    elif gamepad.is_key_pressed("R1"):
         power_expand_board.set_power("BL1", bl)
         power_expand_board.set_power("BL2", bl)

    elif gamepad.is_key_pressed("L2"):
        power_expand_board.set_power("DC1", motor1)
        power_expand_board.set_power("DC2", motor2)
        power_expand_board.set_power("DC3", motor3)
        power_expand_board.set_power("DC4", motor4)

    elif gamepad.is_key_pressed("R2"):
         power_expand_board.stop("BL1")
         power_expand_board.stop("BL2")

    elif gamepad.is_key_pressed("Up"):
         power_expand_board.set_power("DC7",80)

    elif gamepad.is_key_pressed("Down"):
         power_expand_board.set_power("DC7",-80)

    elif gamepad.is_key_pressed("Left"):
         power_expand_board.set_power("DC8",50)
    
    elif gamepad.is_key_pressed("Right"):
         power_expand_board.set_power("DC8",-50)
    
    elif gamepad.is_key_pressed("+"):
        sv["s6"].move_to(shooter_point1_angle_servo,25)

    elif gamepad.is_key_pressed("≡"):
        sv["s6"].move_to(shooter_point2_angle_servo,25)

    else:
        power_expand_board.set_power("DC5",0)
        power_expand_board.set_power("DC6",0)
        power_expand_board.set_power("DC7",0)
        power_expand_board.set_power("DC8",0)
        
 def macanum_1 ():
    if not gamepad.get_joystick("Rx") == 0:
        en["RF"].set_power(gamepad.get_joystick("Rx") / (1.6 * -1))
        en["RB"].set_power(gamepad.get_joystick("Rx") / (1.6 * -1))
        en["LB"].set_power(gamepad.get_joystick("Rx") / (1.6 * -1))
        en["LF"].set_power(gamepad.get_joystick("Rx") / (1.6 * -1))
        #power_expand_board.set_power("DC8",(gamepad.get_joystick("Rx") / (1.7 * -1)))#LF

    elif not gamepad.get_joystick("Lx") == 0:
        en["RF"].set_power(gamepad.get_joystick("Lx") / (1.6*-1))
        en["RB"].set_power(gamepad.get_joystick("Lx") / 1.5)
        en["LB"].set_power(gamepad.get_joystick("Lx") / 1.6)
        en["LF"].set_power(gamepad.get_joystick("Lx") / (1.6 * -1))
        #power_expand_board.set_power("DC8",(gamepad.get_joystick("Lx") / (1.7 * -1)))#LF
    
    elif not gamepad.get_joystick("Ly") == 0:
        en["LB"].set_power(gamepad.get_joystick("Ly") / 1.7)
        en["LF"].set_power(gamepad.get_joystick("Ly") / 1.635)
        en["RF"].set_power(gamepad.get_joystick("Ly") / (1.635 * -1))
        en["RB"].set_power(gamepad.get_joystick("Ly") / (1.7 * -1))
        #power_expand_board.set_power("DC8",(gamepad.get_joystick("Ly") / 1.7))#LF
    else:
        en["RF"].set_power(0)
        en["RB"].set_power(0)
        en["LB"].set_power(0)
        en["LF"].set_power(0)
        #power_expand_board.set_power("DC8",0)



#manual
class manual():

    def shooter_reload(power: int):
        power_expand_board.set_power("DC3",power)
        time.sleep(0.01)
        power_expand_board.set_power("DC3",0)
    
    def feed():
        power_expand_board.set_power("DC1", -motor1)
        power_expand_board.set_power("DC2", motor2)
        power_expand_board.set_power("DC3", -motor3)
        power_expand_board.set_power("DC4", -motor4)
    
    def forward(a:int):
        en["RF"].set_power(a / (1.6*-1))
        en["RB"].set_power(a / 1.5)
        en["LB"].set_power(a / 1.6)
        en["LF"].set_power(a / (1.6 * -1))

    def backward(a:int):
        en["RF"].set_power(a / 1.6)
        en["RB"].set_power(a / (1.5*-1))
        en["LB"].set_power(a / (1.6*-1))
        en["LF"].set_power(a / 1.6)

    def turn_left(a:int):
        en["RF"].set_power(a / (1.6 * -1))
        en["RB"].set_power(a / (1.6 * -1))
        en["LB"].set_power(a / (1.6 * -1))
        en["LF"].set_power(a / (1.6 * -1))

    def turn_right(a:int):
        en["RF"].set_power(a / (1.6 * 1))
        en["RB"].set_power(a / (1.6 * 1))
        en["LB"].set_power(a / (1.6 * 1))
        en["LF"].set_power(a / (1.6 * 1))

    def stop():
        en["RF"].set_power(0)
        en["RB"].set_power(0)
        en["LB"].set_power(0)
        en["LF"].set_power(0)


#auto
class auto :
 def auto1():
   manual.forward(100)
   time.sleep(2)
   manual.turn_left(100)
   time.sleep(1)


#main     
freefire = 0
while True:
    time.sleep(0.001)
    if power_manage_module.is_auto_mode():
        auto.auto1()
        while not not power_manage_module.is_auto_mode():
            pass
    else:
        joys.macanum_1()
        joys.control()

#test

# power_expand_board.set_power("DC1",100)
# power_expand_board.set_power("DC2",100)
# power_expand_board.set_power("DC3",100)
# power_expand_board.set_power("DC4",100)
# power_expand_board.set_power("DC5",100)
# power_expand_board.set_power("DC6",100)
# power_expand_board.set_power("DC7",100)
# power_expand_board.set_power("DC8",100)
# power_expand_board.set_power("BL1",100)
# power_expand_board.set_power("BL2",100)