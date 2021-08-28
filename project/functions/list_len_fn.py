from project.functions.vrbs_function import VrbsFunction


class ListLenFn(VrbsFunction):

    def __init__(self, compiler):
        super().__init__(compiler, 'list_len', 2)

    def execute(self, params):
        list_name = params[0]
        var = params[1]
        lst = self.compiler.get_list(list_name)
        self.compiler.add_var(var, len(lst))
