import os
from project.compiler.vrbs_compiler import VrbsCompiler
import sys


PROJECT_DIR = sys.path[0]
FILE_CODE = 'tic_tac_toe.vrbs'


# Main
def main():
    # Load file
    with open(PROJECT_DIR + '/codes/' + FILE_CODE) as code:
        compiler = VrbsCompiler()
        compiler.set_code(code.read())
        compiler.execute()


# Init
if __name__ == '__main__':
    main()
