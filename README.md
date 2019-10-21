## Git Basics
## Unix Shell
## Git Collaboration
## Python Basics 1
### Profile link:
[a link](https://www.hackerrank.com/savichevdenis244?hr_r=1)
## Memory Management
Questions:
1) What's going to happen if program reaches maximum limit of stack ?
- When the maximum stack size has been reached, we have a stack overflow and the program receives a Segmentation Fault.
2) What's going to happen if program requests a big (more then 128KB) memory allocation on heap ?
- In Linux, if you request a large block of memory via malloc(), the C library will create such an anonymous mapping instead of using heap memory. 'Large' means larger than MMAP_THRESHOLD bytes, 128 kB by default and adjustable via mallopt().
3) What's the difference between Text and Data memory segments ?
- Text memory segment is read only and stores data as a string literals. Data memory is read and write and saving the contents for static variables initialized in source code.
```shell 56094baf5000-56094baf7000 r--p 00000000 fd:00 393551                     /usr/bin/cat
56094baf7000-56094bafc000 r-xp 00002000 fd:00 393551                     /usr/bin/cat
56094bafc000-56094baff000 r--p 00007000 fd:00 393551                     /usr/bin/cat
56094baff000-56094bb00000 r--p 00009000 fd:00 393551                     /usr/bin/cat
56094bb00000-56094bb01000 rw-p 0000a000 fd:00 393551                     /usr/bin/cat
56094c801000-56094c822000 rw-p 00000000 00:00 0                          [heap]
7fa5399f8000-7fa539a1a000 rw-p 00000000 00:00 0 
7fa539a1a000-7fa5469c4000 r--p 00000000 fd:00 395627                     /usr/lib/locale/locale-archive
7fa5469c4000-7fa5469e6000 r--p 00000000 fd:00 397654                     /usr/lib64/libc-2.29.so
7fa5469e6000-7fa546b33000 r-xp 00022000 fd:00 397654                     /usr/lib64/libc-2.29.so
7fa546b33000-7fa546b7f000 r--p 0016f000 fd:00 397654                     /usr/lib64/libc-2.29.so
7fa546b7f000-7fa546b80000 ---p 001bb000 fd:00 397654                     /usr/lib64/libc-2.29.so
7fa546b80000-7fa546b84000 r--p 001bb000 fd:00 397654                     /usr/lib64/libc-2.29.so
7fa546b84000-7fa546b86000 rw-p 001bf000 fd:00 397654                     /usr/lib64/libc-2.29.so
7fa546b86000-7fa546b8c000 rw-p 00000000 00:00 0 
7fa546ba7000-7fa546ba8000 r--p 00000000 fd:00 397151                     /usr/lib64/ld-2.29.so
7fa546ba8000-7fa546bc8000 r-xp 00001000 fd:00 397151                     /usr/lib64/ld-2.29.so
7fa546bc8000-7fa546bd0000 r--p 00021000 fd:00 397151                     /usr/lib64/ld-2.29.so
7fa546bd1000-7fa546bd2000 r--p 00029000 fd:00 397151                     /usr/lib64/ld-2.29.so
7fa546bd2000-7fa546bd3000 rw-p 0002a000 fd:00 397151                     /usr/lib64/ld-2.29.so
7fa546bd3000-7fa546bd4000 rw-p 00000000 00:00 0 
7ffd7b334000-7ffd7b355000 rw-p 00000000 00:00 0                          [stack]
7ffd7b361000-7ffd7b364000 r--p 00000000 00:00 0                          [vvar]
7ffd7b364000-7ffd7b365000 r-xp 00000000 00:00 0                          [vdso]
ffffffffff600000-ffffffffff601000 r-xp 00000000 00:00 0                  [vsyscall]
```
```
Heap - 56094c801000-56094c822000,
Stack - 7ffd7b334000-7ffd7b355000,
```
#### The first article was difficult for me, but I figured out the basics of the anatomy of programs in memory. I find this material useful to everyone.
**Screenshots:**
<img src="task_unix_shell/image_2019-09-13_00-17-12.png" width=600 align=right>
<img src="task_unix_shell/image_2019-09-13_00-19-45.png" width=600 align=right>
<img src="task_unix_shell/image_2019-09-13_00-19-45.png" width=600 align=right>
<img src="task_unix_shell/image_2019-09-13_23-27-46.png" width=600 align=right>
<img src="task_git_collaboration/image_2019-09-19_23-54-41.png" width=600 align=right>
<img src="task_git_collaboration/image_2019-09-19_23-47-38.png" width=600 align=right>
<img src="python_basics_1/photo_2019-10-18_00-34-41.jpg" width=600 align=right>