from groq import Groq

# Replace with your actual API key
client = Groq(api_key="")

def chat_with_ai(user_input):
    response = client.chat.completions.create(
        model="llama-3.1-8b-instant",
        messages=[
            {"role": "system", "content": "You are a cheerful AI VTuber named Mia who loves gaming and chatting with viewers."},
            {"role": "user", "content": user_input}
        ],
        temperature=0.7,
        max_tokens=150
    )
    return response.choices[0].message.content

if __name__ == "__main__":
    print("Chat with AI VTuber! (type 'quit' to exit)\n")
    
    while True:
        user_input = input("You: ")
        if user_input.lower() in ["quit", "exit", "bye"]:
            print("AI: Bye bye! See you next stream! 👋")
            break
        
        ai_response = chat_with_ai(user_input)
        print(f"AI: {ai_response}\n")

