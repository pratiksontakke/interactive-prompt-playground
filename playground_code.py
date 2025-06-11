from openai import OpenAI
from dotenv import load_dotenv
import itertools
import os

load_dotenv()

client = OpenAI()

# === Parameters to test ===
models = ["gpt-3.5-turbo"]
temperatures = [0.0, 0.7, 1.2]
max_tokens_list = [50, 150, 300]
presence_penalties = [0.0, 1.5]
frequency_penalties = [0.0, 1.5]

system_prompt = input("\nEnter system prompt (e.g., 'You are a helpful assistant'): ").strip()
user_prompt = input("Enter user prompt (e.g., 'Write a product description for iPhone'): ").strip()

# === Run combinations ===
print("\nRunning test combinations... Please wait.")

base_dir = os.path.dirname(os.path.abspath(__file__))
output_path = os.path.join(base_dir, "interactive_prompt_output.txt")
with open(output_path, "w", encoding="utf-8") as f:

    for model, temp, max_tokens, presence, frequency in itertools.product(
        models, temperatures, max_tokens_list, presence_penalties, frequency_penalties
    ):
        
        f.write("🔹" * 20 + "\n")
        f.write(f"Model: {model}\n")
        f.write(f"Temperature: {temp}\n")
        f.write(f"Max Tokens: {max_tokens}\n")
        f.write(f"Presence Penalty: {presence}\n")
        f.write(f"Frequency Penalty: {frequency}\n")

        try:
            response = client.chat.completions.create(
                model=model,
                messages=[
                    {"role": "system", "content": system_prompt},
                    {"role": "user", "content": user_prompt}
                ],
                temperature=temp,
                max_tokens=max_tokens,
                presence_penalty=presence,
                frequency_penalty=frequency,
            )

            # print(response)
            reply = response.choices[0].message.content.strip()
            f.write("\nAssistant Response:\n")
            f.write(reply + "\n")

            usage = response.usage
            f.write("\nToken Usage:\n")
            f.write(f"Prompt Tokens     : {usage.prompt_tokens}\n")
            f.write(f"Completion Tokens : {usage.completion_tokens}\n")
            f.write(f"Total Tokens      : {usage.total_tokens}\n")

        except Exception as e:
            f.write("\nError occurred: " + str(e) + "\n")

        f.write("\n")

print("\nAll combinations tested. Output saved to 'interactive_prompt_output.txt'.")
