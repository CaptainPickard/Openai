import openai
import config

openai.api_key = config.openai_api_key
print("")
print('Type when prompted by >>>, enter in \'exit\' to exit the program')

# # list engines
# engines = openai.Engine.list()who am i

# # print the first engine's id
# print(engines.data[0].id)

# create a completion, the following loop runs the whole program

'''
LATEST MODEL	    MAX REQUEST	    TRAINING DATA
text-davinci-002	4,000 tokens	Up to Jun 2021
text-curie-001	    2,048 tokens	Up to Oct 2019
text-babbage-001	2,048 tokens	Up to Oct 2019
text-ada-001	    2,048 tokens	Up to Oct 2019
'''

loop_var = True

while loop_var == True:

    user_input = input('>>>')
    completion = openai.Completion.create(engine="code-davinci-002", prompt=f"{user_input}", temperature=0.5, top_p=1)

    if user_input == 'exit':
        loop_var == False
        break
    else:
        # print the completion
        print('-------------------------------------------------')
        print(completion.choices[0].text)
        print(" ")
        print('-------------------------------------------------')






