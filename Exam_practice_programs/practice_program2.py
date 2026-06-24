# python script to print the local time

import time;
itime=time.localtime();
print(time.strftime("%a %b %d %H:%M:%S %Y %Z",itime))

