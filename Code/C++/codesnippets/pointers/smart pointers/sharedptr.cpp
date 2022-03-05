#include <memory>
using namespace std;
   // SHARED POINTER
   // shared_ptr<int[]> int_array_two(new int[input]);
   // shared_ptr<int[]> int_array_three(new int[input]);
   // shared_ptr<int[]> int_array_four(new int[input]);
   shared_ptr<int>ShPtr = make_shared<int>();

    // reference counter for int_array

    cout << "Number of references: " << int_array_two.use_count() << endl;
    cout << "Number of references: " << ShPtr.use_count() << endl;

    /// access the array 
    (int_array_extra.get())[1] = 
    int_array_extra[1] = 3;
