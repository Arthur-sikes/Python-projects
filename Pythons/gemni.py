from google import genai
GEMINI_API_KEY = AIzaSyDjh8Xe7azuAhOWBWAoiJbbg8OqOncWvSQ
client = genai.Client()
text = input("enter txt:")
response = client.models.generate_content(model="gemini-2.5-flash",content=text)