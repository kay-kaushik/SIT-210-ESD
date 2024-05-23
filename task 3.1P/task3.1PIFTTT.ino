// necessary libraries
#include <Wire.h>
#include <BH1750.h>
#include "wifi.h"
#include <WiFiNINA.h>
#include <ArduinoHttpClient.h>

// initialising the sensor
BH1750 lightMeter;

// setting id pass for wifi
char ssid[] = SECRET_SSID;   // your network SSID (name) 
char pass[] = SECRET_PASS;   // your network password
WiFiClient  wifi;

// IFTTT ad http data
const char* serverAddress = "maker.ifttt.com";
const int port = 80;
const char* webHookUrl = "https://maker.ifttt.com/trigger/light_detected/with/key/fxpHNgIezl9k1iNw-qJ9R0Hn6-Xr1Iw7qsnk3GYEMHh";
const char* webHookUrlNd = "https://maker.ifttt.com/trigger/light_not_detected/with/key/fxpHNgIezl9k1iNw-qJ9R0Hn6-Xr1Iw7qsnk3GYEMHh";
HttpClient client = HttpClient(wifi, serverAddress, port);

//function to send http post to the ifttt applet
void iftttTrigger(const char* url)
{
  Serial.println("Sending data to the IFTTT");

  client.post(url);

  // read the status code and body of the response
  int statusCode = client.responseStatusCode();
  String response = client.responseBody();

  Serial.print("Status code: ");
  Serial.println(statusCode);
  Serial.print("Response: ");
  Serial.println(response);

  Serial.println("Wait five seconds");
  delay(5000);
}

void setup() 
{
  Wire.begin();
  Serial.begin(9600);

  // Connect or reconnect to WiFi
  if(WiFi.status() != WL_CONNECTED)
  {
    Serial.print("Attempting to connect to SSID: ");
    Serial.println(SECRET_SSID);
    while(WiFi.status() != WL_CONNECTED){
      WiFi.begin(ssid, pass); 
      Serial.print(".");
      delay(5000);     
    } 
    Serial.println("\nConnected.");
  }

  lightMeter.begin();


}

void loop() 
{

  // light detection
  float lux = lightMeter.readLightLevel();
  Serial.print("Light: ");
  Serial.print(lux);
  Serial.println(" lx");

  // if lux above 500 send light detected trigger
  if (lux > 500)
  {
    Serial.println("Sending notification to the owner!!");
    iftttTrigger(webHookUrl);
    delay(20000);
  }
  else                                                         // else send light not detected trigger
  {
    Serial.println("not enough light");
    iftttTrigger(webHookUrlNd);
    delay(20000);
  }
  delay(1000);
}

