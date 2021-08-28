from project.functions.vrbs_function import VrbsFunction
from project.errors.vrbs_error import VrbsError


class ObjGetFn(VrbsFunction):

    def __init__(self, compiler):
        super().__init__(compiler, 'obj_get', 3)

    def execute(self, params):
        obj_name = params[0]
        prop_name = params[1]
        var = params[2]
        obj = self.compiler.get_obj(obj_name)
        if prop_name not in obj:
            msg = f'Prop "{prop_name}" not defined on object "{obj_name}"'
            raise VrbsError(msg)
        prop_value = obj.get(prop_name)
        self.compiler.add_var(var, prop_value)
