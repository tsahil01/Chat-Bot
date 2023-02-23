import json
import random

bot_responses = open ("responses.json")  
bot_data = json.load(bot_responses)

user_responses = open ("user_input.json")  
user_data = json.load(user_responses)

#----------------Function------------------>>>>

def bot_answer_fun(answer):
    print(f"ChatBot: {answer}")

#<<<<------------------------------------------

#----------------------------------------------
bot_greet = random.choice(bot_data["Intro"]["answer"])
user_greet = user_data["Intro"]["answer"]
# print(user_greet)
#----------------------------------------------

user_que = input("User: ").title()
print(user_que)
if(user_que in user_greet):
    bot_answer_fun(bot_greet)





