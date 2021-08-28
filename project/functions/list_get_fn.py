from project.functions.vrbs_function import VrbsFunction


class ListGetFn(VrbsFunction):

    def __init__(self, compiler):
        super().__init__(compiler, 'list_get', 3)

    def execute(self, params):
        list_name = params[0]
        index = self.parse_number_or_error(params[1])
        var = params[2]
        lst = self.compiler.get_list(list_name)
        self.compiler.add_var(var, lst[int(index)])
