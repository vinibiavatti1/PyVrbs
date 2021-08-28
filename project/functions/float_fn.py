from project.functions.vrbs_function import VrbsFunction


class FloatFn(VrbsFunction):

    def __init__(self, compiler):
        super().__init__(compiler, 'float', 2)

    def execute(self, params):
        val = self.parse_number_or_error(params[1])
        self.compiler.add_var(params[0], val)
