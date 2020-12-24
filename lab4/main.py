from patterns.fabric_pattern.MilkFabric import CheeseFabric, SourCreameFabric
from patterns.adapter_pattern.Smartphone import Iphone
from patterns.adapter_pattern.LightningWire import LightningWire
from patterns.adapter_pattern.AdapterUsb import AdapterUsb
from patterns.adapter_pattern.UsbWire import UsbWire
from patterns.method_pattern.GameAI import ElfBaseAI, OrcBaseAI

if __name__ == '__main__':
    cheeseFabric = CheeseFabric()
    print(cheeseFabric.deliver(2))
    sourcreameFabric = SourCreameFabric()
    print(sourcreameFabric.deliver(3))

    iphone = Iphone()
    lightningwire = LightningWire()
    usbwire = UsbWire()
    adapterusb = AdapterUsb(usbwire)
    print(iphone.charge(lightningwire))
    print(iphone.charge(adapterusb))
    print(iphone.charge(usbwire))

    ElfBase = ElfBaseAI(2000)
    Orcbase = OrcBaseAI(2000)
    ElfBase.turn(Orcbase)
    Orcbase.turn(ElfBase)





