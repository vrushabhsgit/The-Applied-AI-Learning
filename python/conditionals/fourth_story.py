# You're building a smart thermostat alert system:

# * If the `device_status` is "active"
# * And `temperature` > 35 $\rightarrow$ Warn: "High temperature alert!"
# * Else: "Temperature normal"


# * If device is off $\rightarrow$ "Device is offline"

device_status = 'active'
temp = 38

if device_status == "active":
    if temp > 35:
     print("Temp is high")
    else:
       print("Temp is normal")
else:
    print("The device is offline")
    

