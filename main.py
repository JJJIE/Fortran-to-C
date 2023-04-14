import re


def fortran_to_c(fortran_code):
    # 替换注释
    fortran_code = re.sub(r'!.*', r'//\g<0>', fortran_code)

    # 替换变量声明
    fortran_code = re.sub(r'(integer|real|double precision)\s*,\s*::\s*([\w\s,]*)', r'int \g<2>;', fortran_code)
    fortran_code = re.sub(r'(real|double precision)\s*::\s*([\w\s,]*)', r'float \g<2>;', fortran_code)

    # 替换do循环
    fortran_code = re.sub(r'do\s+(\w+)\s*=\s*(\d+),\s*(\d+),\s*(\d+)',
                          r'for(int \g<1>=\g<2>; \g<1> <= \g<3>; \g<1> += \g<4>)', fortran_code)
    fortran_code = re.sub(r'end\s*do', r'}', fortran_code)

    # 替换if语句
    fortran_code = re.sub(r'if\s*\((.*)\)\s*then', r'if(\g<1>) {', fortran_code)
    fortran_code = re.sub(r'else\s*if\s*\((.*)\)\s*then', r'} else if(\g<1>) {', fortran_code)
    fortran_code = re.sub(r'else', r'} else {', fortran_code)
    fortran_code = re.sub(r'end\s*if', r'}', fortran_code)

    # 替换end语句
    fortran_code = re.sub(r'end\s*([\w\s]*)', r'}', fortran_code)

    return fortran_code


fortran_code = """
! This is a simple Fortran code example
integer, parameter :: n = 10
real, dimension(n) :: a, b, c
integer :: i

! Adding two arrays element-wise
do i = 1, n
    c(i) = a(i) + b(i)
end do
"""

c_code = fortran_to_c(fortran_code)
print(c_code)
