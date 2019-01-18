#include <iostream>
#include <thread>

const int NUM_THREADS = 2;
const int NUM_ITER = 20;

int counter = 0;

void child()
{
   for (int i = 0; i < NUM_ITER; i++)
   {
      counter++;
   }
}

main()
{
       std::thread* t[NUM_THREADS];
       int x;

       for (int i=0; i<NUM_THREADS; i++) 
       {
          
          t[i] = new std::thread(child);
       }

       for (int i=0; i<NUM_THREADS; i++)
       {
          t[i]->join();
       }

       std::cout << "counter = " << counter << std::endl;
}
