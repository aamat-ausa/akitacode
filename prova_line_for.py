from AkitaCode.line import Line
import time
linee = "for each case of ( bat_soc bat_temp ) do"
a = time.time()
# for e in list(range(0,1000)):
l1 = Line(n=1,
        line=linee)
b = time.time()

print(l1.get_error())