from project.functions.dec_fn import DecFn
from project.functions.inc_fn import IncFn
from project.functions.breakpoint_fn import BreakpointFn
from project.functions.call_fn import CallFn
from project.functions.def_fn import DefFn
from project.functions.end_fn import EndFn
from project.functions.label_fn import LabelFn
from project.functions.str_replace import StrReplaceFn
from project.functions.str_concat import StrConcatFn
from project.functions.str_split import StrSplitFn
from project.functions.obj_get_fn import ObjGetFn
from project.functions.obj_fn import ObjFn
from project.functions.obj_set_fn import ObjSetFn
from project.functions.obj_del_fn import ObjDelFn
from project.functions.parse_str_fn import ParseStrFn
from project.functions.output_fn import OutputFn
from project.functions.stay_fn import StayFn
from project.functions.str_fn import StrFn
from project.functions.float_fn import FloatFn
from project.functions.int_fn import IntFn
from project.functions.case_fn import CaseFn
from project.functions.jump_fn import JumpFn
from project.functions.input_fn import InputFn
from project.functions.list_fn import ListFn
from project.functions.list_add_fn import ListAddFn
from project.functions.list_del_fn import ListDelFn
from project.functions.list_len_fn import ListLenFn
from project.functions.list_get_fn import ListGetFn
from project.functions.parse_float_fn import ParseFloatFn
from project.functions.parse_int_fn import ParseIntFn
from project.functions.goto_fn import GoToFn
from project.functions.if_else_fn import IfElseFn
from project.functions.if_fn import IfFn
from project.functions.outputln_fn import OutputLnFn
from project.functions.output_fn import OutputFn
from project.functions.calc_fn import CalcFn
from project.functions.var_fn import VarFn
from project.compiler.vrbs_state import VrbsState
from project.errors.vrbs_error import VrbsError
import re


class VrbsCompiler:

    ###########################################################################
    # Class variables
    ###########################################################################

    FUNCTION_REGEX = r'[a-zA-Z\_]+\([^\)\(]*\)'
    FUNCTION_NAME_BEGIN_REGEX = r'[a-zA-Z\_]+\('
    FUNCTION_NAME_END_REGEX = r'\)'
    FUNCTION_PARAMETERS_REGEX = r'\([^\)\(]*\)'
    LABEL_FUNCTION_NAME = 'label'
    EXIT_FUNCTION_NAME = 'exit'
    VAR_IDENTIFIER = '$'
    END_IDENTIFIER = 'end'
    DEF_IDENTIFIER = 'def'

    ###########################################################################
    # Init
    ###########################################################################

    def __init__(self):
        self._code = ''
        self._cursor = 0
        self._functions = []
        self._lines = []
        self._state = VrbsState.WAITING
        self._register_native_functions()
        self._linesep = '\n'
        self._callstack = []
        self._variables = dict()
        self._lists = dict()
        self._objs = dict()

    ###########################################################################
    # Public methods
    ###########################################################################

    def set_code(self, code):
        self.reset()
        self._state = VrbsState.WAITING
        self._code = code
        self._lines = code.split(self._linesep)

    def execute(self):
        self._state = VrbsState.RUNNING
        while self._cursor < len(self._lines):
            line = self._lines[self._cursor]
            function = self._compile(line)
            if function is not None:
                fn_name = self._get_function_name(function)
                fn_parameters = self._get_function_parameters(function)
                if fn_name == VrbsCompiler.EXIT_FUNCTION_NAME:
                    break
                try:
                    self._execute_function(fn_name, fn_parameters)
                except Exception as err:
                    self.output(err)
                    self._state = VrbsState.ERROR
                    return
            self.add_cursor()
        self._state = VrbsState.FINISHED
        return

    def register_function(self, function):
        self._functions.append(function)

    def reset(self):
        self._cursor = 0
        self._callstack = []
        self._variables = dict()
        self._lists = dict()
        self._objs = dict()

    ###########################################################################
    # Override methods
    ###########################################################################

    def output(self, value):
        print(str(value), end='')

    ###########################################################################
    # Context manager
    ###########################################################################

    def set_cursor_at_last_callstack_point(self):
        last = self._callstack.pop()
        if last:
            self.set_cursor(last)

    def call_function(self, def_name):
        for index, line in enumerate(self._lines):
            function = self._compile(line)
            if function is not None:
                fn_name = self._get_function_name(function)
                fn_parameters = self._get_function_parameters(function)
                if fn_name == VrbsCompiler.DEF_IDENTIFIER:
                    if (len(fn_parameters) > 0 and
                            fn_parameters[0] == def_name):
                        self._callstack.append(self._cursor)
                        self.set_cursor(index)
                        return
        raise VrbsError(f'Function "{def_name}" not found')

    def set_cursor_at_next_end(self):
        while self._cursor < len(self._lines):
            line = self._lines[self._cursor]
            function = self._compile(line)
            if function is not None:
                fn_name = self._get_function_name(function)
                if fn_name == VrbsCompiler.END_IDENTIFIER:
                    return
            self.add_cursor()
        raise VrbsError('Function defined without end()')

    def set_cursor_at_label(self, label_name):
        for index, line in enumerate(self._lines):
            function = self._compile(line)
            if function is not None:
                fn_name = self._get_function_name(function)
                fn_parameters = self._get_function_parameters(function)
                if fn_name == VrbsCompiler.LABEL_FUNCTION_NAME:
                    if (len(fn_parameters) > 0 and
                            fn_parameters[0] == label_name):
                        self.set_cursor(index)
                        return
        raise VrbsError(f'Label "{label_name}" not found')

    def add_var(self, name, value):
        name = VrbsCompiler.VAR_IDENTIFIER + str(name)
        self._variables[name] = value

    def add_list(self, name):
        self._lists[name] = list()

    def add_obj(self, name):
        self._objs[name] = dict()

    def get_obj(self, name):
        obj = self._objs.get(name)
        if obj is None:
            raise VrbsError(f'Object "{name}" not defined')
        return obj

    def get_list(self, name):
        lst = self._lists.get(name)
        if lst is None:
            raise VrbsError(f'List "{name}" not defined')
        return lst

    def get_var(self, name):
        return self._variables.get(name, 'None')

    ###########################################################################
    # Private methods
    ###########################################################################

    def _compile(self, line):
        functions = re.findall(VrbsCompiler.FUNCTION_REGEX, line)
        if len(functions) > 0:
            return functions[0]
        return None

    def _get_function_name(self, function):
        return re.sub(VrbsCompiler.FUNCTION_PARAMETERS_REGEX, '', function)

    def _get_function_parameters(self, function):
        parameters = re.findall(
            VrbsCompiler.FUNCTION_PARAMETERS_REGEX,
            function
        )
        return str(parameters[0]) \
            .replace('(', '') \
            .replace(')', '') \
            .split(',')

    def _execute_function(self, fn_name, fn_parameters):
        for fn in self._functions:
            if fn.get_name() == fn_name:
                expected_param_count = fn.get_param_count()
                actual_param_count = len(fn_parameters)
                if expected_param_count > actual_param_count:
                    message = f'The function "{fn_name}" expects ' + \
                        f'{expected_param_count} parameters, but found ' + \
                        f'{actual_param_count} at line {self.get_line()}'
                    raise VrbsError(message)
                fn.execute(self._process_params(fn_parameters))

    def _process_params(self, params):
        result = []
        for param in params:
            if param.startswith(VrbsCompiler.VAR_IDENTIFIER):
                result.append(self.get_var(param))
            else:
                result.append(param)
        return result

    def _register_native_functions(self):
        # Datatypes
        self._functions.append(VarFn(self))
        self._functions.append(FloatFn(self))
        self._functions.append(IntFn(self))
        self._functions.append(StrFn(self))

        # Collections
        self._functions.append(ListFn(self))
        self._functions.append(ListAddFn(self))
        self._functions.append(ListLenFn(self))
        self._functions.append(ListDelFn(self))
        self._functions.append(ListGetFn(self))
        self._functions.append(ObjFn(self))
        self._functions.append(ObjGetFn(self))
        self._functions.append(ObjSetFn(self))
        self._functions.append(ObjDelFn(self))

        # Cursor manager
        self._functions.append(CaseFn(self))
        self._functions.append(JumpFn(self))
        self._functions.append(StayFn(self))
        self._functions.append(IfFn(self))
        self._functions.append(IfElseFn(self))
        self._functions.append(GoToFn(self))
        self._functions.append(LabelFn(self))
        self._functions.append(EndFn(self))
        self._functions.append(DefFn(self))
        self._functions.append(CallFn(self))

        # Parsers
        self._functions.append(ParseIntFn(self))
        self._functions.append(ParseFloatFn(self))
        self._functions.append(ParseStrFn(self))

        # Math
        self._functions.append(CalcFn(self))
        self._functions.append(IncFn(self))
        self._functions.append(DecFn(self))

        # IO
        self._functions.append(InputFn(self))
        self._functions.append(OutputFn(self))
        self._functions.append(OutputLnFn(self))

        # Str
        self._functions.append(StrConcatFn(self))
        self._functions.append(StrSplitFn(self))
        self._functions.append(StrReplaceFn(self))

        # Debug
        self._functions.append(BreakpointFn(self))

    ###########################################################################
    # Get and Set
    ###########################################################################

    def get_cursor(self):
        return self._cursor

    def set_cursor(self, position):
        self._cursor = position

    def add_cursor(self):
        self._cursor += 1

    def get_line(self):
        return self._cursor + 1

    def get_output(self):
        return self._output

    def get_state(self):
        return self._state

    def set_linesep(self, linesep):
        self._linesep = linesep

    def get_variables(self):
        return self._variables

    def get_lists(self):
        return self._lists

    def get_objs(self):
        return self._objs

    def get_callstack(self):
        return self._callstack

    def set_output_fn(self, output_fn):
        self.output = output_fn
