import sys
from pathlib import Path

if __name__ == "__main__":

    if len(sys.argv) != 3:
        print("usage: python3 mydetect.py <file1> <file2>")
        exit(0)
    else:
        file1 = sys.argv[1]
        file2 = sys.argv[2]

    content1 = None
    content2 = None

    all_pass = True

    with open(file1) as f1:
        content1 = f1.read()

    with open(file2) as f2:
        content2 = f2.read()

    lines1 = content1.split("\n")
    lines2 = content2.split("\n")
    for line in lines1:
        if line == "":
            break
        _ = line.split("\t")
        keyword, index = _[0], _[1]
        line2 = None
        for line in lines2:
            if line.split("\t")[0] == keyword:
                line2 = line
                break
        if line2 is not None:
            index2 = line2.split("\t")[1]
            # test_result = set(index2.split(' ')) == set(index.split(' ')) and len(index2) == len(index)
            test_result = set(index2.rstrip().split(' ')) == set(index.rstrip().split(' '))  # I ignore the detection for the last space in each output line. You can use the above line for strict comparison.
            print(f"{keyword}: {test_result}")
            if test_result == False:
                all_pass = False
                indexes1 = set(index.rstrip().split(" "))
                indexes2 = set(index2.rstrip().split(" "))
                if (indexes1-indexes2) is not None:
                    print(f"In File 1 (not in File 2): \n{indexes1-indexes2}")
                if (indexes2-indexes1) is not None:
                    print(f"In File 2 (not in File 1): \n{indexes2-indexes1}")

    if all_pass == True:
        print("All passed!")
