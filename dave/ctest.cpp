#include "libdave.h"
#include <iostream>
#include <cmath>

int main(){
  float x,y,z, answer;

  x = 3.;
  y = 6.;
  answer = x*y;

  dave_multiply(&x,&y,&z);

  std::cout << z << std::endl;

  if (std::abs(z-answer)<1.e-10)
  {
    std::cout << "PASSED" << std::endl;
  }
  else
  {
    std::cout << "FAILED" << std::endl;
    std::cout << "Answer should be " << answer << std::endl;
  }


  return 0;
}
