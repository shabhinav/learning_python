device_status = "offline"
temperature = 35


if device_status == "active":
    if temperature >35:
        print("temperature is high")
    else:
        print("temperature is normal")
else:
    print("device is offline")