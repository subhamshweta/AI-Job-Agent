import openai

#set my OpenAI key
openai.api_key = "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"

def improve_bullet_point(point):
    response = openai.ChatCompletion.create (
        model = "gpt-3.5-turbo",
        messages = [
            {"role": "system", "content": "You are a professional resume expert. Make the following resume bullet point stronger, more specific, and impactful."},
            {"role": "user", "content": point}
        ]
    )
    # Get the AI response text
    return response['choices'][0]['message']['content']

# Test it:
if __name__ == "__main__":
    bullet = "Managed client data."
    improved = improve_bullet_point(bullet)
    print("Original:", bullet)
    print("Improved:", improved)