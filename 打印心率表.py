restHr = int(input('RestingHR:'))
age = int(input('Age:'))

print('{0:<9}|{1:>6}'.format('Intensity','Rate'))
print('---------|------')
intensity = 0.55
for a in range(9):
    targetHR = int(((220-age)-restHr)*intensity+restHr)
    strIntensity = '{0}%'.format(int(intensity*100))
    strtargetHR = '{}bpm'.format(targetHR)
    print('{0:<9}|{1:>6}'.format(strIntensity, strtargetHR))
    intensity += 0.05