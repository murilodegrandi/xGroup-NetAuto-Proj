import datetime

t = datetime.datetime.now().strftime("%d.%m.%Y - %H;%M;%S")
file = open ("!Cisco_" + str(t) + ".txt","w")
file.close()
