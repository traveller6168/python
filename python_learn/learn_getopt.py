#!/usr/bin/python3

import sys
import getopt


if "__main__" == __name__:
    #opc,opm = "",""
    try:
        opts,args = getopt.getopt(sys.argv[1:],"ao:c:",["help","output="]);
        print("=========================opts===================")
        print(opts)
        print("=========================args====================")
        print(args)
        for opt,agr in opts:
            if opt in ("-h","--help"):
                sys.exit(1)
            elif opt in ("-t","--test"):
                print("for test option")
            elif opt in ("-o","--test"):
                print("for test option")
                opm = agr
            elif opt in ("-c","--test"):
                print("for test option")
                opc = agr
            else:
                print("%s  ==>  %s") %(opt,agr)
        print("opt = %s,opm = %s") %(opc,opm)
    except getopt.GetoptError:
        print("getopt error!")
        sys.exit(1)