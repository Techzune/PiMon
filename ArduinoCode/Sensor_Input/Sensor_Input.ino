#include <NewPing.h>

#define SONAR1_trig 12
#define SONAR1_echo 11
#define LIMITSWITCH1 8

NewPing sonar(SONAR1_trig, SONAR1_echo);

String incoming = "";
String outgoing = "";

void setup() 
{
  Serial.begin(115200);
  Serial.setTimeout(2);

  pinMode(LIMITSWITCH1, INPUT_PULLUP);
}

void loop() 
{
}

// Generic data extractions and unit for each category of sensor
String getSonarData(String name, NewPing sonarSensor)
{
  String output = name+",num,";
  double medianTime = sonarSensor.ping_median(5);
  output = output+sonarSensor.convert_cm(medianTime)+",cm;";
  return output;
}

String getLimitSwitchData(String name, int switchPin)
{
  String output = name+",bool,";
  output = output + digitalRead(switchPin) + ",bool;";
  return output;
}

// Aggregate data into message to be sent to Pi
String getSensorData()
{
  String output = "";
  // sensor data: <sensorName>,<dataType>,<data>,<units>
  // Sensor data is composed of comma ',' separated attributes
  
  // message data: <sensorData>;<sensorData>;\n
  // Messages are composed of semicolon ';' separated sensor readings and end with newline '\n'
  
  //Sonar sensors:
  // sonar
  output = output + getSonarData("sonar1",sonar);

  //Limit switch sensors:
  // LIMITSWITCH1
  output = output + getLimitSwitchData("limitSwitch1", LIMITSWITCH1);

  //DEBUG PLEASE REMOVE
  output = output + "sonar2,num,11.5,in;Front Sonar,num,1.34,feet;";
  if (digitalRead(LIMITSWITCH1) == HIGH)
  {
    output = output + "debug.senors,str,This is some test code-ignore me,str;";
  }
  return output;
}

// Serial input parser
void serialEvent()
{
  // recieve input
  while (Serial.available())
  {
    String readString = Serial.readString();
    incoming += readString;
  }
  incoming.trim();

  // command interpreters
  outgoing = cmdGetSensorData(incoming);

  // reply if desired
  if (outgoing != "")
  {
    Serial.print(outgoing + "\n");
    outgoing = "";
  }
  incoming = "";
}

String cmdGetSensorData(String command)
{
  if (command.compareTo("get sensors") == 0)
  {
    return getSensorData();
  }
  return "";
}