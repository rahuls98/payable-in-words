class PayableInWords():
    units = ['','one','two','three','four','five','six','seven','eight','nine'];
    teens = ['ten','eleven','twelve','thirteen','fourteen','fifteen','sixteen','seventeen','eighteen','nineteen']
    tens  = ['','','twenty','thirty','fourty','fifty','sixty','seventy','eighty','ninety']
    suffixes = ['',' thousand, ',' lakh, ',' crore, ']
    
    amt = ''
    res = ''
    
    def __init__(self, inp):
        if( inp=="0" ):
            self.res = "zero"
        else:
            self.formatString(inp)
            self.num2words()
            
    def formatString(self, inp):
        self.amt = inp.split(',')
        self.amt.reverse()
        self.amt = ['0'+x if len(x)==1 else x for x in self.amt]
        if len(self.amt[0])!=3:
            self.amt[0] = '0' + self.amt[0]
            
    def twoDigit(self, n):
        if(n[0]=='0'):
            return ( self.units[int(n[1])] )
        elif(n[0]=='1'):
            return ( self.teens[int(n[1])] )
        else:
            if(n[1]=='0'):
                return ( self.tens[int(n[0])] ) 
            return ( self.tens[int(n[0])] + ' ' + self.units[int(n[1])] )
        
    def threeDigit(self, n):
        if(n[0]=='0'):
            return (self.twoDigit(n[1:]))
        else:
            if n[1:]=="00":
                return ( self.units[int(n[0])] +  ' hundred ' + self.twoDigit(n[1:]))
            else:
                return ( self.units[int(n[0])] +  ' hundred and ' + self.twoDigit(n[1:]))
        
    def num2words(self):
        for i in range(len(self.amt)):
            if(self.amt[i] == '00'): 
                continue
            if(self.amt[i] == '000'):
                self.res = self.suffixes[0] + self.res
                continue
            
            if i==1 and ('and ' not in self.res) and self.amt[0]!='000':
                self.res = 'and ' + self.res
                

            if( len(self.amt[i]) == 2 ):
                self.res = self.twoDigit(self.amt[i]) + self.suffixes[i] + self.res
            else:
                self.res = self.threeDigit(self.amt[i]) + self.suffixes[i] + self.res
                
    def __str__(self):
        if self.res[-2:]==', ':
            return self.res[:-2].capitalize() + ' rupees only'
        return self.res.capitalize() + ' rupees only'
    
    def getString(self):
        if self.res[-2:]==', ':
            return self.res[:-2].capitalize() + ' rupees only'
        return self.res.capitalize() + ' rupees only'
        
def main():
    print(PayableInWords("0")) # Zero rupees only
    print(PayableInWords("8")) # Eight rupees only
    print(PayableInWords("23")) # Twenty three rupees only
    print(PayableInWords("105")) # One hundred and five rupees only
    print(PayableInWords("5,000")) # Five thousand rupees only
    print(PayableInWords("12,223")) # Twelve thousand, two hundred and twenty three rupees only
    print(PayableInWords("1,00,105")) # One lakh, one hundred and five rupees only
    print(PayableInWords("20,00,000")) # Twenty lakh rupees only

    obj = PayableInWords("5,00,50,005") 
    words = obj.getString()
    print(words) # Five crore, fifty thousand, and five rupees only
    
main()