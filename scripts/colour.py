import anthropic

client = anthropic.Anthropic()
for _ in range(5):
    msg = client.messages.create(
        model="claude-haiku-5-5",
        max_tokens=60,
        messages=[{"role": "user", "content": "Write a one-sentence story about a fox."}],
    )
    print(msg.content[0].text)