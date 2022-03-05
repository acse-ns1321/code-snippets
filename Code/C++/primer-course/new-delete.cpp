// new takes a data type and works out the rest for itself. 
// To allocate an array we use a syntax of the form new int[10], which must then be deallocated with delete[].
#include <iostream>

int main( ) {

   int n;
   int *vals;

   std::cout << "Enter a number of squares :";
   // Now you know we pass the address of n into scanf
   std::cin >> n;

   std::cout << "\nYou entered:" << n <<"\n";

   /* using "new" to allocate an array */

   vals = new int[n] ;

   for (int i=0; i<n; i++) {
       vals[i] = (i+1)*(i+1);
   }

   // We'll just print the values for now

   for (int i=0; i<n; i++) {
       std::cout << vals[i] <<"\n";
   }

   /* using "delete" to deallocate/cleanup an array */

    delete[] vals;

   return 0;
}