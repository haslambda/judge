import os
import re

from .base_executor import ScriptExecutor

class RExecutor(ScriptExecutor):
    ext = '.r'
    name = 'R'
    address_grace = 65536
    test_program = NotImplementedError()

    def get_fs(self):
        fs = super(RExecutor, self).get_fs()
        home = self.runtime_dict.get('%s_home' % self.get_executor_name().lower())
        if home is not None:
            fs.append(re.escape(home))
            components = home.split('/')
            components.pop()
            while components and components[-1]:
                fs.append(re.escape('/'.join(components)) + '$')
                components.pop()
        return fs

    def get_cmdline(self):
        return [self.get_command(), '--vanilla', self._code]

    @classmethod
    def get_command(cls):
        name = cls.get_executor_name().lower()
        if name in cls.runtime_dict:
            return cls.runtime_dict[name]
        if '%s_home' % name in cls.runtime_dict:
            return os.path.join(cls.runtime_dict['%s_home'%name], 'bin', 'Rscript')

    @classmethod
    def get_find_first_mapping(cls):
        return {cls.name.lower(): cls.command_paths}

