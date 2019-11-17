/******************** Message ***********************/
const std::string message = "voli vas tata";
/****************************************************/
int currentLetter = 0;

const int PIN  = 1;
const int HIGH = 1;
const int LOW  = 0;

const int DOT_DELAY    = 500;
const int DIT_DELAY    = 1500;
const int LETTER_DELAY = 1000;

static const std::string morseCodesLookup[] = {
    "-----", //0
    ".----", //1
    "..---", //2
    "...--", //3
    "....-", //4
    ".....", //5
    "-....", //6
    "--...", //7
    "---..", //8
    "----.", //9
    ".-",   //A
    "-...", //B
    "-.-.", //C
    "-..",  //D
    ".",    //E
    "..-.", //F
    "--.",  //G
    "....", //H
    "..",   //I
    ".---", //J
    "-.-",  //K
    ".-..", //L
    "--",   //M
    "-.",   //N
    "---",  //O
    ".--.", //P
    "--.-", //Q
    ".-.",  //R
    "...",  //S
    "-",    //T
    "..-",  //U
    "...-", //V
    ".--",  //W
    "-..-", //X
    "-.--", //Y
    "--..", //Z
    " ",   //' '
};

bool isNumeric(const char c) {
    return c > 47 && c < 58;
}
bool isLowerCase(const char c) {
    return c > 96 && c < 123;
}
bool isCaps(const char c) {
    return c > 64 && c < 91;
}

std::string GetMorseForAlfaNum(const char c) {
    if (isNumeric(c))   return morseCodesLookup[c - 48];
    if (isLowerCase(c)) return morseCodesLookup[c - 87];
    if (isCaps(c))      return morseCodesLookup[c - 55];
    if (c == 32) return morseCodesLookup[c + 4];
    return "";
}

void Display(const char c) {
    //std::cout << c;
    if (c == ' ') digitalWrite(PIN, LOW);        
    else digitalWrite(PIN, HIGH);
    delay(c == '.' ? DIT_DELAY : DOT_DELAY);
    digitalWrite(PIN, LOW);
    delay(DIT_DELAY);
}

void DisplayMorseCode(std::string code) {
	for (std::string::size_type i = 0; i < code.size(); i++) {
		Display(code[i]);
	}
}

void setup() {                
    pinMode(PIN, OUTPUT);
}

void loop() {
  DisplayMorseCode(GetMorseForAlfaNum(message[currentLetter]));
  delay(LETTER_DELAY);
  std::cout << std::endl;
  currentLetter = ++currentLetter % message.length();
}
