def makeMem():
  memArray = []
  memArray.append(1)
  for i in range(1,75):
    memArray.append(0)
  for i in range(-1,255):
    memArray.append(i)
    
  for i in range(331,624):
    memArray.append(0)
  
  memoryString = "["
  for i in memArray:
    memoryString+=str(i)+","
  memoryString = memoryString[:-1]+"]"
  a = open("memory","w")
  a.write(memoryString)
  a.close()

def printRegisters(memory):
  print("eax",memory[21],end="\t")
  print("ebx",memory[22],end='\t')
  print("ecx",memory[23],end="\t")
  print("edx",memory[24])
  print("esi",memory[25],end="\t")
  print("edi",memory[26],end='\t')
  print("ebp",memory[27],end="\t")
  print("esp",memory[28])
  print("eip",memory[29])

def printFlags(memory):
  print("print activate",memory[75],end="\t")  
  print("halt",memory[0])

def printInstruction(instruction,eip):
  print("lit",instruction[eip],end='\t')
  print("goto",instruction[eip+5])
  print("loc 1",instruction[eip+1],end='\t')
  print("off 1",instruction[eip+2])
  print("loc 2",instruction[eip+3],end='\t')
  print("off 2",instruction[eip+4])

def printTempvars(memory):
  for i in range(11,21):
    print(memory[i],end=" ")

def printPermvars(memory):
  for i in range(30,51):
    print(memory[i],end=" ")

def printComputation(memory):
  for i in range(1,11):
    print(memory[i],end=" ")

def debug(memory, instruction):
  while(True):
    flag = input("[enter to step]")
    if(flag=="m"):
      print(memory)
    elif(flag=="r"):
      printRegisters(memory)
    elif(flag=="f"):
      printFlags(memory)
    elif(flag=="i"):
      printInstruction(instruction, memory[29])
    elif(flag=="t"):
      printTempvars(memory)
    elif(flag=="p"):
      printPermvars(memory)
    elif(flag=="c"):
      printComputation(memory)
    else:
      break
