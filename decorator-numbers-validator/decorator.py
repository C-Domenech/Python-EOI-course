import random


class Decorator:

    def __init__(self, function):
        self.function = function

    def __call__(self, *args):
        results = self.function(*args)
        for result in results:
            if result < 0:
                print('Uno o más números son negativos.')
                return
            elif type(result) != int:
                print('Uno o más números no son enteros.')
                return
        print('Todos los números son enteros y positivos.')
        return


@Decorator
def number_gen():
    my_randoms = random.sample([-5, 3.6, 6, 4, -9, 8.4, 9], 2)
    print(my_randoms)
    return my_randoms


def main():
    number_gen()


if __name__ == '__main__':
    main()
