from project.functions.vrbs_function import VrbsFunction


class InputFn(VrbsFunction):

    def __init__(self, compiler):
        super().__init__(compiler, 'input', 2)

    def execute(self, params):
        value = input(params[0])
        self.compiler.add_var(params[1], value)
