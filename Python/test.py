from ipaddress import IPv4Network




def main():
    for addr in IPv4Network('192.168.0.0/24'):
        print(addr)

if __name__ == "__main__":
    main()
    print("Test: ",__name__)

print("__name__ equals " + __name__)

if __name__ == '__main__':
    print("if-statement was executed")