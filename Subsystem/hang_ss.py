# TODO: insert robot code here
import wpilib
import commands2
import rev
from constants import ELEC



class HangSubsystem(commands2.Subsystem):
    def __init__(self):
        super().__init__()
        self.motor = rev.CANSparkMax(ELEC.hang_motor_CAN_ID, rev.CANSparkMax.MotorType.kBrushless)
        self.controller = wpilib.XboxController(0)

        
    def rotate_left(self):
        self.motor.set(-0.3)

    
    def rotate_right(self):
        self.motor.set(0.3)

    
    def stop(self):
        self.motor.set(0)

    def is_stopped(self):
        motor_speed = self.motor.get()
        if motor_speed == 0:
            return True
        else:
            return False