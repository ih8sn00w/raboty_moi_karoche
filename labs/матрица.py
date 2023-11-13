ch1 = int(input())
ch2 = int(input())
ch3 = int(input())
ch4 = int(input())
ch5 = int(input())
ch6 = int(input())
ch7 = int(input())
ch8 = int(input())
ch9 = int(input())

string = [[ch1, ch2, ch3],
          [ch4, ch5, ch6],
          [ch7, ch8, ch9]]

if min(string[0]) != ch1:
    minch = min(string[0])
    minindex = string[0].index(minch)
    string[0][minindex] = ch1
    string[0][0] = minch

if min(string[1]) != ch5:
    minch = min(string[1])
    minindex = string[1].index(minch)
    string[1][minindex] = ch5
    string[1][1] = minch

if min(string[2]) != ch5:
    minch = min(string[2])
    minindex = string[2].index(minch)
    string[2][minindex] = ch9
    string[2][2] = minch

print(string)
