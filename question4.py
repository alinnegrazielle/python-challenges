binNum = str(input('Enter a number in binary, up to eight digits: '))

i = 0
tsum = 0
for bin in range(len(binNum) - 1, -1, -1):
    dec = (binNum[bin] * (2**i))
    i += 1
    # print(dec)
    sum = 0
    for contents in dec:
        if contents.isdigit():
            sum += int(contents)
    # print(sum)
    tsum += sum

print('The number {} is equivalent to {} in decimal.'.format(binNum, tsum))
