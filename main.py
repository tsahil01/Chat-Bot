import json
import random
import datetime
from textblob import TextBlob
import wikipedia



#--------------------------------
curr_d = datetime.datetime.now().strftime("%d-%m-%Y")
curr_t = datetime.datetime.now().strftime("%H:%M:%S")
# -------------------------------


bot_responses = open ("responses.json")  
bot_data = json.load(bot_responses)

user_responses = open ("user_input.json")  
user_data = json.load(user_responses)

trainer = open ("trainer2.json")  
trainer_data = json.load(trainer)

#----------------Function------------------>>>>

def bot_answer_fun(answer):
    print(f"ChatBot: {answer}")
    trainer_fn(user_que,answer)
    
def trainer_fn(que,ans):
    trainer_data["name"]["que_ans"].append({"que":f"{que} [{curr_d},{curr_t}]", "ans": ans})
    json.dump(trainer_data, trainer)

def remember_fn(x):
    trainer_data["name"]["remember"].append({f"[{curr_d},{curr_t}]": x})
    json.dump(trainer_data, trainer)
#<<<<------------------------------------------

#----------------------------------------------
while True:
    trainer = open('trainer2.json', 'w') 
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

    elif("Remember" in user_que.split()[0]):
        x = (user_que.split())[1:]
        x = " ".join(x)
        remember_fn(x)

    elif("Wiki-" in user_que.split()[0]):
        x = (user_que.split())[1:]
        x = " ".join(x)
        results = wikipedia.search(x) 
        bot_answer_fun(f"{wikipedia.page(results[0]).summary}")
        
            
    else:
        bot_answer_fun("I didn't get that. Can you say it again?")




