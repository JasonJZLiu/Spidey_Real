"""
@author     Jingzhou Liu
@email      jingzhou.liu@mail.utoronto.ca
@brief      Control interface for Spidey V2
"""

from adafruit_servokit import ServoKit


class Spidey_V2:
    """
    @brief This class provides the control interface for Spidey V2. Spidey V2 is a 12-DOF sprawling type quadruped, 
           with 3 MG90 servos on each leg.
    """

    def __init__(self):
        """
        Initializes the interface and defines internal variables. 
        """
        self.default_state = [0, 0, 0,
                              0, 0, 0,
                              0, 0, 0,
                              0, 0, 0]
        self._state = self.default_state

        self._default_servo_positions = [90, 90, 90,
                                         90, 90, 90,
                                         90, 90, 90,
                                         90, 90, 90]
                                        # [100, 70, 80,
                                        #  100, 80, 100,
                                        #  100, 80, 100,
                                        #  100, 70, 80]
        
        self._joint_to_channel_mapping = [6,  7,  8,
                                          3,  4,  5,
                                          9,  10, 11,
                                          0,  1,  2]

        self._servos = ServoKit(channels = 16) #channel 0 to 3 are not used by the servos


    """
    Properties
    """                                 
    @property
    def state(self):
        """
        :return: The current state of the robot. 
        """
        return self._state
    
    @property
    def servo_positions(self):
        """
        Mapping from joint space to actuator space
        :return: The current servo positions
        """
        servo_positions = self._state.copy()
        for i in [1, 4, 7, 10]:
            servo_positions[i] *= -1
        for i in range(12):
            servo_positions[i] += self._default_servo_positions[i]
            if servo_positions[i] >180:
                servo_positions[i] = 180
            elif servo_positions[i] < 0:
                servo_positions[i] = 0
        return servo_positions


    '''
    Internals
    '''
    def _update(self, position_cmd):
        """
        Updates the state internally
        :param position_cmd: Joint position command in the joint space in degrees
        """
        self._state = position_cmd
    

    '''
    Operations
    '''
    def apply_command(self, position_cmd):
        """
        Applies joint space position command to the robot.
        :param position_cmd: Joint position command in the joint space in degrees
        """
        self._update(position_cmd)
        servo_commands = self.servo_positions

        for i in range(12):
            self._servos.servo[self._joint_to_channel_mapping[i]].angle = servo_commands[i]
    