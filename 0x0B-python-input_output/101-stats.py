#!/usr/bin/python3
""" Module to print status code """
import sys


class Magic:
    """ Class to generates instances with dict and size"""
    def __init__(self):
        """ Init method """
        self.dic = {}
        self.size = 0

    def init_dic(self):
        """ Initialize dict """
        self.dic['200'] = 0
        self.dic['301'] = 0
        self.dic['400'] = 0
        self.dic['401'] = 0
        self.dic['403'] = 0
        self.dic['404'] = 0
        self.dic['405'] = 0
        self.dic['500'] = 0

    def add_status_code(self, status):
        """ add repeated number to the status code """
        if status in self.dic:
            self.dic[status] += 1

    def print_info(self, sig=0, frame=0):
        """ print status code """
        print("File size: {:d}".format(self.size))
        for key in sorted(self.dic.keys()):
            if self.dic[key] is not 0:
                print("{}: {:d}".format(key, self.dic[key]))


if __name__ == "__main__":
    magic = Magic()
    magic.init_dic()
    nlines = 0

    try:
        for line in sys.stdin:
            if nlines % 10 == 0 and nlines is not 0:
                magic.print_info()

            try:
                list_line = [x for x in line.split(" ") if x.strip()]
                magic.add_status_code(list_line[-2])
                magic.size += int(list_line[-1].strip("\n"))
            except:
                pass
            nlines += 1
    except KeyboardInterrupt:
        magic.print_info()
        raise
    magic.print_info()
