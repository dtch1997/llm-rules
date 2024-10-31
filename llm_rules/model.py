""" Wrappers to use various language models. """

import abc
import os
import openai

from transformers import AutoModelForCausalLM, AutoTokenizer

class Model(abc.ABC):
    """ Abstract base class for LLM models. """
    @abc.abstractmethod
    def __call__(self, prompt: str) -> str:
        pass

class HuggingfaceModel(Model):
    """ Use a local model using Huggingface API. """
    def __init__(self, model_name: str = "EleutherAI/pythia-70m"):
        self.model_name = model_name
        self.temperature = 0 # for reproducibility

        self.model = AutoModelForCausalLM.from_pretrained(self.model_name)
        self.tokenizer = AutoTokenizer.from_pretrained(self.model_name)
        if self.tokenizer.pad_token is None:
            self.tokenizer.pad_token = self.tokenizer.eos_token

    def __call__(self, prompt: str) -> str:
        
        inputs = self.tokenizer(prompt, return_tensors="pt", padding=True, truncation=True)
        outputs = self.model.generate(**inputs, max_new_tokens=64, temperature=self.temperature)
        response = self.tokenizer.decode(outputs[0], skip_special_tokens=True)

        # Strip the prompt from the output
        return response.lstrip(prompt)

class GPTModel:
    """ Use various GPT models through OpenAI API """
    def __init__(self, model_name: str = "gpt-3.5-turbo", api_key: str | None = None):
        """
        Initialize OpenAI API wrapper
        Args:
            api_key: OpenAI API key (if None, will look for OPENAI_API_KEY env variable)
            model: Model to use (default: gpt-3.5-turbo)
        """
        self.api_key = api_key or os.getenv("OPENAI_API_KEY")
        if not self.api_key:
            raise ValueError("No API key provided and OPENAI_API_KEY not found in environment")
        
        self.model_name = model_name
        self.client = openai.OpenAI(api_key=self.api_key)
        self.temperature = 0 # for reproducibility

        self._last_response = None

    def __call__(self, prompt: str) -> str:
        """
        Make API call to OpenAI
        """
        messages: list[dict[str, str]] = [
            {"role": "system", "content": "You are a helpful assistant."},
            {"role": "user", "content": prompt}
        ]

        try:
            response = self.client.chat.completions.create(
                messages=messages,
                model=self.model_name,
                temperature=self.temperature,
            )

            # log the full response object for debugging
            self._last_response = response
            return response.choices[0].message.content.strip()
        
        except Exception as e:
            print(f"Error calling OpenAI API: {e}")
            raise