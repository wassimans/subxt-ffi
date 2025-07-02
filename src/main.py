#!/usr/bin/env python3

import os, ctypes
from ctypes import c_uint32

here = os.path.dirname(__file__)
lib_path = os.path.abspath(os.path.join(here, "../target/debug/libsubxt_ffi.dylib"))
lib = ctypes.cdll.LoadLibrary(lib_path)

lib.addition.argtypes = (c_uint32, c_uint32)
lib.addition.restype = c_uint32

print(lib.addition(1, 2))
