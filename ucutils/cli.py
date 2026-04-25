#!/usr/bin/env python
import ast
import cmd
import shlex
import logging
import operator
import itertools

import unicorn

import ucutils
import ucutils.emu

logger = logging.getLogger("ucutil.cli")


# simple evaluator for mathematics
# via: https://stackoverflow.com/a/9558001/87207
OPS = {
    ast.Add: operator.add,
    ast.Sub: operator.sub,
    ast.Mult: operator.mul,
    ast.Div: operator.truediv,
    ast.Pow: operator.pow,
    ast.BitXor: operator.xor,
    ast.USub: operator.neg,
}


def _eval_expr(node):
    pass


def eval_expr(expr):
    """
    evaluate a mathematical expression string.
    should be safe from injection.

    example::

        >>> eval_expr('2^6')
        4
        >>> eval_expr('2**6')
        64
        >>> eval_expr('1 + 2*3**(4^5) / (6 + -7)')
        -5.0

    Args:
      expr (str): the expression to evaulate

    Returns:
      number
    """
    pass


class RHook(ucutils.emu.Hook):
    HOOK_TYPE = unicorn.UC_HOOK_MEM_READ

    def __init__(self, target):
        super(RHook, self).__init__()
        self.target = target

    def hook(self, uc, read_type, address, size, value, user_data):
        pass


class WHook(ucutils.emu.Hook):
    HOOK_TYPE = unicorn.UC_HOOK_MEM_WRITE

    def __init__(self, target):
        super(WHook, self).__init__()
        self.target = target

    def hook(self, uc, write_type, address, size, value, user_data):
        pass


class XHook(ucutils.emu.Hook):
    HOOK_TYPE = unicorn.UC_HOOK_MEM_FETCH

    def __init__(self, target):
        super(XHook, self).__init__()
        self.target = target

    def hook(self, uc, fetch_type, address, size, value, user_data):
        pass


class UnicornCli(cmd.Cmd):
    # here are the general purpose registers a user is probably interested in.
    # order here is important, since we use the contents to replace values before evaluation.
    GPREGS = [
        "RAX",
        "RBP",
        "RBX",
        "RCX",
        "RDI",
        "RDX",
        "RIP",
        "RSI",
        "RSP",
        "EAX",
        "EBP",
        "EBX",
        "ECX",
        "EDI",
        "EDX",
        "EIP",
        "ESI",
        "ESP",
        "AH",
        "AL",
        "AX",
        "BH",
        "BL",
        "BPL",
        "BP",
        "BX",
        "CH",
        "CL",
        "CS",
        "CX",
        "DH",
        "DIL",
        "DI",
        "DL",
        "DS",
        "DX",
        "R8B",
        "R9B",
        "R10B",
        "R11B",
        "R12B",
        "R13B",
        "R14B",
        "R15B",
        "R8D",
        "R9D",
        "R10D",
        "R11D",
        "R12D",
        "R13D",
        "R14D",
        "R15D",
        "R8W",
        "R9W",
        "R10W",
        "R11W",
        "R12W",
        "R13W",
        "R14W",
        "R15W",
        "R8",
        "R9",
        "R10",
        "R11",
        "R12",
        "R13",
        "R14",
        "R15",
    ]

    X64GPREGS = [
        "RAX",
        "RBP",
        "RBX",
        "RCX",
        "RDI",
        "RDX",
        "RIP",
        "RSI",
        "RSP",
        "R8",
        "R9",
        "R10",
        "R11",
        "R12",
        "R13",
        "R14",
        "R15",
    ]

    X32GPREGS = [
        "EAX",
        "EBP",
        "EBX",
        "ECX",
        "EDI",
        "EDX",
        "EIP",
        "ESI",
        "ESP",
    ]

    def __init__(self, emu):
        super().__init__()
        self.emu = emu

    @property
    def prompt(self):
        pass

    def do_exit(self, line):
        pass

    def do_quit(self, line):
        pass

    def do_q(self, line):
        pass

    def do_EOF(self, line):
        pass

    def do_reg(self, line):
        pass

    def parse_addr(self, line):
        pass

    def do_dc(self, line):
        """
        display as character (hexdump).

        Usage::

            dc [address=$pc [size=0x100]]

        Example::

            > dc
            0x8000:
            00000000: BA 5A 82 7C 18 DB C5 D9  74 24 F4 5E 29 C9 B1 59  .Z.|....t$.^)..Y
            00000010: 31 56 14 03 56 14 83 EE  FC E2 F5 FC E8 82 00 00  1V..V...........
            ...

            > dc 0x8000
            0x8000:
            00000000: BA 5A 82 7C 18 DB C5 D9  74 24 F4 5E 29 C9 B1 59  .Z.|....t$.^)..Y
            00000010: 31 56 14 03 56 14 83 EE  FC E2 F5 FC E8 82 00 00  1V..V...........
            ...

            > dc eip 10
            0x8000:
            00000000: BA 5A 82 7C 18 DB C5 D9  74 24 F4 5E 29 C9 B1 59  .Z.|....t$.^)..Y
        """
        pass

    def do_dd(self, line):
        pass

    def do_dq(self, line):
        pass

    def do_u(self, line):
        """
        disassemble at the given address.

        Usage::

            u [address=$pc [count=5]]

        Example::

            > u
            0x8000: mov     edx, 0x187c825a
            0x8005: fcmovnb st(0), st(5)
            ...

            > u 0x8000
            0x8000: mov     edx, 0x187c825a
            0x8005: fcmovnb st(0), st(5)
            ...

            > u eip 2
            0x8000: mov     edx, 0x187c825a
            0x8005: fcmovnb st(0), st(5)
        """
        pass

    def do_t(self, line):
        pass

    def do_g(self, line):
        pass

    def do_sym(self, line):
        pass

    def do_maps(self, line):
        pass

    def do_writefile(self, line):
        """
        write memory to file.

        Usage::

            writefile filename address size

        Example::

            > writefile decoded.bin 0x8000 0x100
            wrote 0x200 bytes to decoded.bin
        """
        pass

    def do_ba(self, line):
        """
        emulate until data breakpoint.

        Usage::

            ba access address

        Values for access are:
          - e: execute
          - r: read
          - w: write

        note that, in contrast to common debuggers,
         this emulator does not support multiple breakpoints.
        therefore, this command immediately begins emulation,
         and continues until the condition is met.
        """
        pass
