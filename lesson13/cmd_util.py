import subprocess
import os
from sys import argv as args

class cmd_utils:
    """
        the sub process example for execute linux command, contains several function(not class and instance level)
        Note: static method
    """

    @staticmethod
    def __popen(cmd_and_arguments):
        """
        create the subprocess.Popen instance
        """
        handle=subprocess.Popen(cmd_and_arguments,stdout=subprocess.PIPE,stderr=subprocess.PIPE)
        return handle


    @staticmethod
    def __format_print(std):
        """
            format the std and print it.
        """
        temp=std.decode("utf-8")
        temp=temp.split("\n")
        for i in range(0,len(temp)-1):
            print(temp[i])


    @staticmethod
    def ls(path,args="-lrt"):
        """
            ls command, list the directory files or folder given.
        """
        #ls command
        cmd='ls'

        #create the Popen instance
        handle=cmd_utils.__popen([cmd,args,path])
        
        #get sub process pid
        pid=handle.pid

        print(f"The pid is:{pid}")

        #get the sub process execution result,contains stdout and stderr
        result=handle.communicate()

        if handle.returncode==0:
            cmd_utils.__format_print(result[0])
        else:
            cmd_utils.__format_print(result[1])

    @staticmethod
    def ping(addr,args="-c2"):
        """
           ping command, ping the dest addr
        """
        cmd='ping'
         
        #create the Popen instance
        handle=cmd_utils.__popen([cmd,args,addr])
        
        #get sub process pid
        pid=handle.pid

        print(f"The pid is:{pid}")

        #get the sub process execution result,contains stdout and stderr
        result=handle.communicate()

        if handle.returncode==0:
            cmd_utils.__format_print(result[0])
        else:
            cmd_utils.__format_print(result[1])
        
        
if __name__=="__main__":
    cmd_utils.ls("/home/wangwenjun")
    cmd_utils.ping("localhost")
