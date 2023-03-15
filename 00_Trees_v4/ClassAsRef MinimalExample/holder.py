from integer_class import IntegerClass
import changer

def main():
    test = IntegerClass(5)
    print("Test before: ", test.integer)
    changer.change_integer(test)
    print("Test after: ", test.integer)

if __name__ == "__main__":
    main()