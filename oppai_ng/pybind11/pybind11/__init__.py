from __future__ import annotations

from ._version import __version__
from ._version import version_info
from .commands import get_cmake_dir
from .commands import get_include

__all__ = (
    "version_info",
    "__version__",
    "get_include",
    "get_cmake_dir",
)
