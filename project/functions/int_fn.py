from project.functions.vrbs_function import VrbsFunction


class IntFn(VrbsFunction):

    def __init__(self, compiler):
        super().__init__(compiler, 'int', 2)

    def execute(self, params):
        val = self.parse_number_or_error(params[1])
        self.compiler.add_var(params[0], int(val))
