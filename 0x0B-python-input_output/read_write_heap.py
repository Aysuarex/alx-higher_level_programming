#!/usr/bin/python3
""" Module that finds a string in the heap of a running
process and replaces it
"""
import sys


def print_error():
    sys.stdout.write("Usage: read_write_heap.py pid search_string")
    sys.stdout.write(" replace_string\n")
    sys.exit(1)

if __name__ == "__main__":
    if len(sys.argv) is not 4:
        print_error()

    pid = int(sys.argv[1])

    s_string = sys.argv[2]
    if s_string == "":
        print_error()

    w_string = sys.argv[3]

    mps_fname = "/proc/{:d}/maps".format(pid)
    mem_fname = "/proc/{:d}/mem".format(pid)

    print("[*] maps: " + mps_fname)
    print("[*] mem: " + mem_fname)

    try:
        maps = open(mps_fname, 'r')
    except Exception as e:
        print("[ERROR] Can not open file " + mps_fname)
        print("        I/O error({}): {}".format(e.errno, e.strerror))
        sys.exit(1)

    for line in maps:
        list_format = line.split(" ")

        if list_format[-1][:-1] == "[heap]":
            print("[*] Found [heap]:")

            address = list_format[0]

            print("\tpathname = " + list_format[-1][:-1])
            print("\taddresses = " + address)
            print("\tpermissions = " + list_format[1])
            print("\toffset = " + list_format[2])
            print("\tinode = " + list_format[4])

            address = address.split("-")

            if len(address) is not 2:
                print("[*] Wrong addr format")
                maps.close()
                sys.exit(1)

            ad_start = int(address[0], 16)
            ad_end = int(address[1], 16)

            print("\tAddr start[{:x}] | end [{:x}]".format(ad_start, ad_end))

            try:
                mem = open(mem_fname, 'rb+')
            except Exception as e:
                print("[ERROR] Can not open file " + maps)
                print("        I/O error({}): {}".format(e.errno, e.strerror))
                maps.close()
                sys.exit(1)

            mem.seek(ad_start)
            heap = mem.read(ad_end - ad_start)

            try:
                i = heap.index(bytes(s_string, "ASCII"))
            except Exception:
                print("Can't find '" + s_string + "'")
                maps.close()
                mem.close()
                sys.exit(0)

            print("[*] Found '{}' at {:x}". format(s_string, i))

            print("[*] Writing '{}' at {:x}".format(w_string, i + ad_start))

            mem.seek(i + ad_start)
            mem.write(bytes(w_string + '\0', "ASCII"))

            maps.close()
            mem.close()

            break
