# TODO: insert robot code here
import logging
log = logging.Logger('P212-robot')
import typing

import wpilib
import commands2
import commands2.cmd

import robotcontainer



class Robot(commands2.TimedCommandRobot):


    def robotInit(self) -> None:
   

        self.autonomousCommand: typing.Optional[commands2.Command] = None

        self.container = robotcontainer.RobotContainer()

        log.info('robot initialized')

    
    def autonomousInit(self) -> None:


        self.autonomousCommand = self.container.getAutonomousCommand()

        if self.autonomousCommand is not None:
            self.autonomousCommand.schedule()

        else:
            log.warning("no auto command")


    def teleopInit(self) -> None:
        
        if self.autonomousCommand is not None:
            self.autonomousCommand.cancel()

    #def teleopPeriodic(self) -> None:

    def testInit(self) -> None:
        commands2.CommandScheduler.getInstance().cancelAll()


if __name__ == "__main__":
    wpilib.run(Robot)    


        
