import os

os.chdir('/Users/ckopack/Desktop/WindTalker')

#open the particledata
particledata = open("particledata.txt", "r")

#print all the data
#str = particledata.read();
#print str

#print the last line
lineList = particledata.readlines()
#print lineList[-1]
currentWeatherData = lineList[-1]

#print the 4th column data string
list(currentWeatherData)
justRawData = currentWeatherData.split(",")[1]

splitData = justRawData.split(":")[1]
l = list(splitData)
#l.remove('"')
#l.remove('"')
print l

wind_speed = ''.join(l[1:4])
wind_gust = ''.join(l[5:7])
wind_dir = ''.join(l[8:10])
temperature = ''.join(l[11:13])
pressure = ''.join(l[14:16])
voltage = ''.join(l[17:19])
voltage2 = int(voltage) + 5

print "Wind Speed: ", wind_speed
print "Wind Gust: ", wind_gust
print "Wind Direction: ", wind_dir
print "Temperature: ", temperature
print "Pressure: ", pressure
print "Voltage: ", voltage2


#close the file
particledata.close()

#from Rick
#sprintf(currentWeatherData, "%02d%02d%03d%03d%05d%02d",
       #wind_speed, wind_gust, wind_dir, temperature, pressure, voltage);
