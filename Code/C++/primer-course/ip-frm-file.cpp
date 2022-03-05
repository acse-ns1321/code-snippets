#include <fstream>

int main () {

  std::fstream fs;
  fs.open ("example.txt", std::fstream::out);
  
  fs << 1000;
  fs.close();

  return 0;
}