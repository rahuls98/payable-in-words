#include <iostream>
#include <array>
#include <vector>
#include <string>

class PayableInWords {
private:
    std::array<std::string, 10> units = {"","one","two","three","four","five","six","seven","eight","nine"};
    std::array<std::string, 10> teens = {"ten","eleven","twelve","thirteen","fourteen","fifteen","sixteen","seventeen","eighteen","nineteen"};
    std::array<std::string, 10> tens  = {"","","twenty","thirty","fourty","fifty","sixty","seventy","eighty","ninety"};
    std::array<std::string, 4> suffixes = {""," thousand, "," lakh, "," crore, "};
    
    std::vector<std::string> amt = {};
    std::string res = "";

    void formatString(std::string inp) {
        std::string temp;
        for(int i=0; i<inp.size(); i++) {
            if(inp[i]!=',') {
                temp += inp[i];
            } else {
                this->amt.push_back(temp);
                temp = "";
            }
        } 
        this->amt.push_back(temp);
        this->amt = std::vector<std::string>(this->amt.rbegin(), this->amt.rend());
    
        for(auto i=(this->amt).begin(); i!=(this->amt).end(); i++) {
            if((*i).size()==1) {
                *i = "0"+(*i);
            }
        }
    }

    std::string twoDigit(std::string n) {
        if(n[0]=='0') {
            return this->units[(n[1]-48)];
        } else if(n[0]=='1') {
            return this->teens[(n[1]-48)];
        } else {
            if(n[1]=='0') {
                return this->tens[(n[0]-48)];
            }
            return this->tens[(n[0]-48)]+" "+this->units[(n[1]-48)];
        }
    }

    std::string threeDigit(std::string n) {
        if(n[0]=='0') {
            return this->twoDigit(n.substr(1));
        } else {
            if(n.substr(1) == "00") {
                return this->units[(n[0]-48)]+" hundred "+this->twoDigit(n.substr(1));
            } else {
                return this->units[(n[0]-48)]+" hundred and "+this->twoDigit(n.substr(1));
            }
        }
    }

    void num2words() {
        for(int i=0; i<(this->amt).size(); i++) {
            if(((this->amt)[i])=="00") continue;
            if(((this->amt)[i])=="000") {
                this->res = this->suffixes[0] + this->res;
                continue;
            }

            if( (i==1) && ((this->res).find("and")==std::string::npos) && ((this->amt)[0]!="000") ) {
                this->res = "and " + this->res;
            }

            if(((this->amt)[i]).size()==2) {
                this->res = this->twoDigit((this->amt)[i]) + this->suffixes[i] + this->res;
            } else {
                this->res = this->threeDigit((this->amt)[i]) + this->suffixes[i] + this->res;
            }
        }
    }

public:
    PayableInWords(std::string inp) {
        if(inp == "0") 
            this->res="zero";
        else {
            this->formatString(inp);
            this->num2words();
        }
    }

    std::string getString() {
        char& firstChar = (this->res).at(0);
        firstChar = (char)(firstChar-32);
        if((this->res).substr((this->res).size()-2)==", ") {
            return (this->res).substr( 0, (this->res).size()-2 )+" rupees only";
        }
        return (this->res)+" rupees only";
    }
};

int main() {
    std::cout<<PayableInWords("0").getString()<<std::endl;
    // Zero rupees only
    std::cout<<PayableInWords("8").getString()<<std::endl;
    // Eight rupees only
    std::cout<<PayableInWords("23").getString()<<std::endl;
    // Twenty three rupees only
    std::cout<<PayableInWords("105").getString()<<std::endl;
    // One hundred and five rupees only
    std::cout<<PayableInWords("5,000").getString()<<std::endl;
    // Five thousand rupees only
    std::cout<<PayableInWords("12,223").getString()<<std::endl;
    // Twelve thousand, two hundred and twenty three rupees only
    std::cout<<PayableInWords("1,00,105").getString()<<std::endl;
    // One lakh, one hundred and five rupees only
    std::cout<<PayableInWords("20,00,000").getString()<<std::endl;
    // Twenty lakh rupees only
    std::cout<<PayableInWords("5,00,50,005").getString()<<std::endl;
    // Five crore, fifty thousand, and five rupees only
    std::cout<<PayableInWords("99,99,99,999").getString()<<std::endl;
    // Ninety nine crore, ninety nine lakh, ninety nine thousand, nine hundred and ninety nine rupees only

    return 0;
}