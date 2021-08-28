from project.functions.vrbs_function import VrbsFunction


class ListAddFn(VrbsFunction):

    def __init__(self, compiler):
        super().__init__(compiler, 'list_add', 2)

    def execute(self, params):
        list_name = params[0]
        val = params[1]
        lst = self.compiler.get_list(list_name)
        lst.append(val)
