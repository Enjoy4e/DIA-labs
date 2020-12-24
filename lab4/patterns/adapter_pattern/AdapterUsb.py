from patterns.adapter_pattern.LightningWire import LightningWire
from patterns.adapter_pattern.UsbWire import UsbWire


class AdapterUsb(LightningWire):
    def __init__(self, usbwire: UsbWire):
        self.usbwire = usbwire

    def get_port(self) -> str:
        if self.usbwire.get_port() == "usb": # если разъемы переходника и кабеля совпадают, то мы соединяем переходник и получаем другой разъем на выходе
            return "lightning"
        else:
            return "incompatible ports"

