from test123 import a

a = 1


def test_outer():
    a = 2

    def test_inner():
        a = 3
        print(a)

    test_inner()


test_outer()
