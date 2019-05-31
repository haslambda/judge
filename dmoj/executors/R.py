from .base_executor import ScriptExecutor


class Executor(ScriptExecutor):
    name = 'R'
    ext = '.r'
    command = 'Rscript'
    command_paths = ['rscript']
    test_program = """\
lines <- readLines("stdin")
for(line in lines){
    cat(line)
}
"""

    def get_cmdline(self):
        return [self.get_command(), '--vanilla --slave', self._code]