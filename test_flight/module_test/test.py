
import sys

class FOO:
    def __init__(self):
        self.dag = sys._getframe().f_code.co_name
        print(self.dag)
        print(self.__module__)
        # print(self.__name__)

def func():
    print(sys._getframe().f_code.co_name)
    foo = FOO()
func()