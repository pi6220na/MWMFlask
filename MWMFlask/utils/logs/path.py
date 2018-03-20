import os
directory = os.path.dirname(os.path.abspath(__file__))[-19:]

if __name__ == '__main__':
    print('os path ' + os.path.dirname(os.path.abspath(__file__)))
    print('directory ' + directory)