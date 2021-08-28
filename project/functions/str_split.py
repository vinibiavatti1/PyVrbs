from project.functions.vrbs_function import VrbsFunction


class StrSplitFn(VrbsFunction):

    def __init__(self, compiler):
        super().__init__(compiler, 'str_split', 3)

    def execute(self, params):
        str1 = str(params[0])
        char = str(params[1])
        lst_name = params[2]
        lst = str1.split(char)
        self.compiler.add_list(lst_name)
        vrbs_list = self.compiler.get_list(lst_name)
        for slice in lst:
            vrbs_list.append(slice)
