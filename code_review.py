import google.generativeai as genai

# Gemini API Key
genai.configure(api_key="your-gemini-api-key")

def review_code(code: str) -> str:

    try:
        # Gemini generative model instance
        model = genai.GenerativeModel("gemini-1.5-flash")

        # Generate a response with instructions for code review
        prompt = f"Review the following code, identify bugs, and suggest fixes:\n\n{code}"
        response = model.generate_content(prompt)

        # Extract and return the text from the response
        return response.text.strip()
    
    except Exception as e:
        raise RuntimeError(f"Error during Gemini API interaction: {e}")
