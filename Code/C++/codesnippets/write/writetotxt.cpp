
#include <iostream>
#include <fstream>
#include <string>
#include <vector>

using namespace std;

 int main(){ 

    vector<string> v = {"hi", "I", "am", "Niranjana"};

    // Create fstream variable named "file"
    std::fstream file;
    
    //  WRITE MODE
    file.open("newTextFile.txt", std::ios::out);

    // if file is open write all the vector text into it
    if(file.is_open()){
        for(int i=0;i<v.size();i++){
		    // file<<v[i]<<endl; // adding one word on every line
            file<<v[i]<< " "; // delimited by a space
    }
        
    // close file
    file.close();
    }

 }