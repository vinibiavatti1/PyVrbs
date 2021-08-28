from project.functions.vrbs_function import VrbsFunction


class ParseIntFn(VrbsFunction):

    def __init__(self, compiler):
        super().__init__(compiler, 'parse_int', 2)

    def execute(self, params):
        x = self.parse_number_or_error(params[0])
        self.compiler.add_var(params[1], int(x))
