
class ComputeProduct:
    def __init__(self, a, b):
        self.a = a
        self.b = b

    def compute(self, message):
        print(message)
        print(self.a * self.b)


if __name__ == '__main__':
    compute_obj = ComputeProduct(10, 12)
    compute_obj.compute("(utils.py) Inside if __name__ == __main__ statement:")

compute_obj = ComputeProduct(10, 4)
compute_obj.compute("(utils.py) Outside if __name__ == __main__ statement:")



