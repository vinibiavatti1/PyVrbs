from project.functions.vrbs_function import VrbsFunction


class VarFn(VrbsFunction):

    def __init__(self, compiler):
        super().__init__(compiler, 'var', 2)

    def execute(self, params):
        self.compiler.add_var(params[0], params[1])
