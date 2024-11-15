# from flask import Flask, render_template, request, jsonify
# import paho.mqtt.client as mqtt
# import json

# app = Flask(__name__)

# # MQTT Broker settings
# BROKER_ADDRESS = "test.mosquitto.org"  # Public broker for testing
# PORT = 8080
# TOPIC = "myserverdata"

# # Initialize the MQTT client and set it to use WebSockets
# mqtt_client = mqtt.Client(transport="websockets")
# mqtt_client.connect(BROKER_ADDRESS, PORT, 60)
# mqtt_client.loop_start()


# def buttonCheck(button_name, state):
#     if button_name == "fan":
#         if state == "on":
#             pub = 11
#             return pub
#         else:
#             pub = 10
#             return pub
#     elif button_name == "kitchen":
#         if state == "on":
#             pub = 21
#             return pub
#         else:
#             pub = 20
#             return pub
#     elif button_name == "hallLight":
#         if state == "on":
#             pub = 31
#             return pub
#         else:
#             pub = 30
#             return pub
#     elif button_name == "roomLight":
#         if state == "on":
#             pub = 41
#             return pub
#         else:
#             pub = 40
#             return pub

# @app.route('/')
# def home():
#     return render_template('index.html')

# @app.route('/button_click', methods=['POST'])
# def button_click():
#     data = request.json
#     button_name = data.get('button')
#     state = data.get('state')
#     print(f"{button_name}/{state}")  # Logs the message to the terminal
#     # buttonCheck(button_name, state)
#     # Publish the state to MQTT
#     # mqtt_client.publish(TOPIC, f"{button_name}/{state}")

#     # data = {"button": button_name, "status": state}
#     # json_data = json.dumps(data)  # Serialize data to JSON string
#     # mqtt_client.publish(TOPIC, json_data)
#     toPublish = buttonCheck(button_name, state)

#     mqtt_client.publish(TOPIC, toPublish)
#     return jsonify({"message": f"{button_name} is now {state} and data sent to MQTT"})



# if __name__ == '__main__':
#     app.run(debug=True)



# from flask import Flask, render_template, request, jsonify
# import paho.mqtt.client as mqtt
# import json

# app = Flask(__name__)

# # MQTT Broker settings
# BROKER_ADDRESS = "test.mosquitto.org"  # Public broker for testing
# PORT = 8080  # Use 8080 if your broker requires WebSockets, else try 1883
# TOPIC = "myserverdata"

# # Initialize the MQTT client and set to WebSockets if required by broker
# mqtt_client = mqtt.Client(transport="websockets")
# mqtt_client.connect(BROKER_ADDRESS, PORT, 60)
# mqtt_client.loop_start()

# def buttonCheck(button_name, state):
#     """Returns encoded integer based on button and state."""
#     return {
#         ("fan", "on"): 1, ("fan", "off"): 2,
#         ("kitchen", "on"): 3, ("kitchen", "off"): 4,
#         ("hallLight", "on"): 5, ("hallLight", "off"): 6,
#         ("roomLight", "on"): 7, ("roomLight", "off"): 8
#     }.get((button_name, state), None)

# @app.route('/')
# def home():
#     return render_template('index.html')

# @app.route('/button_click', methods=['POST'])
# def button_click():
#     data = request.json
#     button_name = data.get('button')
#     state = data.get('state')
    
#     print(f"{button_name}/{state}")  # Logs the button action to the terminal

#     # Encode the button state
#     toPublish = buttonCheck(button_name, state)
#     if toPublish is None:
#         return jsonify({"error": "Invalid button or state"}), 400

#     # Publish data as JSON-encoded message
#     message = json.dumps({"button": button_name, "status": state})
#     # print(buttonCheck(button_name, state))

#     nowMessage = buttonCheck(button_name, state)
#     print(nowMessage)
#     mqtt_client.publish(TOPIC, nowMessage)
#     # return jsonify({"message": f"{button_name} is now {state} and data sent to MQTT"})
#     return 
# if __name__ == '__main__':
#     app.run(debug=True)




from flask import Flask, render_template, request, jsonify
import paho.mqtt.client as mqtt
import json

app = Flask(__name__)

# MQTT Broker settings
BROKER_ADDRESS = "test.mosquitto.org"  # Public broker for testing
PORT = 8080  # Use 8080 if your broker requires WebSockets, else try 1883
TOPIC = "myserverdata"

# Initialize the MQTT client and set to WebSockets if required by broker
mqtt_client = mqtt.Client(transport="websockets")
mqtt_client.connect(BROKER_ADDRESS, PORT, 60)
mqtt_client.loop_start()

def buttonCheck(button_name, state):
    """Returns encoded integer based on button and state."""
    return {
        ("fan", "on"): 1, ("fan", "off"): 2,
        ("kitchen", "on"): 3, ("kitchen", "off"): 4,
        ("hallLight", "on"): 5, ("hallLight", "off"): 6,
        ("roomLight", "on"): 7, ("roomLight", "off"): 8
    }.get((button_name, state), None)

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/button_click', methods=['POST'])
def button_click():
    data = request.json
    button_name = data.get('button')
    state = data.get('state')
    
    print(f"{button_name}/{state}")  # Logs the button action to the terminal

    # Encode the button state
    toPublish = buttonCheck(button_name, state)
    print(toPublish)

    if toPublish is None:
        return jsonify({"error": "Invalid button or state"}), 400

    # Publish data as JSON-encoded message
    mqtt_client.publish(TOPIC, str(toPublish))
    return jsonify({"message": f"{button_name} is now {state} and data sent to MQTT"})

if __name__ == '__main__':
    app.run(debug=True, host="0.0.0.0", port=5000)