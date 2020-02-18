import struct

# st = struct.Struct("i4sif")
#
# data = st.pack(1, b"Lily", 168, 92.5)
# print(data)
#
# data = st.unpack(data)
# print(data)

data = struct.pack("i4sif", 1, b"Lily", 168, 92.5)
print(data)
data = struct.unpack("i4sif", data)
print(data)
