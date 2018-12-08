import pyautogui
import time

#36.150849, -5.359628
#36.151531, -5.339395
__step = 0.00767475

fo  = open("target", "r")

latitude = []
longitude = []

while 1:
	line = fo.readline()
	if not line:
		break
	i = line.index(",")
	latitude.append(line[0:i])
	longitude.append(line[i+1:len(line)-1])

for a in latitude:
	print(a)
print("=====================")
for b in longitude:
	print(b)
print("=====================")

up = float(latitude[0])
for i in range(1,len(latitude)):
	up = max(up, float(latitude[i]))

down = float(latitude[0])
for i in range(1,len(latitude)):
	down = min(down, float(latitude[i]))

left = float(longitude[0])
for i in range(1,len(longitude)):
	left = min(left, float(longitude[i]))

right = float(longitude[0])
for i in range(1,len(longitude)):
	right = max(right, float(longitude[i]))

print(up)
print(down)
print(left)
print(right)
print("=====================")

i = up
j = left
countx = 0
county = 0
while i > down:
	i -= __step
	county += 1
while j < right:
	j += __step
	countx += 1

print(countx)
print(county)
print(countx*county)

maplist = [ [""]*countx for i in range(county) ]

print(len(maplist))
print(len(maplist[0]))
#print(maplist)

i = up
j = left
countx = 0
county = 0
while i > down:
	i -= __step
	county += 1
	while j < right:
		j += __step
		countx += 1
		#print(countx-1)
		#print(county-1)
		maplist[county-1][countx-1] = str(i + (__step/2)) + "," + str(j - (__step/2))
	j = left
	countx = 0

pyautogui.alert(u"请确认你已经打开了SU！！！")
pyautogui.alert(u"请确认你已经切换到英文输入！！！")
num = 0
for a in range(len(maplist)):
	for b in range(len(maplist[0])):
		#print(pyautogui.position()) #find mouse position
		pyautogui.click(24, 62) #click -File
		#pyautogui.moveTo(75, 433)
		pyautogui.click(75, 433) #click -Geo-location
		#pyautogui.moveTo(533, 433)
		pyautogui.click(533, 433) #click -Add More Imagery
		#pyautogui.moveTo(48, 93, duration = 1)
		pyautogui.click(48, 93, duration = 2.5) #click Search
		#pyautogui.press("leftshift")
		pyautogui.typewrite(maplist[a][b])
		pyautogui.press("enter")
		pyautogui.moveTo(48, 233)
		time.sleep(1)
		pyautogui.click()
		time.sleep(0.5)
		pyautogui.click()
		time.sleep(0.5)
		pyautogui.click()
		pyautogui.click(1900, 100)
		pyautogui.click(1940, 100)
		if num > 0:
			time.sleep(0.5)
			pyautogui.click(1540, 1087)
		num += 1

print(time.asctime(time.localtime(time.time())))
