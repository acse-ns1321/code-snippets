#include <iostream>
#include <vector>
#include <fstream>
#include <vector>

using namespace std;

void main(){

    // Create fstream variable for raw data file and open the file
    fstream raw_data_file;
    raw_data_file.open(filepath, fstream::in);

    // String to store data and elements of each line respectively
    string line; 
    string elements;

    // Check if file open was successful
	if (raw_data_file.fail()){
        cerr << filepath << endl << "File failed to open..." << endl;
		system("pause");
	}
    
    // Declaration pointer to a container to store the data 
    vector<string> *vec_str;
    vector<int> *vec_int;
    vector<double> *vec_double;

    *vec.reserve(30);
    // vector<string> *vec(30); // Same as the two statements above


//---------Single line Delimited by comma-----------------------------------    
    // get each line from the file -- default delimiter(3rd parameter) is '/n'
    getline(raw_data_file, line); // if one line, it will be a long single line

    // Builds string stream to parse each line into elements
    istringstream line_stream(line);

    // Loop to enter data into the line 
    for(int i = 0; i < 30; i++){
        getline(line_stream, elements, ',');
        *vec_str.push_back(elements); // save as string
        *vec_int.push_back(stoi(elements)); // save as int
        *vec_double.push_back(stod(elements)); // save as double
    }

 //---------Multiple lines Delimited by comma-----------------------------------
    for(int i = 0; i < rows ; i ++){
        // get each line from the file 
        getline(raw_data_file, line); 
        // Builds string stream to parse each line into elements
        istringstream line_stream(line);
        // Loop to enter data into each line 
        for(int i = 0; i < 30; i++){
            getline(line_stream, elements, ',');
            *vec_str.push_back(elements); // save as string
            *vec_int.push_back(stoi(elements)); // save as int
            *vec_double.push_back(stod(elements)); // save as double
        }
    }
}