from project.functions.vrbs_function import VrbsFunction


class ObjFn(VrbsFunction):

    def __init__(self, compiler):
        super().__init__(compiler, 'obj', 1)

    def execute(self, params):
        self.compiler.add_obj(params[0])
