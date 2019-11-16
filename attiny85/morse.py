msg = "VOLI VAS TATA"

morse = {
    'A':'.-', 'B':'-...', 'C':'-.-.', 'D':'-..', 'E':'.', 
    'F':'..-.', 'G':'--.', 'H':'....', 'I':'..', 'J':'.---', 'K':'-.-', 
    'L':'.-..', 'M':'--', 'N':'-.', 'O':'---', 'P':'.--.', 'Q':'--.-', 
    'R':'.-.', 'S':'...', 'T':'-', 'U':'..-', 'V':'...-', 'W':'.--', 
    'X':'-..-', 'Y':'-.--', 'Z':'--..', '1':'.----', '2':'..---', '3':'...--', 
    '4':'....-', '5':'.....', '6':'-....', '7':'--...', '8':'---..', '9':'----.', 
    '0':'-----', ', ':'--..--', '.':'.-.-.-', '?':'..--..', '/':'-..-.', '-':'-....-', 
    '(':'-.--.', ')':'-.--.-'} 

m = ""
for i in msg:
  if i==" ":
    m += "  "
  else:
    m+=morse[i]
    m+=" "

#print(m)

code = {".":"    digitalWrite(1, HIGH); delay(500); digitalWrite(1, LOW); delay(500);    // morse: .",
        "-":"    digitalWrite(1, HIGH); delay(1000); digitalWrite(1, LOW); delay(500);   // morse: -",
        " ":"    delay(1000);                                                            // morse: delay"}

print()
print("""
void setup() {                
    pinMode(1, OUTPUT);
}

void loop() {
    digitalWrite(1, HIGH);delay(5000);digitalWrite(1, LOW);delay(3000);     // Start: on(5s) off(3s)""")
for i in m:
  print(code[i])
print("""    delay(2000);
}""")
