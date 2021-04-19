

import datetime
import os
#n=5
#while n>0:
  #  startX= startX+1
#break
startX=1
startY= 2
endX=3
endY=4
outputxmin = startX
outputymin = startY
outputxmax = endX
outputymax = endY
realtime = 1
f_xmin = open("xmin.txt","w+", realtime)
f_xmin.write( "%s %s \n" %(str(outputxmin),datetime.datetime.now() ))
f_xmin.flush()

print(datetime.datetime.now().time())

f_ymin = open("ymin.txt","w+", realtime)
f_ymin.write("%s %s \n" %(str(outputymin),datetime.datetime.now() ))
f_ymin.flush()

f_xmax = open("xmax.txt","w+", realtime)
f_xmax.write("%s %s \n" %(str(outputxmax),datetime.datetime.now() ))
f_xmax.flush()

f_ymax = open("ymax.txt","w+", realtime)
f_ymax.write("%s %s \n" %(str(outputymax),datetime.datetime.now() ))
f_ymax.flush()

f_xmin.close()
f_ymin.close()
f_xmax.close()
f_ymax.close()
