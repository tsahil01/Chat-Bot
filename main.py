import json
import random
# from textblob import TextBlob




bot_responses = open ("responses.json")  
bot_data = json.load(bot_responses)

user_responses = open ("user_input.json")  
user_data = json.load(user_responses)

#----------------Function------------------>>>>

def bot_answer_fun(answer):
    print(f"ChatBot: {answer}")

#<<<<------------------------------------------

#----------------------------------------------
while True:
    user_greet = (_.title() for _ in user_data["Intro"]["answer"])
    bot_greet = random.choice(bot_data["Intro"]["answer"])

    user_question = ((_.replace("?","")).title() for _ in user_data["Questions"]["answer"])
    bot_question = random.choice(bot_data["Questions"]["answer"])
    # print(user_question)
    #----------------------------------------------

    user_que = input("\nUser: ").replace("?","").title()
    # user_que = "I can't spel."
    
    # print(user_que)

    if(user_que in user_greet):
        bot_answer_fun(bot_greet)

    elif(user_que in user_question):
        bot_answer_fun(bot_question)
    
    else:
        bot_answer_fun("I did'nt get that. Can you say it again?")




