from project.errors.vrbs_error import VrbsError
from project.functions.vrbs_function import VrbsFunction


class IfFn(VrbsFunction):

    def __init__(self, compiler):
        super().__init__(compiler, 'if', 4)

    def execute(self, params):
        x = params[0]
        y = params[2]
        label = params[3]
        operator = params[1]
        result = self.evaluate_condition(x, operator, y)
        if result:
            self.compiler.set_cursor_at_label(label)
