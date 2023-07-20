"""

notes:
- ensure that no variable can have the same name as a constant and vice versa
- ensure that constants cannot be changed

"""

import sys

keywords = ["program", "function", "var", "const", "class", "if", "try", "catch", "else", "override", "import", "print"]
variables = {}
constants = {}


def parse(line, initline=None):
   if len(line) == 0:
      return None
   if line[0] in keywords:
      #print("Opening keyword: " + line[0])
      pass
   
   if len(line) == 0:
      pass
   
   match line[0]:
      ### Variable definitions ###
      case 'var':
         #print("Variable: " + line[1])
         match line[2]:
            case '=':
               #print("Operator: " + line[2])
               if line[3][0] == "\"" or line[3][0] == "'":
                  varstring = initline.split(line[3][0])
                  variables[line[1]] = varstring[1]
      case 'const':
         #print("Constant: " + line[1])
         match line[2]:
            case '=':
               #print("Operator: " + line[2])
               if line[3][0] == "\"" or line[3][0] == "'":
                  conststring = initline.split(line[3][0])
                  constants[line[1]] = conststring[1]
      ### Actions ###
      case 'print':
         if line[1][0] == "\"" or line[1][0] == "'":
            printstring = line[1].split(line[1][0])
            print(printstring[1])
         else:
            if line[1] in variables.keys():
               print(variables[line[1]])
            elif line[1] in constants.keys():
               print(constants[line[1]])
            else:
               print("Error: No variable named " + line[1])
      case 'quit':
         sys.exit()
      case '//':
         pass
      case _:
         if line[0] in variables.keys():
            print(variables[line[0]])
         elif line[0] in constants.keys():
            print(constants[line[0]])

while True:
   initline = input("> ")
   line = initline.split()
   if line[0] == "import":
      with open(line[1]) as program:
         for line in program:
            parse(line.split(), line)
   parse(line, initline)

print("All variables:\n")
print(variables)
print("\nAll constants:\n")
print(constants)
