from ctypes import *

b0 = c_bool(0)
b1 = c_bool(1)

print(b0)
print(type(b0))
print(b0.value)

print(b1)
print(type(b1))
print(b1.value)

i0 = c_uint(-1)
print(i0.value)

c0 = c_char_p(b"test")
print(c0.value)
print(c0)

c0 = c_char_p(b"test2")
print(c0.value)
print(c0)

p0 = create_string_buffer(5)
print(p0)
print(p0.raw)
print(p0.value)

p0.value = b"a"
print(p0.raw)
print(p0)


i = c_int(42)
pi = pointer(i)

print(i)
print(pi)
print(pi.contents)



