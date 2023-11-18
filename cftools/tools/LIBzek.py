from base64 import b64encode,b64decode,b85encode,b85decode,b16encode,b16decode,a85encode,a85decode,b32encode,b32decode
def Zenc(msg):
    msgUNI = ''
    for char in msg:
        msgUNI=msgUNI+str(ord(char))+' '
    message_bytes = msgUNI.encode('utf-8')
    b64 = b64encode(message_bytes)

    b85 = b85encode(b64)
    b16 = b16encode(b85)
    b32 = b32encode(b16)
    a85 = a85encode(b32)
    out = a85.decode('ascii')
    msgUNI = ''
    for char in out:
        msgUNI = msgUNI + str(ord(char)) + ' '
    message_bytes = msgUNI.encode('utf-8')
    b64 = b64encode(message_bytes)

    b85 = b85encode(b64)
    b16 = b16encode(b85)
    b32 = b32encode(b16)
    a85 = a85encode(b32)
    out = a85.decode('ascii')
    msgUNI = ''
    for char in out:
        msgUNI = msgUNI + str(ord(char)) + ' '

    return msgUNI
def Zdec(b64BYTE):
    numbers = ''.join(c if c.isdigit() else ' ' for c in b64BYTE).split()

    out = ''
    for num in numbers:
        out = out + chr(int(num))
    base64_bytes = out.encode('utf-8')
    a85 = a85decode(base64_bytes)
    b32 = b32decode(a85)
    b16 = b16decode(b32)
    b85 = b85decode(b16)

    b64 = b64decode(b85)
    ou = b64.decode('utf-8')

    numbers = ''.join(c if c.isdigit() else ' ' for c in ou).split()

    out = ''
    for num in numbers:
        out = out+chr(int(num))
    base64_bytes = out.encode('utf-8')
    a85 = a85decode(base64_bytes)
    b32 = b32decode(a85)
    b16 = b16decode(b32)
    b85 = b85decode(b16)

    b64 = b64decode(b85)
    ou = b64.decode('utf-8')

    numbers = ''.join(c if c.isdigit() else ' ' for c in ou).split()

    out = ''
    for num in numbers:
        out = out + chr(int(num))

    return out

def NENC(msg):
    msg_bytes = msg.encode("utf-8")
    b64 = b64encode(msg_bytes)
    out = b64.decode("ascii")
    return out
def NDEC(b64B):
    b = b64B.encode("utf-8")
    b64 = b64decode(b)
    out = b64.decode("utf-8")
    return out



# b64
# b32hex
# b85
# b16
# b32
# a85

