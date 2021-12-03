#n - no of days or can take input from user
n = 8
#val_ways = no of ways a student can attend classes over n days
val_ways = 0
#absentongrad = no of ways for a student to miss the graduation
absentongrad = 0

def printways(s):
    #check if the attendance pattern formed has 4 or more consecutive days as absent
    if len(s)>=4 and (s[-1] == "A" and s[-2] == "A" and s[-3] == "A" and s[-4] == "A"):
        return

    if len(s) == n:
        global val_ways
        #for an attendance pattern increment the count of val_ways - e.g:AAPAAAPP
        val_ways = val_ways+1
        #for an attendance pattern if the nth day is absent increment the count of absentongrad - e.g:AAPAAAPA
        if s[-1] == "A":
            global absentongrad
            absentongrad = absentongrad+1
        print(s)
        return

    #for a string recursively add "A" or "P" - which means for each day there can be two ways-either present or absent
    printways(s+"A")
    printways(s+"P")

if __name__ == '__main__':
    printways("")
    #The number of ways to attend classes over n days.
    print(val_ways)

    #The probability that you will miss your graduation ceremony.
    print(f"{absentongrad}/{val_ways}")