# ESP32 MQTT Home Automation

An ESP32-based home automation system that connects to predefined WiFi networks and communicates with an MQTT broker to control appliances like lights and fans using JSON messages.

## Features

    **WiFi Auto-Connect:**  Scans and connects to specified WiFi networks.
    **MQTT Communication:** Sends and receives device control messages.
    **JSON Command Parsing:**  Processes JSON messages to control devices via GPIO.
    **Device Control:** Manages appliances such as fans and lights.
    **LED Indicator:** Signals successful WiFi connection.

## Components and Libraries
### Hardware
    ESP32 Development Board: Microcontroller with WiFi capabilities.

## Software Libraries

1. WiFi: For WiFi connectivity.
2. PubSubClient: For MQTT communication.
3. ArduinoJson: For JSON parsing.

## Installation

    Clone the Repository:

    git clone https://github.com/jenis-das/ESP32-MQTT-Home-Automation.git
    cd ESP32-MQTT-Home-Automation

    Setup in Arduino IDE:
        Install required libraries: PubSubClient and ArduinoJson.
        Update the knownNetworks array with your WiFi SSIDs and passwords.
        Configure MQTT broker details (mqttServer, mqttPort).
        Upload the code to the ESP32.

## Flask Backend

The Flask backend (app.py) provides an API for MQTT communication with ESP32 devices.
Features

1.    API Integration: Manages MQTT messaging for device control.
2.    JSON Handling: Parses and sends JSON-based commands.
3.    Device Control: Allows remote appliance management.

## Installation

   ### Requirements:
        Python 3.7+
        pip (Python package manager)

   ### Setup:
    pip install -r requirements.txt
    python app.py

## HTML and JavaScript Frontend

A simple web interface for controlling devices via the Flask backend.

### Features

    Interactive UI: User-friendly buttons to send commands.
    API Integration: Communicates with the backend using RESTful APIs.

### Setup
    Open frontend.html in any modern browser.
    Use the interface to send commands like turning appliances on/off.

### Future Enhancements

    Add authentication for secure API usage.
    Build a responsive frontend with frameworks like React.
    Extend API to retrieve device statuses.

License
This project is licensed under the MIT License.