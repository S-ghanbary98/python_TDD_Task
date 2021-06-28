


class Cases:

    def divisible(self, num1, num2):
        if num1 % num2 == 0:
            return True
        else:
            return False

    def modulo(self, num1, num2):
        return num1 % num2

    def positive(self, num1, num2):
        if num1 > 0 and num2 >0:
            return True
        else:
            return False