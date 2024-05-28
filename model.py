# Use a pipeline as a high-level helper
from transformers import AutoTokenizer, AutoModelForCausalLM
import torch


def initialize(token):
    login = token
    global tokenizer
    global model
    tokenizer = AutoTokenizer.from_pretrained("google/gemma-2b-it", token=login)
    model = AutoModelForCausalLM.from_pretrained(
    "google/gemma-2b-it",
    torch_dtype=torch.bfloat16, token=login
)
    
def run(input):
    input_ids = tokenizer(input, return_tensors="pt")

    outputs = model.generate(**input_ids)
    print(tokenizer.decode(outputs[0]))
    
initialize('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')