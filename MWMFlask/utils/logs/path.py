import os
directory = os.path.dirname(os.path.abspath(__file__))[-19:]

#print('in path.py, directory: %s ' % directory)

if __name__ == '__main__':
    print(directory)

