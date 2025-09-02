# Import the basic framework components.
from softioc import softioc, builder
import cothread

# Set the record prefix
builder.SetDeviceName("Rack1")

# Create some records
# Rack1-AC_State_Coil
ai = builder.aIn('AI', initial_value=5)
ao = builder.aOut('AO', initial_value=12.45, on_update=lambda v: ai.set(v))
bi = builder.boolOut('AC_State_Coil', '0', '1', initial_value=0)

# Boilerplate get the IOC started
builder.LoadDatabase()
softioc.iocInit()
softioc.dbl()

# Start processes required to be run after iocInit
def update():
    while True:
        ai.set(ai.get() + 1)
        print(ai.get())
        cothread.Sleep(1)


cothread.Spawn(update)

cothread.WaitForQuit()