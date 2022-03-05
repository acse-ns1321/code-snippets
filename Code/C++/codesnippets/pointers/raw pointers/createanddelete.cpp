// ----------------------- Variable--------------------------------------

// Pointer initialized with NULL then request memory for the variable
int *p = NULL; 
p = new int;

// Combine declaration of pointer and their assignment
int *p = new int; 

// Delete
delete pvalue;    


// ------------------------- Arrays-----------------------------------
char* pvalue  = new char[20];       // Request memory for the variable
delete [] pvalue;

// ------------------------ Multidimensional array---------------

double** pvalue  =  new double [3][4]; 
delete [] pvalue;


// ----------------------- Objects ------------------------------

// allocate an array of four Box objects, 
// the Simple constructor would be called four times and 
// similarly while deleting these objects, destructor will 
// also be called same number of times.

class Box {
   public:
      Box() { 
         cout << "Constructor called!" <<endl; 
      }
      ~Box() { 
         cout << "Destructor called!" <<endl; 
      }
};
int main() {
   Box* myBoxArray = new Box[4];
   delete [] myBoxArray; // Delete array

   return 0;
}