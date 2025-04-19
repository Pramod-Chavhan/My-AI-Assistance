# import tkinter as tk
# from hugchat import hugchat

# def send_message():
#     user_input = entry.get().lower()
#     if user_input == "exit":
#         response.config(text="Goodbye!")
#         entry.config(state=tk.DISABLED)
#     else:
#         id = chatbot.new_conversation()
#         chatbot.change_conversation(id)
#         response_text = chatbot.chat(user_input)
#         response.config(text=response_text)

# # Initialize the chatbot
# chatbot = hugchat.ChatBot(cookie_path="engine\cookies.json")

# # Create the main window
# root = tk.Tk()
# root.title("ChatBot")

# # Create the chat history display
# response = tk.Label(root, text="", wraplength=400, justify=tk.LEFT)
# response.pack(padx=10, pady=10)

# # Create the user input field
# entry = tk.Entry(root, width=50)
# entry.pack(padx=10, pady=10)

# # Create the send button
# send_button = tk.Button(root, text="Send", command=send_message)
# send_button.pack(padx=10, pady=10)

# # Run the application
# root.mainloop()



import requests
import base64

# Replace these variables with your actual API credentials and endpoint
api_key = "YOUR_API_KEY"
api_url = "https://api.example.com/gamma"  # Example API endpoint

def generate_presentation(data):
    headers = {"Authorization": f"Bearer {api_key}", "Content-Type": "application/json"}
    response = requests.post(api_url + "/presentation", json=data, headers=headers)
    if response.status_code == 200:
        presentation_data = response.json()
        # Save or handle the presentation data as needed
        save_presentation(presentation_data)
        return True
    else:
        print(f"Error generating presentation: {response.text}")
        return False

def save_presentation(presentation_data):
    # Handle presentation data based on API response format
    # Example: Saving base64 encoded presentation to a file
    with open("presentation.pptx", "wb") as f:
        f.write(base64.b64decode(presentation_data["file_data"]))

# Example usage
presentation_data = {
    "title": "My Presentation",
    "slides": [
        {"title": "Slide 1", "content": "Content of slide 1"},
        {"title": "Slide 2", "content": "Content of slide 2"}
    ]
}

generate_presentation(presentation_data)

