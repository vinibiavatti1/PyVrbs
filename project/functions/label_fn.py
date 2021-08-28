from project.errors.vrbs_error import VrbsError
from project.functions.vrbs_function import VrbsFunction


class LabelFn(VrbsFunction):

    def __init__(self, compiler):
        super().__init__(compiler, 'label', 1)

    def execute(self, params):
        pass
