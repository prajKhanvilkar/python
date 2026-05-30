import hashlib
def calculate_checksum(FileName):
    fobj = open(FileName, 'rb')
    hobj = hashlib.md5()
    Buffer = fobj.read(1000)
    while (len(Buffer) > 0):
        hobj.update(Buffer)
        Buffer = fobj.read(1000)

    fobj.close()
    return hobj.hexdigest()

def main():
    ret = calculate_checksum("Demo.txt")
    print("Checksum of the file is : " + ret)

if __name__ == "__main__":
    main()