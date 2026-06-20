import fun
from dotenv import load_dotenv

def main():
    while True:
        x = input("You: ")
        response = fun.my_chatbot_response(x)
        print("bot: " + response)

        if x.lower() == "exit":
            print("Exiting the chatbot. Goodbye!")
            return
if __name__ == "__main__":    
    load_dotenv()  # Load environment variables from .env file
    main()