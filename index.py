import gpt4free
from gpt4free import Provider
import gradio as gr
import ast

with gr.Blocks(title="ChatGPT-3.5 (YouBot)") as demo:
    # ChatBot UI
    chatbot = gr.Chatbot().style(height=500)
    user_input = gr.Textbox(label="Message input", placeholder="Ask your question to send to ChatGPT. Press enter to submit your message.")
    clear = gr.Button("Clear Chat")

    examples = gr.Examples(examples=[["Which AI model are you?"], ["What dataset are you trained on?"],["Can you access the internet?"],["Who is the richest person?"],["Tell me a fun story."],["What is 7 + 7?"],["Write the Fibonacci function in Python."]], inputs=[user_input])
    # Track all user and assistant messages for subsequent answers
    messages = []
    # user_msgs = []

    def format_string_representation(response):
        try:
            data = ast.literal_eval(response)
            if isinstance(data, dict) and 'content' in data:
                return data['content']
            else:
                return response
        except (SyntaxError, ValueError):
            return response

    def limit_queries(list):
        if (len(list) > 4):
            return list[-4:]
        else:
            return list

    def bot(history):
        # OPTIONAL: user_msgs replaces messages for string inputs (comment out messages)
        bot_response = gpt4free.Completion.create(Provider.You, prompt=limit_queries(messages), detailed=True, include_links=True)
        bot_response = format_string_representation(bot_response)
        # print(bot_response)
        messages.append([{"role":'assistant', 'content': bot_response}])

        # Stream message to chatbot by queueing characters until a full response is yielded
        history[-1][1] = ""
        for char in bot_response:
            history[-1][1] += char
            yield history
    
    def user(input_text, history):
        messages.append([{"role":'user', 'content': input_text}])
        # user_msgs.append(input_text)
   
        # Return response to chatbot and clear textbox and set its interaction to false while awaiting response
        return gr.update(value="", interactive=False), history + [[input_text, None]]    

    # Submit user input to chatbot and set textbox to be interactive
    user_input.submit(user, [user_input, chatbot], [user_input, chatbot], queue=False).then(
            bot, [chatbot], [chatbot]).then(lambda: gr.update(interactive=True), None, [user_input], queue=False)
    
    # Clear chat history and user input
    clear.click(lambda: None, None, [chatbot], queue=False).then(lambda: None, None, [user_input], queue=False)

demo.queue()
demo.launch(server_port=8080)