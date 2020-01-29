#!/usr/bin/env python3

import random
import time
import serial
from azure.iot.device import IoTHubDeviceClient, Message

# The device connection string to authenticate the device with your IoT hub.
CONNECTION_STRING = "HostName=Watts-Paid.azure-devices.net;DeviceId=WinterBreak;SharedAccessKey=KcpZcZfeE2XyCCTu0v9EZ2CwxVE+ha0NqcgZiUTP+E0="

# Message structure is defined here
MSG_TXT = '{{"temperature":{temperature},"device":{device},"timestamp1":{timestamp1}}}'

ser = serial.Serial("/dev/ttyS0", 230400)
timestamp1 = 323

def iothub_client_init():
    # Create an IoT Hub client using the deivce connection string
    client = IoTHubDeviceClient.create_from_connection_string(CONNECTION_STRING)
    return client


def iothub_client_telemetry_sample_run():
    try:
        client = iothub_client_init()
        print("IoT Hub device sending periodic messages, press Ctrl-C to exit")

        while True:
            while ser.in_waiting > 0:  # While there is data in Serial
                line = ser.readline()  # Read a line in serial
                # print("Line: {}".format(line))
                broken_line = (
                    str(line.decode("UTF-8")).replace("\r", "").replace("\n", "").split(",")
                )
                # print("Broken line: {}".format(broken_line))
                # Extract vlues from the serial line
                device = broken_line[0]
                temperature = broken_line[1]



                msg_txt_formatted = MSG_TXT.format(
                    temperature=temperature, device=device, timestamp1=timestamp1
                )
                # print("Formatted text: {}".format(msg_txt_formatted))
                # structured message using the data recieved.
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
