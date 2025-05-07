import streamlit as st  # Streamlit is used here
import random

def chatbot():
    st.title("🛍️ ShopEasy Bot")  # Streamlit title
    st.write("Type 'exit' to end the chat.")

    greetings = ["Hello!", "Hi there!", "Hey! How can I help you?"]
    delivery_info = ["Deliveries take 3-5 business days.", "Standard delivery time is 3-5 days."]
    return_info = ["You can return a product within 7 days of delivery.", "Returns are accepted within 7 days."]
    refund_info = ["Refunds are processed within 5-7 business days after pickup.", "Refunds take about 5-7 working days."]
    unknown_response = ["I'm not sure I understand. Could you rephrase?", "Sorry, I didn't get that."]

    # Streamlit input box used instead of input()
    user_input = st.text_input("You:").lower()

    if user_input:
        if user_input == 'exit':
            st.write("Bot: Thank you for visiting! Have a nice day 😊")

        elif 'delivery' in user_input or 'shipping' in user_input:
            st.write(f"Bot: {random.choice(delivery_info)}")

        elif any(greeting in user_input for greeting in ['hello', 'hi', 'hey']):
            st.write(f"Bot: {random.choice(greetings)}")


        elif 'return' in user_input or 'exchange' in user_input:
            st.write(f"Bot: {random.choice(return_info)}")

        elif 'refund' in user_input:
            st.write(f"Bot: {random.choice(refund_info)}")

        elif 'thank' in user_input:
            st.write("Bot: You're welcome! 😊")

        else:
            st.write(f"Bot: {random.choice(unknown_response)}")

# Run the chatbot
chatbot()
