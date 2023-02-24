import json
import random
# from textblob import TextBlob



bot_responses = open ("responses.json")  
bot_data = json.load(bot_responses)

user_responses = open ("user_input.json")  
user_data = json.load(user_responses)

trainer = open ("trainer.json")  
trainer_data = json.load(trainer)




#----------------Function------------------>>>>

def bot_answer_fun(answer):
    print(f"ChatBot: {answer}")
    trainer_fn(user_que,answer)
    
def trainer_fn(que,ans):
    trainer_data["user"][f"{que}"] = f"{ans}"
    trainer = open('trainer.json', 'w') 
    json.dump(trainer_data, trainer)

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

    if(user_que in user_greet):
        bot_answer_fun(bot_greet)

    elif(user_que in user_question):
        bot_answer_fun(bot_question)

    elif("Remember" in user_que.split()):
        x = (user_que.split())[1:]
        x = ", ".join(x)
        print(x)
            
    
    else:
        bot_answer_fun("I did'nt get that. Can you say it again?")




