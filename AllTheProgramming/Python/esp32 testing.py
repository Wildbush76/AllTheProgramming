import socket
print("we starting here")
yea = socket.socket(socket.AF_INET,socket.SOCK_STREAM)

yea.connect(('192.168.0.112',80))

yea.send("this is testing idk why im testing with this but this seems like a good way to test out this thing but i dont really know either way its a good test as its sending much data i hope it works i hope  S".encode())
yea.close()


print("ayo we done")
