const path = require('path');
const ffi = require('ffi-napi');

const libPath = path.resolve(__dirname, '../target/debug/libsubxt_ffi.dylib');
const lib     = ffi.Library(libPath, {
  addition: ['uint32', ['uint32','uint32']],
});

console.log(lib.addition(1, 2));
