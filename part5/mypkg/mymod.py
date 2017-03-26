def countLines(file_name):
    return len(open(file_name).readlines())

def countChars(file_name):
    return len(open(file_name).read())

def test(file_name):
    return countLines(file_name), countChars(file_name)

if __name__ == '__main__':
    import sys
    print(test(sys.argv[1]))
