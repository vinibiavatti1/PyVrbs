from project.functions.vrbs_function import VrbsFunction


class ListFn(VrbsFunction):

    def __init__(self, compiler):
        super().__init__(compiler, 'list', 1)

    def execute(self, params):
        self.compiler.add_list(params[0])
