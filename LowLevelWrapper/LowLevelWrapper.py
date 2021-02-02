from ctypes import cdll, c_float, c_void_p, c_bool

lib = cdll.LoadLibrary('./liblowlevel.so')


class LowLevelWrapper(object):
    def __init__(self):
        self.obj = lib.low_level_new()
        lib.low_level_set_pump_on_off.argtypes = [c_void_p, c_bool]
        lib.low_level_set_heat_on_off.argtypes = [c_void_p, c_bool]
        lib.low_level_set_power.argtypes = [c_void_p, c_float]
        lib.low_level_get_power.restype = c_float
        lib.low_level_get_temperature.restype = c_float

    def set_pump_on_off(self, on):
        lib.low_level_set_pump_on_off(self.obj, on)

    def set_heat_on_off(self, on):
        lib.low_level_set_heat_on_off(self.obj, on)

    def set_power(self, percent):
        lib.low_level_set_power(self.obj, percent)

    def get_power(self):
        return lib.low_level_get_power(self.obj)

    def get_temperature(self):
        return lib.low_level_get_temperature(self.obj)
