from langfuse import Langfuse

from dotenv import load_dotenv
load_dotenv()

# Initialize Langfuse client
langfuse = Langfuse()

langfuse.create_prompt(
    name="RAG prompt",
    prompt="You are a helpful assistant who answers questions based on the provided context. The context consists of a list of document excerpts. Keep it short. Do not create facts outside of provided context. Never hallucinate or extrapolate on the context.",
    config={
        "provider": "openai",
        "model": "gpt-4o-mini",
        "top_p": 0.7,
        "max_tokens": 1024,
        "temperature": 0,
        "presence_penalty": 0,
        "frequency_penalty": 0
    },
    labels=["production"]
);
