#Write a program that asks for the biological gender and hemoglobin value (g/l). The program the notifies the user if the hemoglobin value is low, normal or high.
   # - A normal hemoglobin value for adult females is between 117-155 g/l.
   # - A normal hemoglobin value for adult males is between 134-167 g/l.


biological_gender  = input("What is your biological gender? ").lower()

hemoglobin_value = float(input("What is your hemoglobin value (g/l)? "))


if biological_gender == "male":

    if 134 <= hemoglobin_value <= 167 :
        print("normal hemoglobin value")
    elif hemoglobin_value < 134 :
        print(" low hemoglobin value")
    else :
        print(" high hemoglobin value")

elif biological_gender == "female":

    if 117 <= hemoglobin_value <= 155 :
        print("normal hemoglobin value")
    elif hemoglobin_value < 117 :
        print(" low hemoglobin value")
    else :
        print(" high hemoglobin value")

else:
    print ("invalid biological gender")
