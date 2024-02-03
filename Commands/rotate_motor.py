#
# Copyright (c) FIRST and other WPILib contributors.
# Open Source Software; you can modify and/or share it under the terms of
# the WPILib BSD license file in the root directory of this project.
#


import wpilib
import commands2
import commands2.cmd
import wpimath.controller

from Subsystem.hang_ss import HangSubsystem

import constants

import logging
logger = logging.getLogger("aniyah")


class Hang(commands2.Command):
    def __init__(self, hang_ss: HangSubsystem) -> None:
        super().__init__()
        self.hang_ss = hang_ss

    def initialize(self):
        logger.info("running Hang command")

    def execute(self):
        self.hang_ss.rotate_left()

    def isFinished(self):
        # command does not finish it needs to be cancelled
        return False

    def end(self, interrupted):
        self.hang_ss.stop()
        


class Lower(commands2.Command):
    def __init__(self, hang_ss: HangSubsystem) -> None:
        super().__init__()
        self.hang_ss = hang_ss

    def execute(self):
        self.hang_ss.rotate_right()

    def isFinished(self):
        # The command needs to be cancelled in order to stop
        return False

    def end(self, interrupted):
        self.hang_ss.stop()


class StopMotor(commands2.Command):
    def __init__(self, hang_ss: HangSubsystem) -> None:
        super().__init__()
        self.hang_ss = hang_ss

    def initialize(self):
        logger.info("running StopMotor command")

    def execute(self):
        self.hang_ss.stop()

    def isFinished(self):
        # The command needs to be cancelled in order to stop
        return False

    def end(self, interrupted):
        self.hang_ss.stop()
    
