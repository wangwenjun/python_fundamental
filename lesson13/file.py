class FileIoUtils:

    @staticmethod
    def read_and_print(file):
        f=open(file,"r",encoding="utf-8")
        try:
            lines=f.readlines()
            for l in lines:
                print(l)
        finally:
            f.close()

    @staticmethod
    def write(file,contents):
        f=open(file,"a")
        try:
            for l in contents:
                f.write(l+"\n")
            f.flush()
        finally:
            f.close()

    @staticmethod
    def read_with_file(file):
        try:
            with open(file,"r") as f:
                l=f.read()
                print(l)
        finally:
            f.close()

if __name__=="__main__":
    #FileIoUtils.write("f.txt",["1111111","2222222222"])
    #FileIoUtils.read_and_print("f.txt")
    FileIoUtils.read_with_file("f.txt")
