from project.errors.vrbs_error import VrbsError
from project.functions.vrbs_function import VrbsFunction


class IfElseFn(VrbsFunction):

    def __init__(self, compiler):
        super().__init__(compiler, 'if_else', 5)

    def execute(self, params):
        x = params[0]
        y = params[2]
        labelTrue = params[3]
        labelFalse = params[4]
        operator = params[1]
        result = self.evaluate_condition(x, operator, y)
        if result:
            self.compiler.set_cursor_at_label(labelTrue)
        else:
            self.compiler.set_cursor_at_label(labelFalse)
