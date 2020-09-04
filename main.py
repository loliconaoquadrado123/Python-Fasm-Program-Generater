import csv
import random
import time

Config={
    "MaxLength":999999999,
    "Size":100,
    "count":0
}


PropertiesOfMnemonics={
    "ids":{
        "mnemonic":0,
        "argsNumber":1,
        "id":2
    },
    "count":0    
    
    }
count=0

def readCvs(filename):
    with open('cvss/opcodes.csv',"r+") as csvfile:
        readCSV = csv.reader(csvfile, delimiter=',')
        csvFile=[]
        for i in readCSV:
            csvFile.append(i)
        return csvFile
CSV=readCvs("CVSOpcodes.csv")
def compile(data):
    
    mnemonics=[]
    for a in range(len(data)):
        mnemonic=data[a][0]
        
        CVSOpcode=CSV[mnemonic][0]
        
        args=data[a][1]
        argsLenght=CSV[mnemonic][1]
        
        if argsLenght=="1":
            mnemonics.append(CVSOpcode+" "+str(args[0]))
        if argsLenght=="2":
            mnemonics.append(CVSOpcode+" "+str(args[0])+","+str(args[1]))
            mnemonics.append(CVSOpcode)
            print(mnemonic)
        
    with open("asm/compiled.asm","w+") as out:
        header="format pe\n"
        out.write(header)
        for i in range(len(mnemonics)):
            out.write(mnemonics[i]+'\n')
            
       
#0=string 1=int=hex 2 


def main():
    lines=[]
    ArgsNumber=2
    for a in range(Config["Size"]):
        
        line=random.randint(0,len(CSV)-1)
        
        Args=[]
        
        for b in range(ArgsNumber):
            Args.append(random.randint(0,int(Config["MaxLength"])))
        lines.append([line,Args])
        
    compile(lines)
main()
