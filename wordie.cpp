//g++ -o wordie wordie.cpp -lstdc++
#include <iostream>
#include <random>
// example random code: int random = 1+ (rand() % 100);
std::string typo(std::string input){
    std::string finish, toparse;
    char temp;
    int a, b, c, d, w;
    a=b=c=d=w=0;
    toparse=input;
    finish=toparse;
    while (c != toparse.length()){
        if (toparse[c] != ' '){
            w=c;
            while (w < toparse.length() && toparse[w] != ' ' && toparse[w] != ',' && toparse[w] != '.' && toparse[w] != '!' && toparse[w] != ';' && toparse[w] != ':'){
                // must check for condition for each character separately
                w=w+1;
            }
            a=c+1;
            b=a+1;
            d=w-2;
            for (int i = 0; i<d-a; ++i){
                if (d - a > 0) { // Ensure there's a range to shuffle
                    int random = a + (rand() % (d - a));
                    temp = toparse[b];
                    toparse[b] = toparse[random];
                    toparse[random] = temp;
                    b=b+1;
                }
            }
            c = w;
        }
        else {
            c=c+1;    
        }  
    }
    finish = toparse;
    return finish;
}
int main(){
    srand(static_cast<unsigned int>(time(0)));
    std::string output;
    std::string test;
    std::getline(std::cin, test);
    std::cout << "Original text is: " << test << std::endl;
    output = typo(test);
    std::cout << "Typo text is: " << output << std::endl;
    return 0;
}