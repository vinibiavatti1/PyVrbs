from project.errors.vrbs_error import VrbsError
from project.functions.vrbs_function import VrbsFunction


class DefFn(VrbsFunction):

    def __init__(self, compiler):
        super().__init__(compiler, 'def', 1)

    def execute(self, params):
        self.compiler.set_cursor_at_next_end()
