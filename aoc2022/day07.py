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
        for line in input.splitlines():            
            if len(line) > 0:
                match line.split():
                    case ['$', 'cd', '/']:
                        current_dir = root
                    case ['$', 'cd', '..']:
                        current_dir = current_dir.parent
                    case ['$', 'cd', to_dir]:
                        current_dir = next(filter( (lambda d: d.name == to_dir), current_dir.dirs))
                    case ['dir', dir_name]:
                        current_dir.dirs.append(Dir(dir_name, current_dir))
                    case [size,fname] if size.isdigit():
                        current_dir.files.append(File(int(size), fname))
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
        for dir in self.dirs:
            (child_min, child_name) = dir.find_dir2(needed)
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
        (min,name) = self.find_dir2(needed)
        return min


def read_input(file):
    return file.read()

def solve1(input):
    root= Dir.parse(input)
    return root.solve1()

def solve2(input):
    root= Dir.parse(input)
    root.solve1()
    return root.solve2()