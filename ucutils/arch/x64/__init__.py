#!/usr/bin/env python

import struct
import logging

import unicorn
import capstone

import ucutils

logger = logging.getLogger(__name__)


# the unicorn constant for $pc
PROGRAM_COUNTER = unicorn.x86_const.UC_X86_REG_RIP

# the unicorn constant for $sp
STACK_POINTER = unicorn.x86_const.UC_X86_REG_RSP

# the unicorn constant for $bp
BASE_POINTER = unicorn.x86_const.UC_X86_REG_RBP


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


# via: https://github.com/unicorn-engine/unicorn/pull/901/files
def set_msr(uc, msr, value, scratch):
    """
    set the given model-specific register (MSR) to the given value.
    this will clobber some memory at the given scratch address, as it emits some code.
    """
    pass


def get_msr(uc, msr, scratch):
    """
    fetch the contents of the given model-specific register (MSR).
    this will clobber some memory at the given scratch address, as it emits some code.
    """
    pass


def set_gs(uc, addr, scratch):
    """
    set the GS.base hidden descriptor-register field to the given address.
    this enables referencing the gs segment on x86-64.
    """
    pass


def get_gs(uc, scratch):
    """
    fetch the GS.base hidden descriptor-register field.
    """
    pass


def set_fs(uc, addr, scratch):
    """
    set the FS.base hidden descriptor-register field to the given address.
    this enables referencing the fs segment on x86-64.
    """
    pass


def get_fs(uc, scratch):
    """
    fetch the FS.base hidden descriptor-register field.
    """
    pass


def get_pc(emu):
    pass


def set_pc(emu, val):
    pass


def get_sp(emu):
    pass


def set_sp(emu, val):
    pass


def get_bp(emu):
    pass


def set_bp(emu, val):
    pass


def emu_go(emu, addr):
    pass


def emu_stepi(emu):
    pass


def emit_ptr(emu, addr, value):
    pass


def get_ptr_size():
    pass


def parse_ptr(emu, addr):
    pass


def map_gs(emu, size=ucutils.GS_SIZE):
    pass
