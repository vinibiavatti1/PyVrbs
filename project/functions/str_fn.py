from project.functions.vrbs_function import VrbsFunction


class StrFn(VrbsFunction):

    def __init__(self, compiler):
        super().__init__(compiler, 'str', 2)

    def execute(self, params):
        self.compiler.add_var(params[0], str(params[1]))
