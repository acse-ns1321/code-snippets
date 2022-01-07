#include <stdio.h>
#include <stdlib.h>
int main( ) {

   int n, i;
   int *vals;

   printf( "Enter a number of squares :");
   // Now you know we pass the address of n into scanf
   scanf("%d", &n);

   printf( "\nYou entered: %d\n ", n);

   /* we have to _cast_ the void pointer from malloc
      to the relevant type. */

   vals = (int*) malloc(n * sizeof(int)) ;

   for (i=0; i<n; i++) {
       vals[i] = (i+1)*(i+1);
   }

   // We'll just print the values for now

   for (i=0; i<n; i++) {
       printf("%d\n", vals[i]);
   }

   // clean up
   free(vals);

   return 0;
}