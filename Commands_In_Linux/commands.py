# speaking with cmd using python
import os
os.system("echo hello terminal")
os.system("echo 1.ls lists files and directories")
y=os.popen("ls") #excite ls and store the output in as a string
y=y.read()
print(y)
os.system("echo 2.cd to navigate through linux files and directories")
x=os.popen("cd")
x=x.read()
print(x) 
os.system("echo 3.pwd to find the path of current working directory")
p=os.popen("pwd")
p=p.read()
print(p)
os.system("echo 4.cat to write file content to the standard output")
c=os.popen("cat test.py")
c=c.read()
print(c)
os.system("echo 5.tac display content in reverse order")
c=os.popen("tac test.py")
c=c.read()
print(c)
os.system("echo 6.cp to copy file or directories and their content")
c=os.popen("cp test.py copytest.py")
c=c.read()
print(c)
os.system("echo 7.mv to move and rename files and directories")
c=os.popen("mv copytest.py CopyTest.py")
c=c.read()
print(c)
os.system("echo 8.mkdir to create one or more directories")
c=os.popen("mkdir rana3")
c=c.read()
print(c)
os.system("echo 9.rmdir to delete an empty directories")
c=os.popen("rmdir rana3")
c=c.read()
print(c)
os.system("echo 10.rm to delete files within a directories")
c=os.popen("rm -f")
c=c.read()
print(c)
os.system("echo 11.touch to create an empty file")
c=os.popen("touch embedded")
c=c.read()
print(c)
os.system("echo 12.locate to find a file in the database system")
c=os.popen("locate")
c=c.read()
print(c)
os.system("echo 13.find to search for files in specific directory")
c=os.popen("find /home/rana/Rdirectory/file1")
c=c.read()
print(c)
os.system("echo 14.df to report the system's disk space usage")
c=os.popen("df -T")
c=c.read()
print(c)
os.system("echo 15.grep to find a word by searching through all the texts in a specific file")
c=os.popen("grep read CopyTest.py")
c=c.read()
print(c)
os.system("echo 16.du to check how much space afile or directory takes up")
c=os.popen("du /home/rana/Rdirectory")
c=c.read()
print(c)
os.system("echo 17.head to view the first ten lines of a file")
c=os.popen("head test.py")
c=c.read()
print(c)
os.system("echo 18.head -n to print first customized number of lines")
c=os.popen("head -n 3 test.py")
c=c.read()
print(c)
os.system("echo 19.tail to display the last ten lines of a file")
c=os.popen("tail -n 5 test.py")
c=c.read()
print(c)
os.system("echo 20.diff to compares two content of a file line by line then display the parts that do not match")
c=os.popen("diff rana rana2")
c=c.read()
print(c)
os.system("echo 21.chmod to modify a file or directory's read,write and execute permissions")
c=os.popen("chmod 777 rana")
c=c.read()
print(c)
os.system("echo 22.jobs to display all running process along with their statuses")
c=os.popen("jobs")
c=c.read()
print(c)






















