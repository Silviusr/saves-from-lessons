words = ("bitcoin take over the world maybe who knows perhaps")
def find_short(l):
    nl = [len(x) for x in l.split()]
    print(min(nl))
find_short(words)
