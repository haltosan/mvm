TEMP_VARS = "11" #20
EAX = "21" #return values
EBX = "22" #halt
ECX = "23" #loop counter
EDX = "24" #temp var/general purpose
ESI = "25" #goto pointer
EDI = "26" #pointer
EBP = "27" #literal loader
ESP = "28" #stack pointer
EIP = "29" #instruction pointer
INT_VARS = "30" #50
PRINT_INT = "51"
STRING_VARS = "52" #61
STRING_EBP = "62"
PRINT_STRING = "63"
FLOAT_VARS = "64" #73
PRINT_FLOAT = "74"
PRINT_ACTIVATE = "75"
INC = "77"
DEC = "76"
CMP = "331" #585
MAX = 600

############################

def m(loc):
  if(loc>=STRING_VARS):
    return(strings[loc-STRING_VARS])
  else:
    return(memory[loc])

memory = []
strings = []
instruction = []
strings = []

while(memory[0]):
  prntBuf = ["f","null"]
  if(instruction[EIP]<0):#indicating it's a string
    prntBuf[1] = strings[instruction[EIP]+MAX]
    prntBuf[0] = "t"
  if(instruction[EIP+5]>MAX):
    instruction[EIP+5] = m(instruction[EIP+5]-MAX)
  if(instruction[EIP+4]>MAX):
    instruction[EIP+4] = m(instruction[EIP+4]-MAX)
  if(instruction[EIP+3]>MAX):
    instruction[EIP+3] = m(instruction[EIP+3])
  
  m[EBP] = m[instruction[EIP]]
  m[ instruction[EIP+1]+instruction[EIP+2] ] = m[ instruction[EIP+3]+instruction[EIP+4] ]
  EIP += ( (instruction[EIP+5]+1) *5)

  if(memory[PRINT_ACTIVATE!=0]):
    if(memory[PRINT_ACTIVATE==1]):
      print(memory[PRINT_INT])
    elif(memory[PRINT_ACTIVATE==2]):
      print(memory[PRINT_STRING])
    memory[PRINT_ACTIVATE] = 0
