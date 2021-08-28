from abc import ABC, abstractmethod
from project.errors.vrbs_error import VrbsError


class VrbsFunction(ABC):

    ###########################################################################
    # Init
    ###########################################################################

    def __init__(self, compiler, name, param_count):
        self.compiler = compiler
        self.name = name
        self.param_count = param_count

    ###########################################################################
    # Public methods
    ###########################################################################

    def parse_number_or_error(self, value):
        try:
            return float(value)
        except Exception:
            line = self.compiler.get_line()
            message = f'Expected numeric value but received: "{value}" ' + \
                f'at line {line}'
            raise VrbsError(message)

    def evaluate_condition(self, x, operator, y):
        if operator == '==':
            return x == y
        elif operator == '!=':
            return x != y
        elif operator == '>':
            x = self.parse_number_or_error(x)
            y = self.parse_number_or_error(y)
            return x > y
        elif operator == '>=':
            x = self.parse_number_or_error(x)
            y = self.parse_number_or_error(y)
            return x >= y
        elif operator == '<':
            x = self.parse_number_or_error(x)
            y = self.parse_number_or_error(y)
            return x < y
        elif operator == '<=':
            x = self.parse_number_or_error(x)
            y = self.parse_number_or_error(y)
            return x <= y
        else:
            message = f'Invalid operator "{operator}" at line ' + \
                f'{self.compiler.get_line()}'
            raise VrbsError(message)

    ###########################################################################
    # Abstract methods
    ###########################################################################

    @abstractmethod
    def execute(self, params):
        pass

    ###########################################################################
    # Get and Set
    ###########################################################################

    def get_name(self):
        return self.name

    def get_param_count(self):
        return self.param_count
