import gpt4free
from gpt4free import Provider

# Single input queries
single_dictionary_prompt = [{'role': 'user', 'content': 'What is 7+7?'}]
single_string_prompt = ['What is 7+7?']
# Chain input queries (simulate conversation) while also asking the same question above as last query
long_dictionary_chain_prompt = [{'role': 'user', 'content': 'Which AI model are you?'}, {'role': 'assistant', 'content': 'As an AI language model from You.com, I do not have a specific name or identity like other AI models such as ChatGPT or GPT-4. I am simply referred to as YouBot.'}, {'role': 'user', 'content': 'What dataset are you trained on?'}, {'role': 'assistant', 'content': 'As an AI language model from You.com, I am trained on a diverse range of datasets from various domains including news articles, books, and websites. My training data consists of a large corpus of text, which is used to enable me to generate responses to user questions and engage in natural language conversations. It is worth mentioning that my training data is constantly being updated and refined to improve my performance over time.'}, {'role': 'user', 'content': 'What is 7+7?'}]
long_string_chain_prompt = ['Which AI model are you?', 'What dataset are you trained on?', 'What is 7+7?']


single_dictionary_prompt_response = gpt4free.Completion.create(Provider.You, prompt=single_dictionary_prompt, detailed=True, include_links=True)
single_string_prompt_response = gpt4free.Completion.create(Provider.You, prompt=single_string_prompt, detailed=True, include_links=True)
long_dictionary_chain_response = gpt4free.Completion.create(Provider.You, prompt=long_dictionary_chain_prompt, detailed=True, include_links=True)
long_string_chain_response = gpt4free.Completion.create(Provider.You, prompt=long_string_chain_prompt, detailed=True, include_links=True)

# Should answer the same question within relative bounds 
print('Single dictionary prompt response: \n' + single_dictionary_prompt_response + '\n--------------------------------')
print('Single string prompt response: \n' + single_string_prompt_response + '\n--------------------------------')

# Either formatting problems or irrelevant answers
print('Long dictionary chain response: \n' + long_dictionary_chain_response + '\n--------------------------------')
print('Long string chain response: \n' + long_string_chain_response + '\n--------------------------------')