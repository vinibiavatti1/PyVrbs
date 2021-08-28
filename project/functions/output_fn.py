from project.functions.vrbs_function import VrbsFunction


class OutputFn(VrbsFunction):

    def __init__(self, compiler):
        super().__init__(compiler, 'output', 1)

    def execute(self, params):
        self.compiler.output(params[0])
