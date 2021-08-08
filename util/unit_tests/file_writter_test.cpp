// basic operations -- don't forget to save after trying to compile your code =)
#include <iostream>
#include <fstream>

using namespace std;

int main(){
    ofstream myfile("example2.txt");
    
    if (myfile.is_open()){
//        myfile.open("example2.txt");  // creates a file :: 
        myfile << "Writing this to a file. \n"; // write this string here!
        myfile.close();    //close file
    }else
    {
        cout << "Unable to open file" <<endl;
    }
    
    return 0;
}


//  ofstream -> stream class to write into files
//  ifstream -> read on files
//  fstream -> class to read/write

// obs: cin -> istream
//      cout -> ostream
// Missão: aprender a escrever texto estruturado no C++ 
//não precisa ser nada complexo, só preciso extrair os dados importantes 