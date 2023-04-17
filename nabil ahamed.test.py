def get_input():
    input_list=[]
    for i in range(user_input):
        string= str(input("enter the string" +str(i+1)+":"))
        input_list.append(string)
    return input_list

def comp_str (input_list) :
    options =["vowels","consonants"]
    vowels ="aeiou"
    user_choice = 0
    while user_choice<1 or user_choice>len(options) :
        print("please choose")
        for idx,element in enumerate(options) :
            print("{} - {}".format(idx+1,element))
        user_choice = int(input("enter options: "))
        if user_choice >0 and user_choice<=len(options) :
            if user_choice ==1:
                for i in range(len(input_list)):
                    result= [each for each in input_list[i].lower() if each in vowels]
                    print("number of vowels in string"+str(i+1)+  ":",len(result))
                    print("vowels in string" +str(i+1)+ ': '','.join(result))
                    print("\n")
    else:
        print("please select given options")


user_input=int(input("enter the number of string to be compared"))
while user_input<2 or user_input>5 :
    if user_input<2:
        print("\n number of strings should be greater than or equal to 2\n")
    elif user_input >5:
        print("\n number of strings should be less tha or equal to 5 \n")
    opt = ["would you like to enter another value","exit"]
    print("please choose:")
    for idx, element in enumerate(opt):
        print("option {}  - {}".format(idx+1,element))
    user_opt = int(input("enter option number :  "))
    if user_opt==1:
        user_input= int (input("enter the new value"))

    elif user_opt ==2 :
        break
    else:
        print("please select only given option")
else:
        input_list=get_input()
        print(input_list)
        comp_str(input_list)