#include <WiFi.h>                // For ESP32 WiFi connection
#include <PubSubClient.h>         // For MQTT communication
#include <ArduinoJson.h>          // For JSON deserialization

// Define your known networks
const char* knownNetworks[][2] = {
  {"realme 5i", "leodas07"},
  {"moto g64 5G_2678", "liliajasmine"},
  {"Samsung Z4", "guddudas"} 
};

int fan = 3;
int kitchen = 4;
const int hallLight = 5;
const int roomLight = 6;

const int led = 2; // LED for wifi connect

const char* mqttServer = "test.mosquitto.org";  // Use a public broker or your own
const int mqttPort = 8080; 

WiFiClient wifiClient;  // WiFi client object
PubSubClient client(wifiClient);  // MQTT client object

void callback(char* topic, byte* payload, unsigned int length) {
  Serial.print("Message received on topic: ");
  Serial.println(topic);

  StaticJsonDocument<200> doc;

  // Deserialize the payload to the JSON object
  DeserializationError error = deserializeJson(doc, payload, length);

  if (error) {
    Serial.print("Failed to parse JSON: ");
    Serial.println(error.f_str());
    return;
  }

  const char* button = doc["button"];  // Access 'button' field
  const char* status = doc["status"];  // Access 'status' field
  Serial.print("Button: ");
  Serial.println(button);
  Serial.print("Status: ");
  Serial.println(status);

  // Control logic based on button and status
  if (strcmp(button, "fan") == 0) {
    if (strcmp(status, "on") == 0) {
      digitalWrite(fan, HIGH);  // Turn fan on
    } else {
      digitalWrite(fan, LOW);   // Turn fan off
    }
  } else if (strcmp(button, "kitchen") == 0) {
    if (strcmp(status, "on") == 0) {
      digitalWrite(kitchen, HIGH);  // Turn kitchen light on
    } else {
      digitalWrite(kitchen, LOW);   // Turn kitchen light off
    }
  } else if (strcmp(button, "hallLight") == 0) {
    if (strcmp(status, "on") == 0) {
      digitalWrite(hallLight, HIGH);  // Turn hall light on
    } else {
      digitalWrite(hallLight, LOW);   // Turn hall light off
    }
  } else if (strcmp(button, "roomLight") == 0) {
    if (strcmp(status, "on") == 0) {
      digitalWrite(roomLight, HIGH);  // Turn room light on
    } else {
      digitalWrite(roomLight, LOW);   // Turn room light off
    }
  }
}

// Reconnect function to handle MQTT disconnections
void reconnect() {
  while (!client.connected()) {
    Serial.print("Attempting MQTT connection...");
    if (client.connect("ESP32Client")) {
      Serial.println("Connected");
      client.subscribe("myserverdata");  // Resubscribe to the topic
    } else {
      Serial.print("Failed, rc=");
      Serial.print(client.state());
      delay(5000);
    }
  }
}

void setup() {
  Serial.begin(115200);
  pinMode(led, OUTPUT);
  pinMode(fan, OUTPUT);
  pinMode(kitchen, OUTPUT);
  pinMode(hallLight, OUTPUT);
  pinMode(roomLight, OUTPUT);

  // Set MQTT server and callback function
  client.setServer(mqttServer, mqttPort);
  client.setCallback(callback);

  // Scan for available networks
  int numberOfNetworks = WiFi.scanNetworks();
  Serial.println("Scanning for networks...");

  Serial.print("SSID Available: ");
  for (int i = 0; i < numberOfNetworks; i++) {
    String ssid = WiFi.SSID(i);
    Serial.print(ssid + ",");
  }

  // Try to connect to one of the known networks
  for (int i = 0; i < numberOfNetworks; i++) {
    String ssid = WiFi.SSID(i);
    Serial.println("Found network: " + ssid);

    // Check if the found network is one of the known networks
    for (int j = 0; j < sizeof(knownNetworks)/sizeof(knownNetworks[0]); j++) {
      if (ssid == knownNetworks[j][0]) {
        Serial.println("Known network found: " + ssid);
        WiFi.begin(knownNetworks[j][0], knownNetworks[j][1]);
        if (connectToWiFi()) {
          return; // Exit the loop if connected
        }
      }
    }
  }

  Serial.println("No known networks found or failed to connect.");
}

bool connectToWiFi() {
  Serial.print("Connecting");
  int attempts = 10; // Max attempts to connect

  while (WiFi.status() != WL_CONNECTED && attempts > 0) {
    delay(1000);
    Serial.print(".");
    attempts--;
  }

  if (WiFi.status() == WL_CONNECTED) {
    Serial.println("\nConnected!");
    digitalWrite(led, HIGH);  // Turn the LED on
    delay(3000);
    digitalWrite(led, LOW);   // Turn the LED off
    Serial.print("IP Address: ");
    Serial.println(WiFi.localIP());
    return true;
  } else {
    Serial.println("\nFailed to connect.");
    return false;
  }
}

void loop() {
  client.loop();  // Keeps the MQTT connection alive

  if (!client.connected()) {
    reconnect();  // Reconnect if MQTT connection is lost
  }
  delay(100);
}