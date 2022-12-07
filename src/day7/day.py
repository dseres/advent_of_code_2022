import re

class File:
    def __init__(self, size, name):
        self.size : int = size
        self.name : str = name

class Dir:

    def __init__(self, name: str, parent = None):
        self.name : str = name
        self.files : [File] = []
        self.dirs : [Dir] = []
        self.size : int = 0
        self.parent : Dir = parent

    @classmethod
    def parse(cls, input: str):
        root = Dir('/')
        cd_pattern = re.compile('^\$ cd (/|\.\.|[\w|.]+)$')
        ls_pattern = re.compile('^\$ ls$')
        dir_pattern = re.compile('^dir ([\w|.]+)$')
        file_pattern = re.compile('^(\d+) ([\w|.]+)$')
        current_dir = root
        for line in input.splitlines():
            if len(line) > 0:
                match = cd_pattern.search(line)
                if match:
                    to_dir = match.groups()[0]
                    print('to_dir: ', to_dir)
                    if to_dir == '/':
                        current_dir = root
                    elif to_dir == '..':
                        current_dir = current_dir.parent
                    else:
                        current_dir = next(filter( (lambda d: d.name == to_dir), current_dir.dirs))
                    print('current_dir: ',vars(current_dir))
                else:
                    if ls_pattern.match(line):
                        pass
                    else:
                        match = dir_pattern.search(line)
                        if match:
                            dir_name = match.groups()[0]
                            print('found child dir: ',dir_name)
                            child_dir = Dir(dir_name, current_dir)
                            current_dir.dirs.append(child_dir)
                        else:
                            match = file_pattern.search(line)
                            if match:
                                [size,fname] = match.groups()
                                print('found file : ',size,fname)
                                current_dir.files.append(File(size, fname))
                            else:
                                assert(False)
        return root

    def solve1(self):
        return 

    def solve2(self):
        return 0


def read_input():
    file = open("input/input7.txt")
    return file.read()
