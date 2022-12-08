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
                    #print('to_dir: ', to_dir)
                    if to_dir == '/':
                        current_dir = root
                    elif to_dir == '..':
                        current_dir = current_dir.parent
                    else:
                        current_dir = next(filter( (lambda d: d.name == to_dir), current_dir.dirs))
                    #print('current_dir: ',vars(current_dir))
                else:
                    if ls_pattern.match(line):
                        pass
                    else:
                        match = dir_pattern.search(line)
                        if match:
                            dir_name = match.groups()[0]
                            #print('found child dir: ',dir_name)
                            child_dir = Dir(dir_name, current_dir)
                            current_dir.dirs.append(child_dir)
                        else:
                            match = file_pattern.search(line)
                            if match:
                                [size,fname] = match.groups()
                                #print('found file : ', int(size),fname)
                                current_dir.files.append(File(int(size), fname))
                            else:
                                assert(False)
        return root

    def calculate_sizes(self):
        self.calculate_size_impl(self)

    def calculate_size_impl(self,current_dir):
        size = sum([ file.size for file in current_dir.files])
        size += sum( [ self.calculate_size_impl(child) for child in current_dir.dirs ])
        current_dir.size = size
        return size

    def sum1(self):
        sum = 0
        if self.size <= 100000:
            sum += self.size
        for dir in self.dirs:
            sum += dir.sum1()
        return sum

    def find_dir2(self, needed):
        min = None
        name = None
        if needed <= self.size:
            min = self.size
            name = self.name
        for child in self.dirs:
            (child_min, child_name) = child.find_dir2(needed)
            if min is None or child_min is not None and needed <= child_min < min:
                min = child_min
                name = child_name
        return (min,name)

    def solve1(self):
        self.calculate_sizes()
        return self.sum1()

    def solve2(self):
        total_disk_space = 70000000
        unused_disk_space_needed = 30000000
        needed = unused_disk_space_needed - (total_disk_space - self.size)
        print(self.size, needed)
        (min,name) = self.find_dir2(needed)
        # print(min,name)
        return name


def read_input():
    file = open("input/input7.txt")
    return file.read()
