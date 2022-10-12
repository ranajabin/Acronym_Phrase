while True:

    user_input = str(input("Enter a Phrase: "))
    text = user_input.split()
    acrnm = " "
 
    for i in text:
        acrnm = acrnm + str(i[0]).upper()

    if user_input == 'stop': break
    print("Acronym of given Phrase is :" ,acrnm)