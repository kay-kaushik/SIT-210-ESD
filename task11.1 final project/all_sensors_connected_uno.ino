#include "DHT.h"
#include <Wire.h>
#include <BH1750.h>

// Data pin
#define DHTPIN 10
// Sensor type
#define DHTTYPE DHT22

// Initializing the DHT object
DHT dht(DHTPIN, DHTTYPE);

// Initializing the BH1750 object
BH1750 lightMeter;

// Soil moisture sensor pin
#define SOIL_MOISTURE_PIN A1

void setup() {
  Serial.begin(9600);
  while (!Serial) {
    ; // Wait for Serial Monitor to open
  }
  
  pinMode(LED_BUILTIN, OUTPUT);

  dht.begin();
  Wire.begin();
  lightMeter.begin();
}

void loop() {
  delay(2000); // Wait a few seconds between measurements

  // Read humidity
  float h = dht.readHumidity();
  // Read temperature as Celsius (the default)
  float t = dht.readTemperature();
  // Read light intensity
  float lux = lightMeter.readLightLevel();
  // Read soil moisture
  int soilMoistureValue = analogRead(SOIL_MOISTURE_PIN);
  
  // Check if any reads failed and exit early (to try again).
  if (isnan(h) || isnan(t)) {
    Serial.println(F("Failed to read from DHT sensor!"));
    return;
  }
  
  if (lux == 65535) {
    Serial.println(F("Failed to read from BH1750 sensor!"));
    return;
  }

  // Print the sensor readings to the Serial Monitor

  // Send the sensor data to the Raspberry Pi via UART
  Serial.print(F("H:"));
  Serial.print(h);
  Serial.print(F(",T:"));
  Serial.print(t);
  Serial.print(F(",L:"));
  Serial.print(lux);
  Serial.print(F(",SM:"));
  Serial.println(soilMoistureValue);
}



