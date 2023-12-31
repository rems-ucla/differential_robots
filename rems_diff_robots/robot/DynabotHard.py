from rems.robots import RobotBase
from rems_diff_robots.device.Dynamixel.Dynamixel import Dynamixel
from rems_diff_robots.device.ArucoDevice import ArucoDevice


ID_LISTs = [2, 1]



class DynabotHard(RobotBase):
    DEVICE_LIST = [Dynamixel, ArucoDevice]
    def __init__(self, port, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.run.DT = 0.05
        self.run.name = 'Hard'
        self.port = port

    def init_devices(self):
        self.add_device(Dynamixel(ID_LISTs, device_port=self.port))
        self.add_device(ArucoDevice(track_id=2, camera_id=0))

    def init(self, *args, **kwargs):
        super().init(*args, **kwargs)




