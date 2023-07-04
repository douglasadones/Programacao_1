class C1:
    def __init__(self):
        self.p1 = 'P1 da primeira classe'
        self.p2 = 'P2 da primeira classe'
        self.p3 = 'P3 da primeira classe'

    def m1(self, valor):
        print(f"Valor do método m1 da classe superior: {valor}")

    def m2(self):
        print('m2')


class C2(C1):
    def __init__(self, p4):
        super().__init__()
        self.p4 = p4

    def m3(self, aqui):
        super().m1(aqui)
        print("m3")

    def m4(self):
        super().m2()
        print("m4")


test = C2("a")

print(test.p1)
print(test.p2)
print(test.p3)
print(test.p4)
test.m3("bla bla bla")
