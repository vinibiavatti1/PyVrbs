from project.functions.vrbs_function import VrbsFunction


class ObjSetFn(VrbsFunction):

    def __init__(self, compiler):
        super().__init__(compiler, 'obj_set', 3)

    def execute(self, params):
        obj_name = params[0]
        prop_name = params[1]
        prop_value = params[2]
        obj = self.compiler.get_obj(obj_name)
        obj[prop_name] = prop_value
