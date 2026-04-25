#!/usr/bin/env python

import logging
import functools
import contextlib
import collections
from typing import Any

import unicorn

import ucutils
import ucutils.arch
import ucutils.plat
from ucutils import PAGE_SIZE

SCRATCH_SIZE = PAGE_SIZE


logger = logging.getLogger(__name__)


class MemoryAccessor:
    def __init__(self, emu):
        self.emu = emu
        self.symbols: dict[int, str] = {}

    def __getitem__(self, key):
        if isinstance(key, slice):
            if key.step not in (1, None):
                raise ValueError("unsupported step value")

            if key.stop < key.start:
                raise ValueError("must have positive range")

            size = key.stop - key.start
            return self.emu.mem_read(key.start, size)
        elif isinstance(key, int):
            buf = self.emu.mem_read(key, 1)
            return buf[0]
        else:
            raise TypeError("unsupported type")

    # TODO: __setitem__ to write to memory

    def _find_heap_range(self, size: int):
        pass

    def alloc(self, size: int, reason=""):
        pass

    def map_data(self, addr: int, data: bytes, reason=""):
        pass

    def map_region(self, addr: int, size: int, reason=""):
        pass


@unicorn.ucsubclass
class Emulator(unicorn.Uc):
    """
    enhancements:
      - supports multiple hooks of the same type in parallel
      - shortcuts for reg get/set as properties
      - shortcut to memory reads

    Example::

        # register shortcuts
        print(hex(emu.pc))

        # memory slice access
        hexdump(emu.mem[0x401000:0x402000])

        # multiple simultaneous hooks
        emu.hook_add(unicorn.UC_HOOK_CODE, lambda *args: print(args))
        emu.hook_add(unicorn.UC_HOOK_CODE, lambda *args: logger.debug('%s', args))
    """

    def __init__(self, arch_const: int, mode_const: int, plat=None, *args, **kwargs):
        # must be set before super called, because its referenced in getattr

        super().__init__(arch_const, mode_const, *args, **kwargs)

        self.arch = ucutils.arch.get_arch(arch_const, mode_const)

        # public.
        self.mem = MemoryAccessor(self)

        # public.
        # mapping from address to symbolic name
        self.symbols: dict[int, str] = {}

        # public.
        self.is64 = mode_const == unicorn.UC_MODE_64

        # public.
        # platform specific helper instance from `ucutils.plat.*`.
        self.plat = ucutils.plat.bind(self, plat)

        # public.
        self.ptr_size = self.arch.get_ptr_size()

        # mapping from hook type to list of handlers.
        # we install a convenient handler that dispatches to each of the registered handlers
        #  (which are grouped by hook_type).
        self._hooks: dict[int, Any] = collections.defaultdict(lambda: [])
        # mapping from hook type to the handle representing that low level dispatch handler.
        self._handles: dict[int, int] = {}

        self._scratch = None

        self._dis = None

    @property
    def scratch(self):
        pass

    @property
    def dis(self):
        pass

    def _handle_hook(self, hook_type, *args, **kwargs):
        pass

    def hook_add(self, hook_type, fn):
        pass

    def hook_del(self, fn):
        pass

    def go(self, addr):
        pass

    def stepi(self):
        pass

    def push(self, val: int):
        pass

    def pop(self) -> int:
        pass

    def __getattr__(self, k):
        """
        support reg access shortcut, like::

            print(hex(emu.pc))
            print(hex(emu.rax))

        register names are lowercase.
        `pc` is a shortcut for the platform program counter.
        """
        if k == "pc" or k == "program_counter":
            return self.arch.get_pc(self)
        elif k == "stack_pointer":
            return self.arch.get_sp(self)
        elif k == "base_pointer":
            return self.arch.get_bp(self)

        arch = unicorn.Uc.__getattribute__(self, "arch")
        # c = self.arch.S2C.get(k, None)
        c = arch.S2C.get(k, None)
        if c is None:
            # unicorn.Uc has no __getattr__, so fall back directly to __getattribute__
            return unicorn.Uc.__getattribute__(self, k)

        return self.reg_read(c)

    def __setattr__(self, k, v):
        """
        set reg shortcut, like::

            emu.pc  = 0x401000
            emu.rax = 0xAABBCCDD

        register names are lowercase.
        `pc` is a shortcut for the platform program counter.
        """
        if k == "pc" or k == "program_counter":
            return self.arch.set_pc(self, v)
        elif k == "stack_pointer":
            return self.arch.set_sp(self, v)
        elif k == "base_pointer":
            return self.arch.set_bp(self, v)

        if hasattr(self, "arch"):
            c = self.arch.S2C.get(k, None)
            if c is not None:
                return self.reg_write(c, v)

        return super().__setattr__(k, v)


class Hook:
    """
    note: for use with `Emulator` instances, not `unicorn.Uc` instances.
    """

    class Stop(Exception):
        pass

    HOOK_TYPE = NotImplementedError()

    def hook(self, *args, **kwargs):
        raise NotImplementedError()

    def install(self, emu):
        pass

    def uninstall(self, emu):
        pass


@contextlib.contextmanager
def hook(emu, hook):
    pass


class CodeLogger(Hook):
    """
    Example::

        cl = CodeLogger(dis)
        with hook(emu, cl):
            emu.go(0x401000)
    """

    HOOK_TYPE = unicorn.UC_HOOK_CODE

    def __init__(self, dis):
        super(Hook, self).__init__()
        self.dis = dis

    def hook(self, uc, address, size, user_data):
        pass


class WriteLogger(Hook):
    """
    Example::

        wl = WriteLogger(dis)
        with hook(emu, wl):
            emu.go(0x401000)
    """

    HOOK_TYPE = unicorn.UC_HOOK_MEM_WRITE

    MEM_TYPES = {
        unicorn.UC_MEM_READ: "mem read",
        unicorn.UC_MEM_WRITE: "mem write",
        unicorn.UC_MEM_FETCH: "mem fetch",
        unicorn.UC_MEM_READ_UNMAPPED: "mem read (unmapped)",
        unicorn.UC_MEM_WRITE_UNMAPPED: "mem write (unmapped)",
        unicorn.UC_MEM_FETCH_UNMAPPED: "mem fetch (unmapped)",
        unicorn.UC_MEM_WRITE_PROT: "mem write (protected)",
        unicorn.UC_MEM_READ_PROT: "mem read (protected)",
        unicorn.UC_MEM_FETCH_PROT: "mem fetch (protected)",
        unicorn.UC_MEM_READ_AFTER: "mem read (after)",
    }

    def hook(self, uc, write_type, address, size, value, user_data):
        pass


PAGE_MASK = 0xFFFFFFFFFFFFE000


@contextlib.contextmanager
def context(emu):
    """
    provide a temporary emulation block, and restore the CPU context at the end.
    this won't restore memory, so be careful.

    example::

        assert emu.pc == 0xAAAA
        with context(emu):
            emu.go(0x401000)
            assert emu.pc == 0x401000
        assert emu.pc == 0xAAAA
    """
    pass
