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
      analogWrite (E1, 0);
      analogWrite (E2, 0);
      break;
    case '1':
      analogWrite (E1, 255);
      analogWrite (E2, 255);
      break;
    case '2':
      analogWrite (E1, 255);
      analogWrite (E2, 0);
      break;
    case '3':
      analogWrite (E1, 0);
      analogWrite (E2, 255);
      break;
    case '4':
      analogWrite (E1, 255);
      analogWrite (E2, 255);
      break;
    default:
      break;
  }
}

