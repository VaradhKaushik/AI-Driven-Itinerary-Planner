from transformers import AutoTokenizer, AutoModelForCausalLM
import torch

# Ensure a GPU is available
if torch.cuda.is_available():
    device = torch.device("cuda")
    print("Using GPU:", torch.cuda.get_device_name(0))
else:
    raise EnvironmentError("This example requires a GPU, but none was found.")

# Load tokenizer and model
tokenizer = AutoTokenizer.from_pretrained("Salesforce/llama2")
model = AutoModelForCausalLM.from_pretrained("Salesforce/llama2").to(device)

# Prepare text input
text = "Write me a detailed plan for a 5 day trip to Japan, include the times and locations."
input_ids = tokenizer(text, return_tensors="pt").input_ids.to(device)

# Generate output
output = model.generate(input_ids, max_length=50)
generated_text = tokenizer.decode(output[0], skip_special_tokens=True)

print(generated_text)