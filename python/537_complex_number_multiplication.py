class Solution:
    def complexNumberMultiply(self, num1: str, num2: str) -> str:
        real1=int(num1.split("+")[0])
        real2=int(num2.split("+")[0])
        imag1=int(num1.split("+")[1][:-1])
        imag2=int(num2.split("+")[1][:-1])
        real=real1*real2-imag1*imag2
        imag=real1*imag2+real2*imag1
        return str(real)+"+"+str(imag)+"i"