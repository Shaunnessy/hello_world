def main():

    
    print("Am I fat?")

    funNum = float(input("What you weigh?:"))
    endNum = float(input("Hot damn, how tall?:"))

    print(bmi(funNum, endNum))



def bmi(weight,height):

    fat = ((weight * 703)/ (height * height))
    
    if fat > 25:
        damn = "News flash! ", fat ,"... you are fat"
    elif fat <= 25 and fat >= 18 :
        damn = "mehhhh", fat ,"probably healthy"
    elif fat < 18:
        damn = "Whaoaow: ", fat ,"! you are skin"

    return damn


main()
