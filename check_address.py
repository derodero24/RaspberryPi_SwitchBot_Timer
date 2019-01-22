import sys

from set_timer import push


def main():
    try:
        push(sys.argv[1])
        print('Success !!')
    except Exception as ex:
        print('Failed ...')


if __name__ == '__main__':
    main()
