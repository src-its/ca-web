## Hypervisor

A hypervisor is a virtual machine manager. It runs on a physical host machine (real hardware). Hypervisor software has to translate the instructions meant for the Virtual CPU and convert it into instructions for the physical CPU. 

Modern processors support virtualization extensions, which help to minimize performance overhead for virtualized operating systems by mapping a slice of physical CPU directly to the Virtual CPU. [Intel support a technology called VT-x and the AMD equivalent is AMD-V.] For CPUs that do not support virtualization extensions, a hypervisor translates instructions for the Virtual CPU. 


## QEMU & KQEMU

QEMU emulates a physical machine via a special recompiler, referred to as [TCG or Tiny Code Generator](http://wiki.qemu.org/Documentation/TCG), that transforms (tranaslates) binary code written for a given processor into that intended for another one (say, to run ARM/Power arch using an x86 PC.

In the specific case where both source and target are the same architecture (like the common case of x86 on x86), it still has to parse the code to remove any 'privileged instructions' and replace them with context switches. To make it as efficient as possible on x86 Linux, there's a kernel module called KQemu that handles this. Being a kernel module, KQemu is able to execute most code unchanged, replacing only the lowest-level ([ring0](https://en.wikipedia.org/wiki/Protection_ring)-only) instructions. In this case, Qemu still allocates RAM for the emulated machine and loads the code. The difference is that, instead of recompiling the code, Qemu calls KQemu for code scaning/patching/execution.

To emulate more than just the processor, QEMU includes peripheral emulators: disk, network, VGA, PCI, USB, serial/parallel ports, etc.


### KVM

[Kernel-based Virtual Machine (KVM)](http://www.linux-kvm.org/page/Main_Page)

KVM (for Kernel-based Virtual Machine) is a full virtualization solution for Linux on x86 hardware containing virtualization extensions (Intel VT or AMD-V). It consists of a loadable kernel module, `kvm.ko`, that provides the core virtualization infrastructure and a processor specific module, `kvm-intel.ko` or `kvm-amd.ko`, that switches a processor into a new 'guest' state. In other words, KVM is the Linux kernel module that enables this mapping of physical CPU to Virtual CPU. This mapping provides the hardware acceleration for Virtual Machine and boosts its performance.

With KVM, privileged [ring0](https://en.wikipedia.org/wiki/Protection_ring) instructions in the guest state fall back to the hypervisor code. The KVM kernel module also handles a few low-level parts of emulation, like [memory management unit (MMU)](https://en.wikipedia.org/wiki/Memory_management_unit) registers and some parts of [Peripheral Component Interconnect (PCI)](https://en.wikipedia.org/wiki/Conventional_PCI) emulated hardware.

Using KVM, one can run multiple virtual machines running unmodified Linux or Windows images. Each virtual machine has private virtualized hardware: a network card, disk, graphics adapter, etc.

Since KVM is really a driver for the physical CPU capabilities, it is very tightly associated with the CPU architecture (the x86 architecture). This means that the benefits of hardware acceleration will be available only if the Virtual Machine CPU also uses the same architecture (x86).


### KVM vs. QEMU

* QEMU is a Type 2 hypervisor; it can be installed on an operating system and it runs as an indepent process.

* KVM is a Type 1 hypervisor and it comes installed with particular hardware systems.

* QEMU runs on a processor without the need for hardware virtualization extension (Intel VT/VT-d, AMD-V) while KVM uses it.

* QEMU can exists without KVM, but the processing of communication between host and guest CPU is slow. KVM, by contrast, can't emulate another architecture without QEMU to provide full hypervisor functionality.

* When working together, KVM arbitrates access to the CPU and memory, and QEMU emulates the hardware resources (hard disk, video, USB, etc.). When working alone, QEMU emulates both CPU and hardware.

* KVM is a fork of the [QEMU](http://wiki.qemu.org/Main_Page) executable. Eventually, the goal is that QEMU should work anywhere, and if a KVM kernel module is available, it could be used.


## References

* [Difference between KVM and QEMU](http://serverfault.com/questions/208693/difference-between-kvm-and-qemu)
* [KVM and QEMU – do you know the connection?](http://www.innervoice.in/blogs/2014/03/10/kvm-and-qemu/)
