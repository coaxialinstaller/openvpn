import sys

if len(sys.argv) == 2:
    user = sys.argv[1]
else:
    print("user")
    exit()

with open(f"/home/{user}/openvpn-client/server.conf","r") as conf_file:
    print()
    new = ""
    for symbols in conf_file.readlines():
        line = ""
        for symbol in symbols.split():
            if "{replace_this_user}" in symbol:
                line += symbol.replace("{replace_this_user}", user)
            else:
                if symbols.split().index(symbol) == len(symbols.split()):
                    line += symbol
                else:
                    line += symbol + " "
        new += line + "\n"
        print(line)
with open(f"/home/{user}/openvpn-client/server.conf", "w") as test:
    test.write(new)
