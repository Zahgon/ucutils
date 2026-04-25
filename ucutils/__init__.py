#!/usr/bin/env python

import struct
import logging

import hexdump
import unicorn

logger = logging.getLogger(__name__)


PAGE_SIZE = 0x1000
SCRATCH_ADDR = 0x4000
SCRATCH_SIZE = PAGE_SIZE
STACK_ADDR = 0x5000
STACK_SIZE = 0x3000
CODE_ADDR = 0x8000
HEAP_ADDR = 0x40000
GS_SIZE = PAGE_SIZE
FS_SIZE = PAGE_SIZE


def align(value, alignment):
    """
    align the given value.
    result will be greater than or equal to the given value.

    Args:
      value (int): the base value.
      alignment (int): the alignment increment.

    Returns:
      int: the aligned value.
    """
    pass


def get_page_base(addr):
    """
    compute the starting address of the page that contains the given address.

    example::

        assert get_page_base(0x1002) == 0x1000
    """
    pass


def mem_hexdump(emu, addr, size):
    pass


def emit_uint16(emu, addr, value):
    pass


def parse_uint16(emu, addr):
    pass


def emit_uint32(emu, addr, value):
    pass


def parse_uint32(emu, addr):
    pass


def emit_uint64(emu, addr, value):
    pass


def parse_uint64(emu, addr):
    pass


def parse_ascii(emu, addr, length=0x100):
    pass


def parse_utf16(emu, addr, length=0x100):
    pass


def is_64(emu):
    pass


def emit_ptr(emu, addr, value):
    pass


def parse_ptr(emu, addr):
    pass


def probe_addr(emu, addr):
    pass


def alloc_page(emu):
    pass


def free_page(emu, addr):
    pass
