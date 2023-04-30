from time import time #for time recording

def tperror(prompt):
    global inwords

    words = prompt.split()
    errors = 0

    for i in range (len(inwords)):
        if i in (0,len(inwords)-1):
            if inwords[i]==words[i]:
                continue
            else:
                errors=errors+1
        else:
             if inwords[i]==words[i]:
                 if(inwords[i+1]==words[i+1] & inwords[i-1]==words[i-1]):
                     continue
                 else:
                     errors=errors+1
             else:
                 errors=errors+1
        
    return errors



def speed(inprompt,stime,etime): #Calculating the speed of type words per minute
    global time
    global inwords


    inwords = inprompt.split()
    twords = len(inwords)
    speed = twords /time

    return speed 

def elapsedtime(stime,etime):#Calculating elapsed time
    time=stime-etime
    return time


if __name__ == "__main__":
    prompt = '''In one study of average computer users, the average rate for transcription was 33 words per minute, and 19 words per minute for composition. In the same study, when the group was divided into "fast", "moderate" and "slow" groups, the average speeds were 40 wpm, 35 wpm, and 23 wpm respectively. An average professional typist reaches 50 to 80 wpm, while some positions can require 80 to 95 wpm (usually the minimum required for dispatch positions and other typing jobs), and some advanced typists work at speeds above 120 wpm. Two-finger typists, sometimes also referred to as "hunt and peck" typists, commonly reach sustained speeds of about 37 wpm for memorized text and 27 wpm when copying text, but in bursts may be able to reach speeds of 60 to 70 wpm. From the 1920s through the 1970s, typing speed (along with shorthand speed) was an important secretarial qualification and typing contests were popular and often publicized by typewriter companies as promotional tools.'''

    print("Type this :  ",prompt)

    input("Press Enter when you are ready to check your speed !!! ")

    stime=time()
    inprompt=input()
    etime=time()

# Collecting all info and returning by function

    time = round(elapsedtime(stime,etime),2)
    speed = speed(inprompt,stime,etime)
    errors= tperror(prompt)


    print("Total time elapsed : ", time , "seconds")
    print("Your average typing speed was",speed,"words per minute (w/m)")
    print("with the total of",errors,"errors")






