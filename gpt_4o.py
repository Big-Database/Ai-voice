import openai
import os

# Set your OpenAI API key
OPENAI_API_KEY = "your-api-key-here"

# Function to interact with GPT-4o
def chat_with_gpt4o(prompt):
    try:
        response = openai.ChatCompletion.create(
            model="gpt-4o",  # Use GPT-4o model
            messages=[{"role": "user", "content": prompt}],
            temperature=0.7  # Adjust creativity (0 = deterministic, 1 = highly creative)
        )
        return response["choices"][0]["message"]["content"]
    
    except Exception as e:
        return f"Error: {e}"

# Interactive Loop
print("Chat with GPT-4o! Type 'exit' to quit.")
while True:
    user_input = input("\nYou: ")
    if user_input.lower() in ["exit", "quit"]:
        print("Goodbye!")
        break
    
    response = chat_with_gpt4o(user_input)
    print(f"GPT-4o: {response}")
