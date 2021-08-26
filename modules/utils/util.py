import os


def example():
    print(os.path.abspath("../data"))
    print("example 2")
    print("example 3")
    print("example 4")
    print(os.path.dirname(os.path.realpath(__file__)))
