from project.functions.vrbs_function import VrbsFunction
import os


class OutputLnFn(VrbsFunction):

    def __init__(self, compiler):
        super().__init__(compiler, 'output_ln', 1)

    def execute(self, params):
        self.compiler.output(str(params[0]) + os.linesep)
