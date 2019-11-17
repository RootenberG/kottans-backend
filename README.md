## Git Basics
## [Unix Shell](https://github.com/RootenberG/kottans-backend/tree/master/task_unix_shell)
## [Git Collaboration](https://github.com/RootenberG/kottans-backend/tree/master/task_git_collaboration)
## [Python Basics 1](https://github.com/RootenberG/kottans-backend/tree/master/python_basics_1)
## [TCP. UDP. Network](https://github.com/RootenberG/kottans-backend/tree/master/task_networks)
### Profile link:
[a link](https://www.hackerrank.com/savichevdenis244?hr_r=1)
## Memory Management:
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

## HTTP & HTTPS
```
    curl https://api.github.com/users/RootenberG
    curl -i https://api.github.com/users/RootenberG
    curl --user "RootenberG:blabla" https://api.github.com/gists/starred
    curl --user "RootenberG:*******" https://api.github.com/gists/starred
    curl --user "RootenberG" https://api.github.com/gists/starred
    curl -i https://api.github.com/orgs/kottans/repos
    curl --user "RootenberG" -X POST -d '{"title":"New issue","body":"Tutorial issue test","labels":["test_bug"]}' https://api.github.com/repos/RootenberG/kottans-backend/issues
 ```
1) Name at least three possible negative consequences of not using https.
- No permanent connection, no keys, no authentication.
2) Explain the main idea behind public key cryptography in few sentences
- There are two type of key authentication, synchronous and asynchronous, in the case of syn there is only one type of key. and in asyn there are two keys one private an another public, basically public key is for ensure that only the receiver can open this message with the public key.
3) You are creating an application for pet clinic. You need to implement the following functionality:
- POST Status code:204 body add new pet (including name, age, breed, owner's name, medical history)
- GET Status code:200 search pet by name
- PUT Status code:204 change name of an existing pet
- PUT Status code:204 add new info about pet's health
- POST Status code:200 assign a pet to a particular doctor in the clinic
- POST Status code:205 register an appointment for a pet. This request should include info about pet, doctor and appointment date and time.