import os

from .base_executor import ScriptExecutor


class Executor(ScriptExecutor):
    name = 'R'
    ext = '.r'
    command = 'Rscript'
    command_paths = ['rscript']
    test_program = """
f <- file("stdin")
open(f)
while(length(line <- readLines(f,n=1)) > 0) {
  write(line, stdout())
}
"""

    def get_cmdline(self):
        return [self.get_command(), '--vanilla', '--slave', self._code]