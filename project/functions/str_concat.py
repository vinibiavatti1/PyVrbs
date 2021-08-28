from project.functions.vrbs_function import VrbsFunction


class StrConcatFn(VrbsFunction):

    def __init__(self, compiler):
        super().__init__(compiler, 'str_concat', 3)

    def execute(self, params):
        str1 = str(params[0])
        str2 = str(params[1])
        var = params[2]
        self.compiler.add_var(var, str1 + str2)
