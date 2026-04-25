import logging

import ucutils

logger = logging.getLogger(__name__)


def emit_list_entry(emu, addr, flink, blink):
    pass


def init_list_entry(emu, addr):
    pass


def parse_list_entry(emu, addr):
    # TODO: use ptrsize
    pass


def emit_unicode(emu, addr, ustring):
    pass


def parse_unicode(emu, addr):
    pass


def alloc_unicode(emu, s):
    pass


class DllAlreadyLoaded(ValueError):
    pass


def load_dll(emu, dll):
    """
    Args:
      emu (ucutils.Emulator): the emulator instance.
      dll (Dict[str, any]): dictionary with keys:
        filename (str): DLL filename.
        pe (pefile.PE): the parsed PE file.

    Raises:
      DllAlreadyLoaded: if memory is already mapped at the preferred base address.
    """
    pass
