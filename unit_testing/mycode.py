class unittest_sample():
    def hello_world(self):
        return 'hello world'

    def create_num_list(self, length):
        return [x for x in range(length)]

    def custom_func_x(self, x, const, power):
        return const * (x) ** power

    def custom_non_lin_num_list(self, length, const, power):
        return [self.custom_func_x(x, const, power) for x in range(length)]
        