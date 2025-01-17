import torch
from transformers import AutoTokenizer, AutoModelForSeq2SeqLM
from langchain.memory import ConversationBufferWindowMemory

def main():
    """
    Entry point for the chatbot application using a custom-trained model.
    """
    # Load the trained tokenizer and model
    model_path = '/Users/Raneet/Desktop/untitled folder/Horimiya/checkpoint-15340' 
    tokenizer = AutoTokenizer.from_pretrained("google/flan-t5-base")
    model = AutoModelForSeq2SeqLM.from_pretrained(model_path)

    # Set up conversational memory
    conversational_memory_length = 5
    memory = ConversationBufferWindowMemory(k=conversational_memory_length, memory_key="chat_history", return_messages=True)

    # Initialize conversation history
    chat_history = []

    # Device configuration (CPU or GPU)
    device = torch.device('cuda' if torch.cuda.is_available() else 'cpu')
    model.to(device)

    # User's input question print("Type 'exit', 'bye', 'goodbye', or 'see you' to end the chat.")
    while True:
        user_question = input("Ranzeet : ")

        # Check if the user wants to exit
        if any(exit_phrase in user_question.lower() for exit_phrase in ['exit', 'bye', 'goodbye', 'see you']):
            print("Goodbye!")
            break

        # Save conversation history to memory
        for message in chat_history:
            memory.save_context(
                {'input': message['Ranzeet']},
                {'output': message['Hori-san']}
            )

        # Prepare input for the model
        inputs = tokenizer("summarize: " + user_question, return_tensors="pt", truncation=True).to(device)

        # Generate a response using the model
        outputs = model.generate(
            inputs['input_ids'],
            max_length= 124,
            num_beams=4,
            early_stopping=True
        )
        response = tokenizer.decode(outputs[0], skip_special_tokens=True)

        # Append to chat history
        message = {'Ranzeet': user_question, 'Hori-san': response}
        chat_history.append(message)

        # Print the chatbot's response
        print("Hori-san:", response)

if __name__ == "__main__":
    main()
