import logging

import ucutils
import ucutils.arch
import ucutils.plat.win as ucwin
from ucutils.plat.win import *  # noqa: F403, F401

logger = logging.getLogger(__name__)


# recall the PEB/TEB structure layout (64-bit)::
#
#     gs (TEB)         PEB             LDR_DATA
#    +----------+ +-->+----------+ +->+----------+ +-->+--------+  +--------+
#    |          | |   |          | |  |          | |   |        +->+        +->  load order list
#    |          | |   |          | |  | +10h +-----+   |        +<-+        +<-
#    |          | |   |          | |  |          |     +--------+  +--------+
#    |          | |   |          | |  | +20h +-------+
#    | +60h  +----+   | +18h +-----+  |          |   +>+--------+  +--------+
#    |          |     |          |    | +30h +-----+   |        +->+        +->  memory order list
#    |          |     |          |    |          | |   |        +<-+        +<-
#    +----------+     +----------+    +----------+ |   +--------+  +--------+
#                                                  |
#                                                  +-->+--------+  +--------+
#                                                      |        +->+        +->  init order list
#                                                      |        +<-+        +<-
#                                                      +--------+  +--------+


def emit_teb(emu, addr, peb_addr):
    pass


def parse_teb(emu, addr):
    pass


def emit_peb(emu, addr, ldr_data_addr):
    pass


def parse_peb(emu, addr):
    pass


def emit_ldr_data(emu, addr):
    pass


def parse_ldr_data(emu, addr):
    pass


def append_list_entry(emu, head_addr, entry_addr):
    pass


def emit_ldr_data_table_entry(
    emu,
    addr,
    dllbase_addr,
    entrypoint_addr,
    sizeofimage,
    fulldllname_us,
    basedllname_us,
):
    pass


def get_teb_addr(emu):
    pass


def map_teb(emu):
    """
    allocate and initialize the TEB, PEB, and LDR_DATA structures.
    """
    pass


def append_ldr_data_entry(emu, entry_addr):
    pass
