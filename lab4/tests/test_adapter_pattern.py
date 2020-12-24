from patterns.adapter_pattern.Smartphone import Iphone
from patterns.adapter_pattern.LightningWire import LightningWire
from patterns.adapter_pattern.AdapterUsb import AdapterUsb
from patterns.adapter_pattern.UsbWire import UsbWire


def test_charging():
    iphone = Iphone()
    lightningwire = LightningWire()
    usbwire = UsbWire()
    adapterusb = AdapterUsb(usbwire)

    assert iphone.charge(lightningwire)
    assert not iphone.charge(usbwire)
    assert iphone.charge(adapterusb)
