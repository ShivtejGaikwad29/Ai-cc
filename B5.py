# chatbot

import random

def chatbot():
    print("Welcome to customer care chatbot")
    print("To end the chart type 'exit'")

    greetings = ['Hello','Hi','Hey','Namste']
    deliveries = ['Your order is on the way...','Your delivery will ne come in 7 days']
    refund = ['Your refund will be return after 7 days','your refund will be return online after 7 days']
    return_info = ["You can return a product within 7 days of delivery.", "Returns are accepted within 7 days."]
    issue = ['For any query contact 24389','you can visit on www.com']
    unknown_response = ["I'm not sure I understand. Could you rephrase?", "Sorry, I didn't get that."]

    while True:
        user_input = input("You: ").lower()

        if user_input == 'exit':
            print("Bot: Thank you for visiting! Have a nice day 😊")
            break

        elif any(greeting in user_input for greeting in ['hello', 'hi', 'hey']):
            print(f"Bot: {random.choice(greetings)}")
        
        elif 'delivery' in user_input or 'shipping' in user_input:
            print(f"Bot: {random.choice(deliveries)}")

        elif 'return' in user_input or 'exchange' in user_input:
            print(f"Bot: {random.choice(return_info)}")

        elif 'refund' in user_input:
            print(f"Bot: {random.choice(refund)}")

        elif 'issue' in user_input:
            print(f"Bot: {random.choice(issue)}")

        elif 'thank' in user_input:
            print("Bot: You're welcome! 😊")

        else:
            print(f"Bot: {random.choice(unknown_response)}")

# Run the chatbot
chatbot()
