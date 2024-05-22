// kartik kaushik, student id - 219052482. Code for task 1.1P 

// the following code blinks my name in morse code, this is acheived by using a long blink signifying a line/ dash and a short blink signifying a dot.

void setup()
 {
  // initialize digital pin LED_BUILTIN as an output.
  pinMode(LED_BUILTIN, OUTPUT);
}

// a dash is represented by the led being turned on for 4 secoonds, a dot is represented by an led being on for 2 seconds. 
void loop() 
{
   // morse code for 'K' (- . -)
  digitalWrite(LED_BUILTIN, HIGH);

  delay(4000);

  digitalWrite(LED_BUILTIN, LOW);

  delay(1000);
  
  digitalWrite(LED_BUILTIN, HIGH);
  
  delay(2000);
 
  digitalWrite(LED_BUILTIN, LOW);
  
  delay(1000);
  
  digitalWrite(LED_BUILTIN, HIGH);

  delay(4000);
  
  digitalWrite(LED_BUILTIN, LOW);
  
  delay(1000);
  
  //morse code for 'A' (. -)
  
  digitalWrite(LED_BUILTIN, HIGH);
  
  delay(2000);
 
  digitalWrite(LED_BUILTIN, LOW);
  
  delay(1000);
  
  digitalWrite(LED_BUILTIN, HIGH);

  delay(4000);

  digitalWrite(LED_BUILTIN, LOW);

  delay(1000);
  
  //morse code for 'R' (. - .)
  
  digitalWrite(LED_BUILTIN, HIGH);
  
  delay(2000);
 
  digitalWrite(LED_BUILTIN, LOW);
  
  delay(1000);
  
  digitalWrite(LED_BUILTIN, HIGH);

  delay(4000);

  digitalWrite(LED_BUILTIN, LOW);
  
  delay(1000);
  
  digitalWrite(LED_BUILTIN, HIGH);
  
  delay(2000);
 
  digitalWrite(LED_BUILTIN, LOW);
  
  delay(1000);
  
  //morse code for 'T' (-)
  
  digitalWrite(LED_BUILTIN, HIGH);

  delay(4000);

  digitalWrite(LED_BUILTIN, LOW);
  
  delay(1000);
  
  // morse code for 'I' (. .)
  
  digitalWrite(LED_BUILTIN, HIGH);
  
  delay(2000);
 
  digitalWrite(LED_BUILTIN, LOW);
  
  delay(1000);
  
  digitalWrite(LED_BUILTIN, HIGH);
  
  delay(2000);
 
  digitalWrite(LED_BUILTIN, LOW);
  
  delay(1000);
  
  //morse code for 'K' (- . -)
  
  digitalWrite(LED_BUILTIN, HIGH);

  delay(4000);

  digitalWrite(LED_BUILTIN, LOW);
  
  delay(1000);
  
  digitalWrite(LED_BUILTIN, HIGH);
  
  delay(2000);
 
  digitalWrite(LED_BUILTIN, LOW);
  
  delay(1000);
  
  digitalWrite(LED_BUILTIN, HIGH);

  delay(4000);
  
  digitalWrite(LED_BUILTIN, LOW);
  
  delay(1000);
  
  // repeat
}
