from flask import Flask, render_template, request, redirect, url_for
from flask_wtf import Form
from wtforms import TextField

# Copyright (c) Microsoft. All rights reserved.
# Licensed under the MIT license. See LICENSE file in the project root for full license information.

import random
import time

# Using the Python Device SDK for IoT Hub:
#   https://github.com/Azure/azure-iot-sdk-python
# The sample connects to a device-specific MQTT endpoint on your IoT Hub.
from azure.iot.device import IoTHubDeviceClient, Message

# The device connection string to authenticate the device with your IoT hub.
# Using the Azure CLI:
# az iot hub device-identity show-connection-string --hub-name {YourIoTHubName} --device-id MyNodeDevice --output table
CONNECTION_STRING = "HostName=Watts-Paid.azure-devices.net;DeviceId=Python-deivce;SharedAccessKey=XW4VFenS3vvvGR9D7IEOeKB+Iu6+q72IX7SMVmyIFLQ="

# Define the JSON message to send to IoT Hub.
TEMPERATURE = 20.0
HUMIDITY = 60
DEVICE = 2
MSG_TXT = '{{"deviceID": {deviceID},"room":{room}}}'


DEVICEid = ''
ROOM = ''

def iothub_client_init():
    # Create an IoT Hub client
    client = IoTHubDeviceClient.create_from_connection_string(CONNECTION_STRING)
    return client
def iothub_client_telemetry_sample_run(deviceID, room):

    try:
        client = iothub_client_init()
        print ( "IoT Hub device sending periodic messages, press Ctrl-C to exit" )


        DEVICEid = deviceID
        ROOM = room
        #temperature = TEMPERATURE + (random.random() * 15)
        #humidity = HUMIDITY + (random.random() * 20)


        #device = 3
        msg_txt_formatted = MSG_TXT.format(deviceID=DEVICEid, room=ROOM)
        message = Message(msg_txt_formatted)

        # Add a custom application property to the message.
        # An IoT hub can filter on these properties without access to the message body.

            # Send the message.
        print( "Sending message: {}".format(message) )
        client.send_message(message)
        print ( "Message successfully sent" )
        time.sleep(1)

    except KeyboardInterrupt:
        print ( "IoTHubClient sample stopped" )
app = Flask(__name__)
app.config['SECRET_KEY'] = 'our very hard to guess secretfir'

@app.route('/index', methods=['GET', 'POST'])
def index():
    error = ""
    if request.method == 'POST':
        # Form being submitted; grab data from form.
        name = request.form['name']
        deviceID = request.form['deviceID']
        room = request.form['room']

        # Validate form data
        if len(name) == 0 or len(deviceID) ==0 or len(room)== 0:
            # Form data failed validation; try again
            error = "No fields can be left blank"
        else:
            # Form data is valid; move along
            print (deviceID)
            iothub_client_telemetry_sample_run(deviceID, room)
            return redirect(url_for('thank_you'))

    # Render the sign-up page
    return render_template('index.html', message=error)

@app.route('/thank-you', methods=['GET', 'POST'])
def thank_you():
    if request.method == 'POST':
        return redirect(url_for('index'))
    else:
        return render_template('thank-you.html')


# Run the application
app.run(debug=True)
