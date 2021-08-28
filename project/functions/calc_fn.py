from project.errors.vrbs_error import VrbsError
from project.functions.vrbs_function import VrbsFunction


class CalcFn(VrbsFunction):

    def __init__(self, compiler):
        super().__init__(compiler, 'calc', 4)

    def execute(self, params):
        x = self.parse_number_or_error(params[0])
        y = self.parse_number_or_error(params[2])
        var = params[3]
        operator = params[1]
        result = None
        if operator == '+':
            result = x + y
        elif operator == '-':
            result = x - y
        elif operator == '*':
            result = x * y
        elif operator == '/':
            result = x / y
        elif operator == '//':
            result = x // y
        elif operator == '%':
            result = x % y
        elif operator == '**':
            result = x ** y
        else:
            message = f'Invalid operator "{operator}" at line ' + \
                f'{self.compiler.get_line()}'
            raise VrbsError(message)
        self.compiler.add_var(var, result)
