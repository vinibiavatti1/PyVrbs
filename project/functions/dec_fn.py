from project.errors.vrbs_error import VrbsError
from project.functions.vrbs_function import VrbsFunction


class DecFn(VrbsFunction):

    def __init__(self, compiler):
        super().__init__(compiler, 'dec', 2)

    def execute(self, params):
        x = self.parse_number_or_error(params[0])
        x -= 1
        var = params[1]
        self.compiler.add_var(var, x)
