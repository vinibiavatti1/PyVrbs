from project.errors.vrbs_error import VrbsError
from project.functions.vrbs_function import VrbsFunction


class CaseFn(VrbsFunction):

    def __init__(self, compiler):
        super().__init__(compiler, 'case', 3)

    def execute(self, params):
        x = params[0]
        y = params[1]
        label = params[2]
        if x == y:
            self.compiler.set_cursor_at_label(label)
