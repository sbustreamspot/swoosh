import sys

map = {'process': 'a',
       'thread': 'b',
       'file': 'c',
       'MAP_ANONYMOUS': 'd',
       'NA': 'e',
       'stdin': 'f',
       'stdout': 'g',
       'stderr': 'h',
       'accept': 'i',
       'access': 'j',
       'bind': 'k',
       'chmod': 'l',
       'clone': 'm',
       'close': 'n',
       'connect': 'o',
       'execve': 'p',
       'fstat': 'q',
       'ftruncate': 'r',
       'listen': 's',
       'mmap2': 't',
       'open': 'u',
       'read': 'v',
       'recv': 'w',
       'recvfrom': 'x',
       'recvmsg': 'y',
       'send': 'z',
       'sendmsg': 'A',
       'sendto': 'B',
       'stat': 'C',
       'truncate': 'D',
       'unlink': 'E',
       'waitpid': 'F',
       'write': 'G',
       'writev': 'H',
      }

if __name__ == "__main__":
    with open(sys.argv[1], 'r') as f:
        for line in f:
            fields = [w.strip() for w in line.split(',')]
            fields[0] = str(int(fields[0]) + 1)
            fields[1] = map[fields[1]]
            fields[2] = str(int(fields[2]) + 1)
            fields[3] = map[fields[3]]
            fields[4] = map[fields[4]]
            del fields[5] # no timestamp
            print '\t'.join(fields)
