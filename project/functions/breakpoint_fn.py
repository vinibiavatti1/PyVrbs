from project.errors.vrbs_error import VrbsError
from project.functions.vrbs_function import VrbsFunction


class BreakpointFn(VrbsFunction):

    def __init__(self, compiler):
        super().__init__(compiler, 'breakpoint', 0)

    def execute(self, params):
        variables = self.compiler.get_variables()
        lists = self.compiler.get_lists()
        objs = self.compiler.get_objs()
        callstack = self.compiler.get_callstack()
        print('######## DEBUG ########')
        print('Variables', variables)
        print('Lists', lists)
        print('Objs', objs)
        print('Callstack', callstack)
        print('######## DEBUG ########')
        input('Type enter to continue...')
