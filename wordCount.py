import sys

input = open(sys.argv[1], "r")
output = open(sys.argv[2], "w+")
dictionary = {}
if input.mode == "r":
    contents = input.read()
    list = contents.split(" ")
    for iword in list:
        iword = iword.lower()
        if "\n" in iword:
            list.append(iword[0:iword.index("\n")])
            list.append(iword[iword.index("\n")+1:len(iword)])
        elif "-" in iword:
            list.append(iword[0:iword.index("-")])
            list.append(iword[iword.index("-")+1:len(iword)])
        elif "'" in iword:
            list.append(iword[0:iword.index("'")])
            list.append(iword[iword.index("'") + 1:len(iword)])
        elif "," in iword:
            list.append(iword[0:iword.index(",")])
        elif "." in iword:
            list.append(iword[0:iword.index(".")])
        elif ";" in iword:
            list.append(iword[0:iword.index(";")])
        elif ":" in iword:
            list.append(iword[0:iword.index(":")])
        elif "" == iword:
            iword = iword.lower()
        else:
            if iword in dictionary.keys():
                dictionary[iword] = dictionary[iword]+1
            else:
                dictionary[iword] = 1
    for oword in sorted(dictionary.keys()):
        output.write("%s %d \n" % (oword, dictionary[oword]))
