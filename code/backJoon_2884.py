import datetime
H, M = input().split()

if int(H) < 10:
    H = '0' + str(H)

time = datetime.datetime.strptime(H+M, '%H%M') - datetime.timedelta(minutes=45)

print(time.timetuple().tm_hour, time.minute)