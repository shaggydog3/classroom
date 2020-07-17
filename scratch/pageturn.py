def pageCount(n, p):


def main():
    pageCount(2,6)

def initpagefunc(n):
    oddoreven = n % 2
    pagesfromend = (n - oddoreven, n + 1 - oddoreven)
    return pagesfromend

if __name__ == '__main__':
    main()