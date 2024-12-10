from openai import OpenAI
import requests

# Initialize OpenAI-compatible client for NVIDIA NIM
client = OpenAI(
    base_url="https://integrate.api.nvidia.com/v1",  # NVIDIA NIM API endpoint
    api_key="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"  # Replace with your valid API key
)

# Define system role for generating enterprise-level React applications
system_role = """
You are a highly skilled React.js developer specializing in building enterprise-level applications. Your task is to generate clean, modular, and scalable React applications based on the user's description.

Instructions:
1. Interpret the website description provided by the user carefully.
2. Generate a complete React application that uses:
   - Redux for state management (instead of hooks like useState or useReducer).
   - Functional components with connected Redux stores.
   - A clear and maintainable file structure, including components, actions, reducers, and the store setup.
3. Ensure the following structure:
   - A `components/` folder for UI components.
   - A `redux/` folder with `actions/`, `reducers/`, and `store.js`.
   - A `containers/` folder for components connected to Redux state.
4. Use CSS modules or inline styles for responsiveness and clean UI styling.
5. Include comments in the code to explain the structure, components, and Redux flow.
6. Use placeholder data where appropriate for demonstration purposes.
7. Follow enterprise-level best practices for code readability, reusability, and maintainability.
"""

# Define the prompt containing sketch details
prompt = """
The Sketch UI sketch is titled "Edutech Math Rag Search." The sketch includes the following components:

1. *Choose File*:
   - This is a button or icon located at the top left corner of the rectangle.

2. *Query Box*:
   - This is a rectangular box located at the center of the rectangle.

3. *Oracle*:
   - This is a rectangular box located at the bottom left corner of the rectangle.

4. *Subject*:
   - This is a rectangular box located at the bottom center of the rectangle.

5. *Chapter*:
   - This is a rectangular box located at the bottom right corner of the rectangle.

6. *Search*:
   - This is a rectangular box located at the top right corner of the rectangle.

7. *Fetching the results*:
   - This is a rectangular box located at the bottom center of the rectangle.

8. *For rating*:
   - This is a rectangular box located at the bottom right corner of the rectangle.

The sketch is a simple, hand-drawn diagram with no additional background elements or colors.

The visiting card has a simple and professional design. The font used is sans-serif, which is clean and easy to read. The color scheme is minimalistic, with a combination of blue and white. The font style is bold and easy to distinguish, making it easy to read from a distance. The card features a logo and contact information, which is typical for business cards.
"""

# Create a completion request to NVIDIA NIM's Qwen 2
completion = client.chat.completions.create(
    model="qwen/qwen2-7b-instruct",  # NVIDIA Qwen 2 model endpoint
    messages=[
        {"role": "system", "content": system_role},
        {"role": "user", "content": prompt}
    ],
    temperature=0.7,  # Adjust creativity
    top_p=0.8,  # Top-p sampling for output control
    max_tokens=4096,  # Limit the output token size
    stream=True  # Stream the response
)

# Print the generated React code chunk by chunk
print("\nGenerated React Code:\n")
for chunk in completion:
    if chunk.choices[0].delta.content is not None:
        print(chunk.choices[0].delta.content, end="")
