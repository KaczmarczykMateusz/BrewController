g++ -c -fPIC LowLevelApi.cpp -o LowLevelApi.o
g++ -shared -Wl,-soname,liblowlevel.so -o liblowlevel.so  LowLevelApi.o



Way of using code:
low_Level = LowLevelWrapper()
print(low_Level.get_power())
low_Level.set_power(58.1)
print(f"{low_Level.get_power():.2f}")
