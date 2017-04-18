const int E1 = 5, E2 = 6;
const int H1 = 4, H2 = 7;

void turn (char direction);


void setup () 
{
  Serial.begin (9600);
  
  for (int i = 4; i <= 7; i++)
    pinMode (i, OUTPUT);
}

void loop () 
{
  while(Serial.available ())
  {
    char direction = Serial.read ();
    turn (direction);
  }
}

void turn (char direction)
{
  if (direction == '4')
  {
    digitalWrite (H1, LOW);
    digitalWrite (H2, LOW);
  }

  else
  {
    digitalWrite (H1, HIGH);
    digitalWrite (H2, HIGH);
  }

  switch (direction)
  {
    case '0':
      digitalWrite (E1, LOW);
      digitalWrite (E2, LOW);
      Serial.println("STOP");
      break;
    case '1':
      digitalWrite (E1, HIGH);
      digitalWrite (E2, HIGH);
      Serial.println("FORWARD");
      break;
    case '2':
      digitalWrite (E1, HIGH);
      digitalWrite (E2, LOW);
      Serial.println("RIGHT");
      break;
    case '3':
      digitalWrite (E1, LOW);
      digitalWrite (E2, HIGH);
      Serial.println("LEFT");
      break;
    case '4':
      digitalWrite (E1, HIGH);
      digitalWrite (E2, HIGH);
      Serial.println("BACKWARD");
      break;
    default:
      break;
  }
}

