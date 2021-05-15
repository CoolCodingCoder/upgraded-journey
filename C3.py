class C(object):
    a = 40.5
    
    def __init__(self):
        self.b = 2
        print(self)
        
    def i_fun(self):
        self.c = 12
    @classmethod
    def fun(cls):
         cls.a = 35.9
         d = cls.a * 100
         print(d)

    @staticmethod
    def s_func():
        print('static')



class O(object):
    nums = []
    def __init__(self, *args):
        self.nums.append(list(args))
    
    def prtNums(cls):
        Numbers = cls.nums
        print(Numbers)

c = O(1, 2, 3)
c.prtNums()