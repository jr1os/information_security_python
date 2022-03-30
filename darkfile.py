import ctypes


attribute_hidden = 0x02

resp = ctypes.windll.kernel32.SetFileAttributeW('fhidden.txt', attribute_hidden)

if resp:
    print("file hidden")
else:
    print("file not hidden")
