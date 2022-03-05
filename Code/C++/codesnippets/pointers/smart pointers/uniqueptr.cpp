// Unique pointer
#include <memory>
// This syntax just looks ilke a constructor!
   // You feed it a pointer
   // Note there is special syntax here to tell the unique_ptr that 
   // it is pointing at an int array - this is so the unique_ptr knows
   // which version of delete to call

   // declaration
   unique_ptr<int[]> int_array(new int[input]);
   unique_ptr<int>unPtr1 = make_unique<int>(25);


   // moving ownership of unique pointers
   unique_ptr<int>unPtr2 = move(unPtr1);