import socket

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
    else:
        print("Please Turn OH the Internet Connection")