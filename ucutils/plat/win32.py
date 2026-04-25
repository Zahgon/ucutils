import logging

import ucutils
import ucutils.arch
import ucutils.plat.win as ucwin
from ucutils.plat.win import *  # noqa: F403, F401

logger = logging.getLogger(__name__)


# recall the PEB/TEB structure layout (32-bit)::
#
#     gs (TEB)         PEB             LDR_DATA
#    +----------+ +-->+----------+ +->+----------+ +-->+--------+  +--------+
#    |          | |   |          | |  |          | |   |        +->+        +->  load order list
#    |          | |   |          | |  | +0Ch +-----+   |        +<-+        +<-
#    |          | |   |          | |  |          |     +--------+  +--------+
#    |          | |   |          | |  | +14h +-------+
#    | +30h  +----+   | +0Ch +-----+  |          |   +>+--------+  +--------+
#    |          |     |          |    | +1Ch +-----+   |        +->+        +->  memory order list
#    |          |     |          |    |          | |   |        +<-+        +<-
#    +----------+     +----------+    +----------+ |   +--------+  +--------+
#                                                  |
#                                                  +-->+--------+  +--------+
#                                                      |        +->+        +->  init order list
#                                                      |        +<-+        +<-
#                                                      +--------+  +--------+

OFFSET_PEB = 0x30
OFFSET_LDR_DATA = 0xC
OFFSET_IN_LOAD_ORDER = 0x0C
OFFSET_IN_MEM_ORDER = 0x14
OFFSET_IN_INIT_ORDER = 0x1C


def emit_teb(emu, teb_addr, peb_addr):
    pass


def parse_teb(emu, teb_addr):
    pass


def emit_peb(emu, peb_addr, ldr_data_addr):
    pass


def parse_peb(emu, peb_addr):
    pass


def emit_ldr_data(emu, ldr_addr):
    pass


def parse_ldr_data(emu, ldr_addr):
    pass


def append_list_entry(emu, head_addr, entry_addr):
    pass


def emit_ldr_data_table_entry(
    emu,
    ldr_addr,
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
