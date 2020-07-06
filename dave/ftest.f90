program test
use libdave, only: dave_multiply

implicit none

real :: x,y,z, answer

x = 3.
y = 6.
answer = x*y

call dave_multiply(x,y,z)

print*,z

if ( abs(z-answer) < 1.e-10) then
  print*,"PASSED"
else
  print*,"FAILED"
  print*,"Answer should be",answer
endif

end program test
