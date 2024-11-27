from openAi import OpenAI
def aiProcess(command):
    client = OpenAI(
        # api_key = "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
        api_key = "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",
    )

    completion = client.chat.completions.create(
        model="gpt-3.5-turbo",
        messages=[
            {"role": "system", "content": "You are a person named Shail who speaks Hindi, English as well as Gujarati all written in english text. He is from India, Gujarat. You analyze chat history and respond like Shail."},
            {"role": "user", "content": command}
        ]
    )

    return completion.choices[0].message