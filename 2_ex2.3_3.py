easyPace=8*60+15
tempo=7*60+12
TotalTime=easyPace+tempo*3
Hours= int(TotalTime/3600)
Minutes=((TotalTime-Hours)%60)   
print (Hours)
print(":")
print(Minutes)
