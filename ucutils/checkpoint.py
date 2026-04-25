#!/usr/bin/env python
import logging
import contextlib
from typing import Dict
from dataclasses import dataclass

import unicorn

import ucutils.emu
from ucutils import PAGE_SIZE

logger = logging.getLogger(__name__)


class MemWriteTracker(ucutils.emu.Hook):
    HOOK_TYPE = unicorn.UC_HOOK_MEM_WRITE

    def __init__(self):
        super(ucutils.emu.Hook, self).__init__()

        # keys are the page starting addresses.
        # values are the contents of the page before the first write.
        self.original_pages = {}

    def hook(self, uc, optype, addr, size, value, data):
        pass


def restore_pages(emu, tracker):
    pass


@dataclass
class Checkpoint:
    written_pages: Dict[int, bytes]


@contextlib.contextmanager
def checkpoint(emu):
    """
    save the state of the emulator and restore it after executing some block of logic.
    the contents of the context manager are a dictionary with the keys:
      - written_pages (Map[int, bytes]): the address and contents of written pages

    example::
        emu.eax = 0x0
        with checkpoint(emu) as cp:
            emu.go(...)
            assert emu.eax == 69
            assert emu.mem[0x0:0x4] == 'AAAA'
        assert emu.eax == 0x0
        assert emu.mem[0x0:0x4] == '\x00\x00\x00\x00'
        assert 0x0 in cp['written_pages']
    """
    pass
