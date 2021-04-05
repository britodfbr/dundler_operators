class IncolumeDevices0:
    def __init__(self):
        self._devices = [
            'avel C65 i9 Pro',
            'asus zenfone ASUS_Z01KDA',
            'epson ecotank L6191',
            'hp office jet pro 8600',
            'microboard centturion core 2 duo',
            'microboard centturion ME i7',
            'multilaser M10A',
            'asus zenfone2',
            'nokia 1600 GSM',
        ]


class IncolumeDevices1(IncolumeDevices0):
    def __len__(self):
        return len(self._devices)


class IncolumeDevices2(IncolumeDevices1):
    def __getitem__(self, item):
        if isinstance(item, int):
            return self._devices.pop(item)
        else:
            raise TypeError(f'Not founded key {item}')


class IncolumeDevices3(IncolumeDevices2):
    def __contains__(self, item):
        return item in self._devices


class IncolumeDevices4(IncolumeDevices3):
    def __iter__(self):
        while self._devices:
            yield self._devices.pop()