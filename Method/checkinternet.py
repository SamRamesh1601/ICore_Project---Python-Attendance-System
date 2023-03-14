import socket
import ctypes


def is_connect():
    try:
        s = socket.create_connection(("www.google.com",80))
        if s is not None:
            s.close
        return True
    except OSError:
        pass
    return False

if __name__ == "__main__":
    if is_connect():
        print("Please Turn OFF the Internet Connection ")
        # ctypes.windll.user32.MessageBoxW(0,"TURN OFF Internet Connection","Warning!",1)
    else:
        print("Please Turn ON the Internet Connection")
        ctypes.windll.user32.MessageBoxW(0,"Need Internet Connection","Warning!",16)
