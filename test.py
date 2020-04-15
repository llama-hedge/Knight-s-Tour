class Test:
    def __init__(self):
        self.var = [5]

    def aaa(self):
        self.var = ["a"]

tester = Test()
box = []
box.append(tester.var)
print(box)
tester.aaa()
box.append(tester.var)
print(box)
print(tester.var)