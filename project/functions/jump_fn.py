from project.errors.vrbs_error import VrbsError
from project.functions.vrbs_function import VrbsFunction


class JumpFn(VrbsFunction):

    def __init__(self, compiler):
        super().__init__(compiler, 'jump', 3)

    def execute(self, params):
        x = params[0]
        y = params[2]
        operator = params[1]
        result = self.evaluate_condition(x, operator, y)
        if result:
            self.compiler.add_cursor()
