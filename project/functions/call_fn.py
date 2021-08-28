from project.errors.vrbs_error import VrbsError
from project.functions.vrbs_function import VrbsFunction


class CallFn(VrbsFunction):

    def __init__(self, compiler):
        super().__init__(compiler, 'call', 1)

    def execute(self, params):
        def_name = params[0]
        self.compiler.call_function(def_name)
