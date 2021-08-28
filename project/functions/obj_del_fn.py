from project.functions.vrbs_function import VrbsFunction
from project.errors.vrbs_error import VrbsError


class ObjDelFn(VrbsFunction):

    def __init__(self, compiler):
        super().__init__(compiler, 'obj_del', 2)

    def execute(self, params):
        obj_name = params[0]
        prop_name = params[1]
        obj = self.compiler.get_obj(obj_name)
        if prop_name not in obj:
            msg = f'Prop "{prop_name}" not defined on object "{obj_name}"'
            raise VrbsError(msg)
        del obj[prop_name]
