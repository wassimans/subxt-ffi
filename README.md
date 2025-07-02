# subxt-ffi
Example of exposing some Subxt functionality to other languages through FFI

- We want to expose some Subxt functionality to other programming languages (foreign languages), so they can interact with any Substrate based network (Polkadot in our case example). 
- We don't want to expose what Subxt already exposes through its public API because:
    - it's very Rust specific
    - huge API surface to cover
    - type safety is not guaranteed
- So because the Subxt API is relatively low level, what we want instead for an FFI (Foreign Function Interface) 
is to introduce more abstraction to simplify the API for client languages. The abstraction is simply a Rust crate that exposes ready to use functions that use and call the low level Subxt API under the hood. 
- A foreign language (Swift, Python ..etc) needs to call natively compiled Rust code (our library) at the assembly level through a given system ABI. Almost all major programming languages can interact with the C programming language's ABI, which is the most common and present virtually in all major operating systems. 

``` mermaid
flowchart LR
  subgraph Rust side
    subxt[Subxt Public API]
    facade[Facade crate]
    node[Substrate node]
    cabi[C ABI library]
    subxt --> facade
    facade --> node
    facade --> cabi
  end

  subgraph Client side
    swift[Swift client]
    python[Python client]
    kotlin[Kotlin client]
    js[JavaScript client]
    swift --> cabi
    python --> cabi
    kotlin --> cabi
    js --> cabi
  end
```
To build the project and produce the libraries run:

cargo build

which will produce a library in target/debug/. The exact filename depends on your platform:


Windows: libsubxt_ffi.dll
OS X: libsubxt_ffi.dylib
Linux: libsubxt_ffi.so

For the purpose of our example, we'll target Python3 via its ctypes library, and Nodejs via its ffi-napi package.

In our examples, we will hardcode the path to the resulting Rust dynamic libraries, but a more generic way would be to define a specific environment variable. On most Linux based systems it's LD_LIBRARY_PATH=$PWD/target/debug, and DYLD_LIBRARY_PATH=$PWD/target/debug for macOS. On Windows, just copy the compiled dynamic library (.dll) into the current working directory before running the examples.

To run the example for Python: python3 src/main.py
For Nodejs: node src/main.js


