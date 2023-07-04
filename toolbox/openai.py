import openai

def initialize_openai(openai_env_var : str = "OPENAI_EUROPE"):

    # Initialize OpenAI client
    openai.api_type = "azure"
    openai.api_version = "2023-03-15-preview"
    openai.api_base = os.getenv(f"{openai_env_var}_ENDPOINT")
    openai.api_key = os.getenv(f"{openai_env_var}_API_KEY")    

    # check that we have both the endpoint and the key
    if openai.api_base is None or openai.api_key is None:
        raise Exception(f"Coudn't find OpenAI credentials in environment variables {openai_env_var}_ENDPOINT and {openai_env_var}_API_KEY")