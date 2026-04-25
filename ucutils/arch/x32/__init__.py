#!/usr/bin/env python

import struct
import logging

import unicorn
import capstone

import ucutils

logger = logging.getLogger(__name__)


# the unicorn constant for $pc
PROGRAM_COUNTER = unicorn.x86_const.UC_X86_REG_EIP

# the unicorn constant for $sp
STACK_POINTER = unicorn.x86_const.UC_X86_REG_ESP

# the unicorn constant for $bp
BASE_POINTER = unicorn.x86_const.UC_X86_REG_EBP


# via: https://github.com/unicorn-engine/unicorn/blob/master/tests/regress/x86_gdt.py
F_GRANULARITY = 0x8
F_PROT_32 = 0x4
F_LONG = 0x2
F_AVAILABLE = 0x1

A_PRESENT = 0x80

A_PRIV_3 = 0x60
A_PRIV_2 = 0x40
A_PRIV_1 = 0x20
A_PRIV_0 = 0x0

A_CODE = 0x10
A_DATA = 0x10
A_TSS = 0x0
A_GATE = 0x0

A_DATA_WRITABLE = 0x2
A_CODE_READABLE = 0x2

A_DIR_CON_BIT = 0x4

S_GDT = 0x0
S_LDT = 0x4
S_PRIV_3 = 0x3
S_PRIV_2 = 0x2
S_PRIV_1 = 0x1
S_PRIV_0 = 0x0

# unicorn and capstone are separate projects.
# i'm not sure that the register mappings are guaranteed to be consistent.
# so we build a mapping that translates capstone <-> unicorn register constants
U2C = {}  # from unicorn constant to capstone constant
C2U = {}  # from capstone constant to unicorn constant
U2S = {}  # from unicorn constant to string
C2S = {}  # from capstone constant to string
S2U = {}  # from string to unicorn constant
S2C = {}  # from string to capstone constant
REGS = set([])  # valid register names
for const_name in dir(capstone.x86_const):
    if not const_name.startswith("X86_REG_"):
        continue

    uconst_name = "UC_" + const_name
    reg_name = const_name[len("X86_REG_") :].lower()
    uconst = getattr(unicorn.x86_const, uconst_name, None)
    cconst = getattr(capstone.x86_const, const_name, None)

    U2C[uconst] = cconst
    C2U[cconst] = uconst
    U2S[uconst] = reg_name
    C2S[cconst] = reg_name
    S2U[reg_name] = uconst
    S2C[reg_name] = uconst
    REGS.add(reg_name)


def get_capstone():
    """
    construct a capstone disassembler instance appropriate for this architecture.
    """
    pass


# our own definitions, not standardized?
GSINDEX = 1
FSINDEX = 2


def init_gdt(emu, gdt):
    # unclear why `emu.gdtr = (...)` doesn't work
    pass


# via: https://github.com/unicorn-engine/unicorn/blob/master/tests/regress/x86_gdt.py
def create_gdt_entry(base, limit, access, flags):
    pass


def set_gdt_entry(emu, gdt, entry, index):
    pass


def read_gdt_entry(emu, gdt, index):
    pass


# via: https://github.com/unicorn-engine/unicorn/blob/master/tests/regress/x86_gdt.py
def create_selector(idx, flags):
    pass


def set_gs(emu, gdt, addr, size):
    """
    set the GS.base descriptor-register field to the given address.
    this enables referencing the gs segment on x86-32.

    note: the GDT must have been initialized elsewhere for this to take effect.

    example::

        gdt = alloc_page(emu)
        init_gdt(emu, gdt)
        set_gs(emu, gdt, 0x2000, 0x1000)
    """
    pass


def get_gs(emu, gdt):
    pass


def set_fs(emu, gdt, addr, size):
    """
    set the FS.base descriptor-register field to the given address.
    this enables referencing the fs segment on x86-32.

    note: the GDT must have been initialized elsewhere for this to take effect.

    example::

        gdt = alloc_page(emu)
        init_gdt(emu, gdt)
        set_fs(emu, gdt, 0x2000, 0x1000)
    """
    pass


def get_fs(emu: unicorn.Uc, gdt):
    pass


def get_pc(emu: unicorn.Uc):
    pass


def set_pc(emu: unicorn.Uc, val):
    pass


def get_sp(emu: unicorn.Uc):
    pass


def set_sp(emu: unicorn.Uc, val):
    pass


def get_bp(emu: unicorn.Uc):
    pass


def set_bp(emu: unicorn.Uc, val: int):
    pass


def emu_go(emu: unicorn.Uc, addr: int):
    pass


def emu_stepi(emu: unicorn.Uc):
    pass


def emit_ptr(emu: unicorn.Uc, addr, value):
    pass


def parse_ptr(emu: unicorn.Uc, addr):
    pass


def get_ptr_size():
    pass


def get_gdt(emu):
    pass


def map_fs(emu, size=ucutils.FS_SIZE):
    pass
