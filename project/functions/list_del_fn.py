from project.functions.vrbs_function import VrbsFunction


class ListDelFn(VrbsFunction):

    def __init__(self, compiler):
        super().__init__(compiler, 'list_del', 2)

    def execute(self, params):
        list_name = params[0]
        index = params[1]
        lst = self.compiler.get_list(list_name)
        del lst[index]
