#!/usr/bin/python3
for num in range(0, 90):
        if num % 10 > num / 10:
                if num != 89:
                        print("{:02d}, ".format(num), end='')
                else:
                        print("{:02d}".format(num))
