import os
import sys
from _typeshed import StrOrBytesPath, StrPath, SupportsRead, SupportsWrite
from typing import Any, AnyStr, Callable, Iterable, NamedTuple, Sequence, TypeVar, Union, overload

_PathT = TypeVar("_PathT", str, os.PathLike[str])
# Return value of some functions that may either return a path-like object that was passed in or
# a string
_PathReturn = Any

class Error(OSError): ...
class SameFileError(Error): ...
class SpecialFileError(OSError): ...
class ExecError(OSError): ...
class ReadError(OSError): ...
class RegistryError(Exception): ...

def copyfileobj(fsrc: SupportsRead[AnyStr], fdst: SupportsWrite[AnyStr], length: int = ...) -> None: ...
def copyfile(src: StrPath, dst: _PathT, *, follow_symlinks: bool = ...) -> _PathT: ...
def copymode(src: StrPath, dst: StrPath, *, follow_symlinks: bool = ...) -> None: ...
def copystat(src: StrPath, dst: StrPath, *, follow_symlinks: bool = ...) -> None: ...
def copy(src: StrPath, dst: StrPath, *, follow_symlinks: bool = ...) -> _PathReturn: ...
def copy2(src: StrPath, dst: StrPath, *, follow_symlinks: bool = ...) -> _PathReturn: ...
def ignore_patterns(*patterns: StrPath) -> Callable[[Any, list[str]], set[str]]: ...

if sys.version_info >= (3, 8):
    def copytree(
        src: StrPath,
        dst: StrPath,
        symlinks: bool = ...,
        ignore: None | Callable[[str, list[str]], Iterable[str]] | Callable[[StrPath, list[str]], Iterable[str]] = ...,
        copy_function: Callable[[str, str], None] = ...,
        ignore_dangling_symlinks: bool = ...,
        dirs_exist_ok: bool = ...,
    ) -> _PathReturn: ...

else:
    def copytree(
        src: StrPath,
        dst: StrPath,
        symlinks: bool = ...,
        ignore: None | Callable[[str, list[str]], Iterable[str]] | Callable[[StrPath, list[str]], Iterable[str]] = ...,
        copy_function: Callable[[str, str], None] = ...,
        ignore_dangling_symlinks: bool = ...,
    ) -> _PathReturn: ...

def rmtree(path: bytes | StrPath, ignore_errors: bool = ..., onerror: Callable[[Any, Any, Any], Any] | None = ...) -> None: ...

_CopyFn = Union[Callable[[str, str], None], Callable[[StrPath, StrPath], None]]

if sys.version_info >= (3, 9):
    def move(src: StrPath, dst: StrPath, copy_function: _CopyFn = ...) -> _PathReturn: ...

else:
    # See https://bugs.python.org/issue32689
    def move(src: str, dst: StrPath, copy_function: _CopyFn = ...) -> _PathReturn: ...

class _ntuple_diskusage(NamedTuple):
    total: int
    used: int
    free: int

def disk_usage(path: int | StrOrBytesPath) -> _ntuple_diskusage: ...
@overload
def chown(path: StrOrBytesPath, user: str | int, group: None = ...) -> None: ...
@overload
def chown(path: StrOrBytesPath, user: None = ..., *, group: str | int) -> None: ...
@overload
def chown(path: StrOrBytesPath, user: None, group: str | int) -> None: ...
@overload
def chown(path: StrOrBytesPath, user: str | int, group: str | int) -> None: ...

if sys.version_info >= (3, 8):
    @overload
    def which(cmd: StrPath, mode: int = ..., path: StrPath | None = ...) -> str | None: ...
    @overload
    def which(cmd: bytes, mode: int = ..., path: StrPath | None = ...) -> bytes | None: ...

else:
    def which(cmd: StrPath, mode: int = ..., path: StrPath | None = ...) -> str | None: ...

def make_archive(
    base_name: str,
    format: str,
    root_dir: StrPath | None = ...,
    base_dir: StrPath | None = ...,
    verbose: bool = ...,
    dry_run: bool = ...,
    owner: str | None = ...,
    group: str | None = ...,
    logger: Any | None = ...,
) -> str: ...
def get_archive_formats() -> list[tuple[str, str]]: ...
def register_archive_format(
    name: str,
    function: Callable[..., Any],
    extra_args: Sequence[tuple[str, Any] | list[Any]] | None = ...,
    description: str = ...,
) -> None: ...
def unregister_archive_format(name: str) -> None: ...

if sys.version_info >= (3, 7):
    def unpack_archive(filename: StrPath, extract_dir: StrPath | None = ..., format: str | None = ...) -> None: ...

else:
    # See http://bugs.python.org/issue30218
    def unpack_archive(filename: str, extract_dir: StrPath | None = ..., format: str | None = ...) -> None: ...

def register_unpack_format(
    name: str, extensions: list[str], function: Any, extra_args: Sequence[tuple[str, Any]] | None = ..., description: str = ...
) -> None: ...
def unregister_unpack_format(name: str) -> None: ...
def get_unpack_formats() -> list[tuple[str, list[str], str]]: ...
def get_terminal_size(fallback: tuple[int, int] = ...) -> os.terminal_size: ...
