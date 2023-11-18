from .LIBzek import Zdec,Zenc
class zs():
    def __init__(self, *, path,ENCODING):
        self.__path = path
        self._enc = ENCODING

    def read(self):
        x = open(self.__path, "r")

        d = []

        strochaks = []

        b = ''

        c = x.readlines()
        print("zs pered forom")

        z = len(c)
        for m in range(z):
            for v in c[int(m)]:
                d.append(v)

            d.remove('\n')

            for s in range(len(d)):
                b = b + str(d[s])
            if self._enc == True:
                strochaks.append(Zdec(b))
            elif self._enc == False:
                strochaks.append(b)
            d = []
            b = ''

        x.close()
        return strochaks

    def write(self, acc, pa, app):
        x = open(self.__path, "a")
        x.write(f"{Zenc(acc)}\n{Zenc(pa)}\n{Zenc(app)}\n")
        x.close()

