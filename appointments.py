'''
    appointments
'''

booked = [1,3,9,12,13,18,26,27,28,29]
holidays = [4,5,15,16,21,22]

total = booked+holidays
appointments = []
for i in range(1,30):
    if i not in total :
        appointments.append(i)


print(appointments)


print ([i for i in range(1,30) if i not in total ])
