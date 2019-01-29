import os


def diskUsage(path):
    """
    type path: str
    rtype: int
    """
    total = os.path.getsize(path)
    if os.path.isdir(path):
        for name in os.listdir(path):
            total += diskUsage(os.path.join(path, name))
    print("%8d %s" % (total, path))
    return total

if __name__ == "__main__":
    diskUsage('../')
