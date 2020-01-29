
Skip to content
Pull requests
Issues
Marketplace
Explore
@ssreekanth2000
Learn Git and GitHub without any code!

Using the Hello World guide, you’ll start a branch, write comments, and open a pull request.
aselker /
watts-scope-2019-20
Private

2
0

    0

Code
Issues 0
Pull requests 0
Actions
Projects 0
Security
Insights
watts-scope-2019-20/azure/raspi.py
@ssreekanth2000 ssreekanth2000 This works f91383b 3 hours ago
54 lines (38 sloc) 1.6 KB
Code navigation is available!

Navigate your code with ease. Click on function and method calls to jump to their definitions or references in the same repository. Learn more

Code navigation is available for this repository but data for this commit does not exist.
Learn more or give us feedback
#!/usr/bin/env python3

import random
import time
from azure.iot.device import IoTHubDeviceClient, Message

# The device connection string to authenticate the device with your IoT hub.
CONNECTION_STRING = "HostName=Watts-Paid.azure-devices.net;DeviceId=WinterBreak;SharedAccessKey=KcpZcZfeE2XyCCTu0v9EZ2CwxVE+ha0NqcgZiUTP+E0="

# Message structure is defined here
TEMPERATURE = 20.0
HUMIDITY = 60
DEVICE = 2
MSG_TXT = '{{"temperature": {temperature},"device":{device}}}'

temperature = ''
device = ''




def iothub_client_init():
    # Create an IoT Hub client using the deivce connection string
    client = IoTHubDeviceClient.create_from_connection_string(CONNECTION_STRING)
    return client


def iothub_client_telemetry_sample_run():
    try:
        client = iothub_client_init()
        print("IoT Hub device sending periodic messages, press Ctrl-C to exit")

        while True:
            temperature = TEMPERATURE + (random.random() * 15)
            humidity = HUMIDITY + (random.random() * 20)
            device = 3
            msg_txt_formatted = MSG_TXT.format(temperature=temperature, humidity=humidity, device=device)
            message = Message(msg_txt_formatted)

                # Send the message.
            print("Sending message: {}".format(message))
            client.send_message(message)
                # print("Message successfully sent")

            time.sleep(0.1)

    except KeyboardInterrupt:
        print("IoTHubClient sample stopped")


if __name__ == "__main__":
    print("IoT Hub Quickstart #1 - Simulated device")
    print("Press Ctrl-C to exit")
    iothub_client_telemetry_sample_run()

    © 2020 GitHub, Inc.
    Terms
    Privacy
    Security
    Status
    Help

    Contact GitHub
    Pricing
    API
    Training
    Blog
    About
