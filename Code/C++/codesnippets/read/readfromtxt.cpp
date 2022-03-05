// Headers

#include <iostream>
#include <fstream>
#include <string>
#include <vector>
// include header fstream


    
    // create fstream variable named "file"
    std::fstream file;

    
    //  WRITE MODE
    file.open("newTextFile.txt", std::ios::out); 
    // if file is open write some text into it
    if(file.is_open()){
        file<< " Hi! I'm Niranjana. This is my first file!\n";
        // close file
        file.close();
    }

    // APPEND MODE
    file.open("newTextFile.txt", std::ios::app); 
    // if file is open APPEND some text into it
    if(file.is_open()){
        file<< " Hi! I'm back\n";
        // close file
        file.close();
    }

    // READ MODE
    file.open("newTextFile.txt", std::ios::in); 
    // If file is open, read the text in the file and write it out
    if(file.is_open()){ 
        // Method: Read first line - store it in a variable - write it out : repeat using while loop
        // Note include the string library
        std::string line;
        while(getline(file, line)){// getline function takes file name and varible name as input
        std::cout<<line<<std::endl; // print out each line as it is read
        }
        // Close file
        file.close();
    }
}



