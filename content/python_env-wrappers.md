## What is a Python virual environment?

### Premise of a wrapper/enviroment:

- The most basic form, essentially a function that is called within a function:
    - does not have to be in the same language
    - data formats must both be compatible with one another
- Programs like SWIG can wrap programs for the use automatically
- Programmers want to use wrappers to adapt their own code to code that might not have been written by themselves or their teams
- Useful in writing error checking functions without increasing the length of code by a considerable amount
- Wrapper libraries are light bits of code that convert some interface into a compatible interface for some other program
    - allows for fixing of poor design
    - allows for two sets of code to work together
    - cross language running of programs (useful for web apps, games, etc.)
- An instance is created within the parent code in which the child code is run
    - higher level programs like Java can run lower level programs like R as an instance
    - Java itself runs in a virtual enviroment
       - builds a temporary virtual machine
       - bound by no operating system, whereas other languages required OS specific libraries and code

### Device Wrappers

-  Used to make hardware not originally designed for an OS to work
    - running windows drivers in linux
    - using modern hardware on depreciated OS
- For backwards compatibility

As technology moves forward, software and hardware become more efficient and more powerful. However, progress tends to progress discretely, rather than continuously and so there comes a point where some hardware is simply incompatible with new hardware. This can be due to a plethora of reasons; lazy developers, old hardware is simply too different from new, etc. One way to overcome this barrier is using something called a device wrapper. But what is a device wrapper?

In essence, a device wrapper is code that emulates the environment in which the device works *inside* of the main environment. What happens is that the newer, more powerful OS will set aside some memory and trick the drivers inside the old device into thinking that it is actually plugged into an older OS that supports it. 

## References

* [Wikipedia: Wrapper Library](https://en.wikipedia.org/wiki/Wrapper_library)
* [Wikipedia: Driver Wrapper](https://en.wikipedia.org/wiki/Driver_wrapper)
