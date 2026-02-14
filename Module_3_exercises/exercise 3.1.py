#Write a program that asks a fisher the length of a zander in centimeters.
# If the zander does not fulfill the size limit, the program instructs to release the fish back into the lake 
#and notifies the user of how many centimeters below the size limit the caught fish was. A zander must be 42 centimeters 
#or longer to meet the size limit.

zander = float(input("enter the lenght of the zander in centimeters:"))

if zander < 42:
    print("release the fish back into the lake")
    print(f"your fish is " + str(42-zander) + "cm below the limit!!!")
else:
    print ("you can keep the fish :)")