from transformers import AutoModelForCausalLM, AutoTokenizer
import torch

def generate_character_background(keyword):
    """Generate a character background based on a given keyword using a pre-trained language model.

    Args:
        keyword (str): The keyword for the character background.

    Returns:
        str: The generated character background text.
    """
    model_name = "Shenzhi-wang/Llama3-8B-Chinese-Chat"

    # Load tokenizer and model
    tokenizer = AutoTokenizer.from_pretrained(model_name)
    model = AutoModelForCausalLM.from_pretrained(model_name)

    # Define input text
    input_text = f"I am a TRPG character, my background is {keyword}. I have an extensive story, for example..."
    input_ids = tokenizer.encode(input_text, return_tensors="pt")

    # Generate text
    output = model.generate(input_ids, max_length=200, num_return_sequences=1, temperature=0.9, pad_token_id=tokenizer.eos_token_id)

    # Decode generated text
    generated_text = tokenizer.decode(output[0], skip_special_tokens=True)

    return generated_text

if __name__ == "__main__":
    keyword = input("Please input the keyword for the character: ")
    background = generate_character_background(keyword)
    print("Generated character background:")
    print(background) 
