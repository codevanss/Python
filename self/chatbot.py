import google.generativeai as genai

API_KEY = "Your_API_Key"

genai.configure(api_key = API_KEY)

model = genai.GenerativeModel("gemini-2.0-flash")

chat =  model.start_chat()

print ("Chat with gemini! Type 'exit' to quit.")
while True:
    user_input = input("You: ")
    if user_input.lower() == 'exit':
        print("Exiting chat. Goodbye!")
        break


    try:
        response = chat.send_message(user_input)
        print("Gemini:", response.text)
    except Exception as e:
        print("Error:", e)