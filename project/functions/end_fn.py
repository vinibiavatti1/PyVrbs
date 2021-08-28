from project.errors.vrbs_error import VrbsError
from project.functions.vrbs_function import VrbsFunction


class EndFn(VrbsFunction):

    def __init__(self, compiler):
        super().__init__(compiler, 'end', 0)

    def execute(self, params):
        self.compiler.set_cursor_at_last_callstack_point()
