#Only Works on positonal arguments, Macro Processor Written By Sarthak Sharma
class MProcessor():

    def __init__(self):
        self.instructionList = []
        self.macroIndices = {}
        self.macroStartIndices = []
        self.macroEndIndices = []
        self.MOT = {}
        self.MNT = {}

    def writeProgram(self):
        startIndex = 0
        inst_split = []
        MNT_extIndex = 0
        lineNumber = 1
        while(1):
            line = input(f"\n Enter the line number {lineNumber} :")
            if line:
                self.instructionList.append(line)
                lineNumber+=1
            else:
                break
        print("\n\n### Given Program ###")
        for lines in self.instructionList:
            print(lines)

        for counter in range(0, len(self.instructionList)):
             if(self.instructionList[counter].find('MACRO') != -1):
                 self.macroStartIndices.append(counter)
                 splitstring = self.instructionList[counter].split() #Append All the start Indices to a list, so that we can keep track of all the macro starts
                 self.MNT[splitstring[0]] = {}
                 self.MNT[splitstring[0]][counter] = 0
             elif(self.instructionList[counter].find('MEND') != -1):
                     self.macroEndIndices.append(counter)
                     for key in self.MNT.keys():
                         self.MNT[key][self.macroStartIndices[startIndex]] = self.macroEndIndices[startIndex] #Assign Start and End Indices to all the macros found in our program
                         startIndex+=1

#Add Macro Names to The Macro Name Table and Operand Parameters to the OPTAB
        for index in self.macroStartIndices:
            inst_split = self.instructionList[index].split()
            self.MOT[inst_split[0]] = {}
            for item in inst_split[2:len(inst_split)]:
                arg = item.replace('&','')
                self.MOT[inst_split[0]][arg] = 0

        #Start Reading the actual CODE NOW AND PRINT OUT ALL THE DATA Structures :
        print("\n\n\t\t\t### MACRO NAME TABLE ( CONTAINS NAME, AND START AND END INDICES OF A MACRO)")
        for key, values in self.MNT.items():
            print(f"\n\t{key} --------------> {values}")
        print("\n\n\t\t\t### MACRO OPERAND TABLE (CONTAINS PARAMETERS)")
        for key, values in self.MOT.items():
            print(f"\n\t{key} --------------> {values}")

        print("\n\n\t\t Performing Macro Expansion Now...")
        print("\n\n\t\t || Expanded Source Code ||")    
        for instructions in self.instructionList[self.macroEndIndices[-1]:len(self.instructionList)]:
            inst_split = instructions.split()
            if(inst_split[0] in self.MNT.keys()):
                print("\n\n### Macro Calls Encountered ### ")
                for key,value in self.MNT.items():
                        for key,val in value.items():
                            for items in self.instructionList[key+1:val]:
                                print(items)
            else:
                print(instructions)
if(__name__  == "__main__"):
    print("\n\n\t\t\t ### Macro Processor ###")
    mProcessor = MProcessor()
    mProcessor.writeProgram()
