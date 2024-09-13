def program():
    questions = [["a.What is the capital of India?","Hyderabad","Kolkata","New Delhi","Uttar Pradesh",3],
                ["b.Who is the current Prime Minister of India?","Rahul Gandhi","Narendra Modi","Yogi Adityanath","Amit Shah",2],
                ["c.Who heads the RBI?","Ashwani Vaishnav","Rahul Gandhi"," D.Y.Chandrachud","Shaktikantadas",4],
                ["d.Who created Bitcoin?",'Satoshi Nakamoto','Vitalik Buterin','Charlie Lee','Gavin Andresen',1],
                ["e.What is the currency of India?","Indian Rupee",'Indian Dinar','Indian Peso','Indian Dollar',1]]

    levels= [1000,10000,50000,100000,500000]
    moneyWon=0

    for i in range(0,len(questions)):
        questionPack = questions[i]
        print(f'Your Question is\n {questionPack[0]}')
        print(f'''Options are:
    1.{questionPack[1]}
    2.{questionPack[2]}
    3.{questionPack[3]}
    4.{questionPack[4]}''')
        reply=0
        try:
            reply = int(input('ENTER THE NUMBER OF YOUR CHOSEN OPTION(1,2,3,4): '))
        except:
            print("Enter a valid NUMBER!!")
        
        if (reply==questionPack[-1]):
            print(f"Advitiya!! \n Absolutely Correct.\n You won Rs.{levels[i]}")
            moneyWon += levels[i]
        else:
            print("OHooo! Computer Mahodya is reall angry with you for answering that incorrectly.\nBut, it's okay to fail sometimes in life\n Better luck Next Time\n")
        
    
    NextQQ=input("Press Enter to continue!")
    request = input("Do you wanna repeat?\nEnter y or n: ")
    if (request=="y" or request == "Y" or request == "Yes" or request=="YES"):
        program()
    
program()