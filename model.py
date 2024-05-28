# Use a pipeline as a high-level helper
from transformers import AutoTokenizer, AutoModelForCausalLM
import torch

login = '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'

tokenizer = AutoTokenizer.from_pretrained("google/gemma-2b-it", token=login)
model = AutoModelForCausalLM.from_pretrained(
    "google/gemma-2b-it",
    torch_dtype=torch.bfloat16, token=login
)

input_text = "Write me a poem about Machine Learning."
input_ids = tokenizer(input_text, return_tensors="pt")

outputs = model.generate(**input_ids)
print(tokenizer.decode(outputs[0]))