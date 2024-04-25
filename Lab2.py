def calculate_bmi(height,weight):
    print("Height =",height)
    print("Weight=",weight)
    bmi = weight/(height*height)
    print("BMI=",bmi)
    if bmi<18.5:
        print("under weight")
    elif bmi>=18.5 and bmi<=25.0:
        print("normal weight")
    elif bmi>25.0:
        print("over weight")
weightinp=float(input("What is your weight?"))
heightinp=float(input("What is your height?(in m)"))
calculate_bmi(weight=weightinp, height=heightinp)
