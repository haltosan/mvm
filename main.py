#from utils import makeMem
from utils import *
SD = False

TEMP_VARS = "11" #20
temp_vars = 11
EAX = "21" #return values
eax = 21
EBX = "22" #halt
ebx = 22
ECX = "23" #loop counter
ecx = 23
EDX = "24" #temp var/general purpose
edx = 24
ESI = "25" #goto pointer
esi = 25
EDI = "26" #pointer
edi = 26
EBP = "27" #literal loader
ebp = 27
ESP = "28" #stack pointer
esp = 28
EIP = "29" #instruction pointer
eip = 29
INT_VARS = "30" #50
int_vars = 30
PRINT_INT = "51"
print_int = 51
STRING_VARS = "52" #61
string_vars = 52
STRING_EBP = "62"
string_ebp = 62
PRINT_STRING = "63"
print_string = 63
FLOAT_VARS = "64" #73
float_vars = 64
PRINT_FLOAT = "74"
print_float = 74
PRINT_ACTIVATE = "75"
print_activate = 75
INC = "77"
inc = 77
DEC = "76"
dec = 76
CMP = "331" #585
cmp = 331
MAX = 625

############################

def m(loc):
  if(loc>=STRING_VARS):
    return(strings[loc-STRING_VARS])
  else:
    return(memory[loc])

def sd(*t): #show decode
  if(SD):
    print(t)

memory = [1,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,-1,0,1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20,21,22,23,24,25,26,27,28,29,30,31,32,33,34,35,36,37,38,39,40,41,42,43,44,45,46,47,48,49,50,51,52,53,54,55,56,57,58,59,60,61,62,63,64,65,66,67,68,69,70,71,72,73,74,75,76,77,78,79,80,81,82,83,84,85,86,87,88,89,90,91,92,93,94,95,96,97,98,99,100,101,102,103,104,105,106,107,108,109,110,111,112,113,114,115,116,117,118,119,120,121,122,123,124,125,126,127,128,129,130,131,132,133,134,135,136,137,138,139,140,141,142,143,144,145,146,147,148,149,150,151,152,153,154,155,156,157,158,159,160,161,162,163,164,165,166,167,168,169,170,171,172,173,174,175,176,177,178,179,180,181,182,183,184,185,186,187,188,189,190,191,192,193,194,195,196,197,198,199,200,201,202,203,204,205,206,207,208,209,210,211,212,213,214,215,216,217,218,219,220,221,222,223,224,225,226,227,228,229,230,231,232,233,234,235,236,237,238,239,240,241,242,243,244,245,246,247,248,249,250,251,252,253,254,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0]
strings = ['hello','world']
instruction = [0, 31, 0, 11, 0, 0, 15, 1, 0, 15, 0, 0, 0, 21, 0, 21, 0, 0, 0, 11, 0, 27, 0, 0, 0, 331, 636, 27, 0, 0, 1, 331, 626, 27, 0, 0, 0, 21, 0, 331, 636, 0, 0, 21, 0, 21, 0, 646, 0, 21, 0, 21, 0, 1, 0, 21, 0, 21, 0, 4, 0, 21, 0, 21, 0, 0, 0, 1, 0, 75, 626, 0, 0, 31, 0, 77, 656, 0, 0, 21, 0, 21, 0, -12, 0, 21, 0, 21, 0, 0, 0, 32, 0, 12, 0, 0, 16, 1, 0, 16, 0, 0, 0, 21, 0, 21, 0, 0, 0, 11, 0, 27, 0, 0, 0, 331, 636, 27, 0, 0, 1, 331, 626, 27, 0, 0, 0, 21, 0, 331, 636, 0, 0, 21, 0, 21, 0, 646, 0, 21, 0, 21, 0, 1, 0, 21, 0, 21, 0, 4, 0, 21, 0, 21, 0, 0, 0, 1, 0, 75, 626, 0, 0, 32, 0, 77, 657, 0, 0, 21, 0, 21, 0, -12, 0, 21, 0, 21, 0, 0, 0, 33, 0, 13, 0, 0, 17, 1, 0, 17, 0, 0, 0, 21, 0, 21, 0, 0, 0, 11, 0, 27, 0, 0, 0, 331, 636, 27, 0, 0, 1, 331, 626, 27, 0, 0, 0, 21, 0, 331, 636, 0, 0, 21, 0, 21, 0, 646, 0, 21, 0, 21, 0, 1, 0, 21, 0, 21, 0, 4, 0, 21, 0, 21, 0, 0, 0, 1, 0, 75, 626, 0, 0, 33, 0, 77, 658, 0, 0, 21, 0, 21, 0, -12, 0, 21, 0, 21, 0, 0, 0, 34, 0, 14, 0, 0, 18, 1, 0, 18, 0, 0, 0, 21, 0, 21, 0, 0, 0, 11, 0, 27, 0, 0, 0, 331, 636, 27, 0, 0, 1, 331, 626, 27, 0, 0, 0, 21, 0, 331, 636, 0, 0, 21, 0, 21, 0, 646, 0, 21, 0, 21, 0, 1, 0, 21, 0, 21, 0, 4, 0, 21, 0, 21, 0, 0, 0, 1, 0, 75, 626, 0, 0, 34, 0, 77, 659, 0, 0, 21, 0, 21, 0, -12, 0, 21, 0, 21, 0, 0, 0, 0, 0, 27, 0, 0]

memory[11] = 1
memory[12] = 2
memory[13] = 3
memory[14] = 4

memory[15] = 5
memory[16] = 6
memory[17] = 7
memory[18] = 8
runCount = 0
while(memory[0]==1): #flag indicating when to stop
  runCount += 1
  print(runCount)
  #debug(memory, instruction)
  
  prntBuf = ["f","null"]
  dupeInstruction = [0, 0,0, 0,0, 0] #lit, l1,o1 l2,o2, goto
  if(instruction[memory[eip]]<0):#indicating it's a string
    prntBuf[1] = strings[instruction[memory[eip]]+MAX]
    prntBuf[0] = "t"
  ## MUTATORS ##
  '''
  if(instruction[memory[eip]]>=MAX): #lit from memory
    dupeInstruction[0] = memory[instruction[memory[eip]]-MAX]
    print("lit ->",dupeInstruction[0])
  else:
      dupeInstruction[0] = instruction[memory[eip]]
  '''
  dupeInstruction[0] = instruction[memory[eip]]
  if(instruction[memory[eip]+1]>=MAX): #location 1 from memory
    dupeInstruction[1] = memory[instruction[memory[eip]+1]-MAX]
    sd("loc 1 ->",dupeInstruction[1])
  else:
      dupeInstruction[1] = instruction[memory[eip]+1]
  if(instruction[memory[eip]+2]>=MAX): #offset 1 from memory 
    dupeInstruction[2] = memory[instruction[memory[eip]+2]-MAX]
    sd("off 1 ->",dupeInstruction[2])
  else:
    dupeInstruction[2] = instruction[memory[eip]+2]
  if(instruction[memory[eip]+3]>=MAX): #location 2 from memory
    dupeInstruction[3] = memory[instruction[memory[eip]+3]-MAX]
    sd("loc 2 ->",dupeInstruction[3])
  else:
    dupeInstruction[3] = instruction[memory[eip]+3]
  if(instruction[memory[eip]+4]>=MAX): #offset 2 from memory
    dupeInstruction[4] = memory[instruction[memory[eip]+4]-MAX]
    sd("off 2 ->",dupeInstruction[4])
  else:
    dupeInstruction[4] = instruction[memory[eip]+4]
  if(instruction[memory[eip]+5]>MAX): #goto from memory
    dupeInstruction[5] = memory[instruction[memory[eip]+5]-MAX]
    sd("goto ->",dupeInstruction[5])
  else:
    dupeInstruction[5] = instruction[memory[eip]+5]
  
  ## EXECUTED INSTRUTIONS ##
  memory[ebp] = dupeInstruction[0] #load literal
  memory[ dupeInstruction[1]+dupeInstruction[2] ] = memory[ dupeInstruction[3]+dupeInstruction[4] ] #mov
  memory[eip] += (dupeInstruction[5]+1)*6 #goto
  '''
  if(memory[print_activate!=0]):#printing
    if(memory[print_activate==1]):#int
      print(memory[print_int])
    elif(memory[print_activate==2]):#string
      print(memory[print_string])
    memory[print_activate] = 0 #reset print flag
  '''
  #debug(memory,instruction)

printRegisters(memory)
print(memory)
