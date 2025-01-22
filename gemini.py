import google.generativeai as genai

# Configure the API key
genai.configure(api_key="AIzaSyBOgx6_jTZIZIsaE-Ol_awnKnyneHCtmSs")  # Replace with your actual API key

# Create a model object
model = genai.GenerativeModel("gemini-1.5-flash")  # Ensure the model name is correct
print(dir(model))

def generate_content(prompt):
    try:
        # Generate content with the model
        response = model.generate_content(prompt)
        print("Generated Response:", response.text)
    except Exception as e:
        print(f"An error occurred: {e}")

# Example usage
# generate_content("Explain how ML works")

#----------------------------------------------------------------------------------

#1 Text Generation
def generate_text(prompt):
    return model.generate_content(prompt)

#2 Text summarization
def generate_summary(prompt):
    return model.generate_content(f'summarize: {prompt}')

#3 Question Answering
def generate_qa(context, prompt):
    return model.generate_content(f'context: {context} question: {prompt}')

#4 sentiment analysis
def sentiment_analyset(prompt):
    return model.generate_content(f'Analyze the sentiment of: {prompt}')

#5 Text Translation
def text_translation(text, target_language):
    return model.generate_content(f'Translate this text to {target_language}: {text}')

#1
prompt = "The Nine Tailed Fox"
print(generate_text(prompt).text)
print("-----------------------------------------------------------------------")
#2
text = "The Nine Tailed Fox is a mythical creature in Japanese folklore. It is said to be a fox with nine tails. The fox is said to be a symbol of good luck and prosperity. It is also said to be the ancestor of the legendary nine-headed dragon. The fox is also said to have been named after the name of the legendary dragon."
print(generate_summary(text).text)
print("-----------------------------------------------------------------------")
#3
context = "The Nine Tailed Fox is a mythical creature in Japanese folklore. It is said to be a fox with nine tails. The fox is said to be a symbol of good luck and prosperity. It is also said to be the ancestor of the legendary nine-headed dragon. The fox is also said to have been named after the name of the legendary dragon."
question = "What is the name of the legendary dragon?"
print(generate_qa(context, question).text)
print("-----------------------------------------------------------------------")
#4
text ="The Nine Tailed Fox in a purple crystal ball in a tree"
print(sentiment_analyset(text).text)
print("-----------------------------------------------------------------------")
#5
text ="The Nine Tailed Fox  in a purple crystal ball in a tree"
print(text_translation(text, "es").text)
print("-----------------------------------------------------------------------")





# temperature: Controls creativity (e.g., 0.7 for balanced, 1.0 for creative).
# max_tokens: Limits the response length.
# top_k: Limits the number of tokens considered at each step.
