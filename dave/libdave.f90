module libdave
  use, intrinsic :: iso_c_binding

implicit none

contains

subroutine dave_multiply(x,y,z) BIND(C, NAME='dave_multiply')
  real(c_float), intent(in)  :: x,y
  real(c_float), intent(out) :: z

  z = x*y

end subroutine

end module libdave
