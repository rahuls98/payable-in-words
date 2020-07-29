class PayableInWords():
    __units = ['','one','two','three','four','five','six','seven','eight','nine'];
    __teens = ['ten','eleven','twelve','thirteen','fourteen','fifteen','sixteen','seventeen','eighteen','nineteen']
    __tens  = ['','','twenty','thirty','fourty','fifty','sixty','seventy','eighty','ninety']
    __suffixes = ['',' thousand, ',' lakh, ',' crore, ']
    
    __amt = ''
    __res = ''
    
    def __init__(self, inp):
        if( inp=="0" ):
            self.__res = "zero"
        else:
            self.__formatString(inp)
            self.__num2words()
            
    def __formatString(self, inp):
        self.__amt = inp.split(',')
        self.__amt.reverse()
        self.__amt = ['0'+x if len(x)==1 else x for x in self.__amt]
        if len(self.__amt[0])!=3:
            self.__amt[0] = '0' + self.__amt[0]
            
    def __twoDigit(self, n):
        if(n[0]=='0'):
            return ( self.__units[int(n[1])] )
        elif(n[0]=='1'):
            return ( self.__teens[int(n[1])] )
        else:
            if(n[1]=='0'):
                return ( self.__tens[int(n[0])] ) 
            return ( self.__tens[int(n[0])] + ' ' + self.__units[int(n[1])] )
        
    def __threeDigit(self, n):
        if(n[0]=='0'):
            return (self.__twoDigit(n[1:]))
        else:
            if n[1:]=="00":
                return ( self.__units[int(n[0])] +  ' hundred ' + self.__twoDigit(n[1:]))
            else:
                return ( self.__units[int(n[0])] +  ' hundred and ' + self.__twoDigit(n[1:]))
        
    def __num2words(self):
        for i in range(len(self.__amt)):
            if(self.__amt[i] == '00'): 
                continue
            if(self.__amt[i] == '000'):
                self.__res = self.__suffixes[0] + self.__res
                continue
            
            if i==1 and ('and ' not in self.__res) and self.__amt[0]!='000':
                self.__res = 'and ' + self.__res
                

            if( len(self.__amt[i]) == 2 ):
                self.__res = self.__twoDigit(self.__amt[i]) + self.__suffixes[i] + self.__res
            else:
                self.__res = self.__threeDigit(self.__amt[i]) + self.__suffixes[i] + self.__res
                
    def __str__(self):
        if self.__res[-2:]==', ':
            return self.__res[:-2].capitalize() + ' rupees only'
        return self.__res.capitalize() + ' rupees only'
    
    def getString(self):
        if self.__res[-2:]==', ':
            return self.__res[:-2].capitalize() + ' rupees only'
        return self.__res.capitalize() + ' rupees only'
        
def main():
    print(PayableInWords("0")) # Zero rupees only
    print(PayableInWords("8")) # Eight rupees only
    print(PayableInWords("23")) # Twenty three rupees only
    print(PayableInWords("105")) # One hundred and five rupees only
    print(PayableInWords("5,000")) # Five thousand rupees only
    print(PayableInWords("12,223")) # Twelve thousand, two hundred and twenty three rupees only
    print(PayableInWords("1,00,105")) # One lakh, one hundred and five rupees only
    print(PayableInWords("20,00,000")) # Twenty lakh rupees only
    print(PayableInWords("99,99,99,999")) # Ninety nine crore, ninety nine lakh, ninety nine thousand, nine hundred and ninety nine rupees only

    obj = PayableInWords("5,00,50,005") 
    words = obj.getString()
    print(words) # Five crore, fifty thousand, and five rupees only
    
main()
