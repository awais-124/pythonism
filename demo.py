num=int(input("Enter a number for table generation : "))
while(True):
    lower_range=int(input("Enter lower range(inclusive) : "))
    upper_range=int(input("Enter Upper range(inclusive) : "))
    if(lower_range<upper_range):
        break;
    else:
        print("... Lower range must be less or equal to upper range ...\nRe-Enter Ranges plz...\n")
        
print("🎉🎉🎉 TABLE OF ",num," 🎉🎉🎉")        
for x in range(lower_range,(upper_range+1)):
    print(num," x ", x, " = ", (x*num))