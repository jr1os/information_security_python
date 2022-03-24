import socket 
import sys


def main():
    try:
        s = socket.socket(socket.AF_INET, socket.SOCK_STREAM, 0)
    except socket.error as e:
        print("Connection Fail")
        print(f"Erro {e}")
        sys.exit()
    print("Socket success ")

    hostdest = input("insert ip address:")
    portdest = int(input("insert port:"))

    try:
        s.connect((hostdest, portdest))
        print(f"client tcp connect success {hostdest}")
        s.shutdown(2)
    except socket.error as e:
        print("Connection Fail")
        print(f"Erro {e}")
        sys.exit()


if __name__ == "__main__":
    main()
