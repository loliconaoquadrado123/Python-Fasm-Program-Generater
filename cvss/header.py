class Indices:
        def __init__(self,params):
                self.MaxLengthOfNumbers=params[0],
                self.Lines:params[1]
    class Params:
        def __init__(self):
class Configuration:
    
    def __init__(self,Params,Indice):
        self.params=Params(Params)
        self.indices=Indices(Indice)
        
        config.params[.MaxLength]
        CVS=readCvs("cvss/opcodes.csv")
        self.mnemonics=[]     
        for i in CVS:
            mnemonics.append(CVS[i][0])   
def readCvs(filename):
    with open('cvss/opcodes.csv',"r+") as csvfile:
        readCSV = csv.reader(csvfile, delimiter=',')
        csvFile=[]
        for i in readCSV:
            csvFile.append(i)
        return csvFile
CSV=readCvs("CVSOpcodes.csv")
def compile(data):
    config=Configuration([999999999,10],)
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
    Write("asm/compiled.asm","w+")
def Write(filename,mode):
    with open(filename,mode) as out:
    header="format pe\n section '.text' code readable executable\n public start as '_start'\n"
    out.write(header)
    for i in range(len(mnemonics)):
        out.write(mnemonics[i]+'\n')
       
#0=string 1=int=hex 2 

