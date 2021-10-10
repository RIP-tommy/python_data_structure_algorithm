class Test:
    def __init__(self, no = 0):
        self.no = no


def main():
    a = Test()
    b = Test()
    a.no = 10
    print(b.no)

main()
