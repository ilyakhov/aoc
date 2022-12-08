def solution7(p):
    from collections import defaultdict

    LIMIT_SIZE = 100000
    CD = "cd"
    LS = "ls"
    BACK = ".."
    ROOT = "/"
    ACTION_PREFIX = "$"
    DIR_PREFIX = "dir"

    def check_num(string):
        return max(string) <= "9" and min(string) >= "0"

    def parse_action(line):
        action = line.split(ACTION_PREFIX, 1)[1].strip()
        if action == LS:
            return LS
        elif action.startswith(CD):
            return (CD, action.split()[1])

    def do_ls(current_path, lines_iterator, tree):
        while True:
            try:
                line = next(lines_iterator)
                if line.startswith(ACTION_PREFIX):
                    return line, lines_iterator, tree
                else:
                    obj_type, name = line.split()
                    if check_num(obj_type):
                        tree[f"{'/'.join(current_path)}/{name}"] = int(obj_type)
                    else:
                        tree[f"{'/'.join(current_path)}/{name}"] = obj_type
            except StopIteration:
                return None

    def do_cd(current_path, to):
        if to == BACK:
            current_path.pop()
        else:
            current_path.append(to)

        return current_path

    def do_action(action, current_path, lines_iterator, tree):
        if action == LS:
            return do_ls(current_path, lines_iterator, tree)
        else:
            return do_cd(current_path, action[1])

    current_path = []
    tree = dict()
    skip_iteration = False

    with open(p) as inp:
        while True:
            if skip_iteration is False:
                try:
                    line = next(inp)
                except StopIteration:
                    break

            signal = line

            if signal.startswith(ACTION_PREFIX):
                action = parse_action(signal)
                result = do_action(action, current_path, inp, tree)

            if isinstance(result, list):
                skip_iteration = False
            elif isinstance(result, tuple):
                line, inp, tree = result
                skip_iteration = True
            else:
                break

    dir_sizes = defaultdict(int)
    for k, v in sorted(tree.items(), key=lambda _: _[0]):
        if v == "dir":
            continue
        folder = k.rsplit("/", 1)[0]
        while folder != ROOT:
            dir_sizes[folder] += v
            folder = folder.rsplit("/", 1)[0]
        assert folder == ROOT
        dir_sizes[folder] += v

    total_sum = 0
    for f, s in dir_sizes.items():
        if s <= LIMIT_SIZE:
            total_sum += s

    return total_sum
