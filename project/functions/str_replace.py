from project.functions.vrbs_function import VrbsFunction


class StrReplaceFn(VrbsFunction):

    def __init__(self, compiler):
        super().__init__(compiler, 'str_replace', 4)

    def execute(self, params):
        str1 = str(params[0])
        find = str(params[1])
        replace = str(params[2])
        var = params[3]
        new = str1.replace(find, replace)
        self.compiler.add_var(var, new)
