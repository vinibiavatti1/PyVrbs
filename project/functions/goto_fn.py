from project.errors.vrbs_error import VrbsError
from project.functions.vrbs_function import VrbsFunction


class GoToFn(VrbsFunction):

    def __init__(self, compiler):
        super().__init__(compiler, 'goto', 1)

    def execute(self, params):
        label = params[0]
        self.compiler.set_cursor_at_label(label)
