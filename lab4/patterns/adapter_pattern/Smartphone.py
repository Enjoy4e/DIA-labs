from patterns.adapter_pattern.LightningWire import LightningWire
import time


class Iphone:
    def __init__(self):
        self.__port = "lightning"

    def charge(self, wire: LightningWire):
        if self.__port == wire.get_port():
            print("Charging...")
            time.sleep(1)
            print("Your iphone is fully charged")
            return True
        else:
            print("Incompatible ports")
            return False
