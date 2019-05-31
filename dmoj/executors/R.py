import os

from .r_executor import RExecutor


class Executor(RExecutor):
    name = 'R'
    command_paths = ['rscript']

    def get_nproc(self):
        return [-1, 1][os.name == 'nt']