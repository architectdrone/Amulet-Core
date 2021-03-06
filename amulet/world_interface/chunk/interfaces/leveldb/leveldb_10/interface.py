from __future__ import annotations

from amulet.world_interface.chunk.interfaces.leveldb.leveldb_9.interface import (
    LevelDB9Interface,
)


class LevelDB10Interface(LevelDB9Interface):
    def __init__(self):
        LevelDB9Interface.__init__(self)

        self.features["chunk_version"] = 10


INTERFACE_CLASS = LevelDB10Interface
