import os
import openai

openai.api_key = os.environ["OPENAI_API_KEY"]

name = "Akshay Sharma"
current_company = "Meesho"
current_job_title = "Product Manager"
experiences = "6 years as a full stack developer and 3 years a product manager at fintech and ecommerce company in India"
educations = "B.Tech. in Computer Science from VIT, Vellore, graduated in 2014"

LinkedInPrompt = f"Create a persona based on the following information:\n\nName: {name}\n Current Company: {current_company}\nCurrent Job Title: {current_job_title}\nProfessional Job Experience: {experiences}\nEducation: {educations} \n\nPersona:"

# generate a persona using OpenAI's GPT-3 API
response = openai.Completion.create(
    engine="text-davinci-003",
    prompt=LinkedInPrompt,
    max_tokens=200,
    n=1,
    stop=None,
    temperature=0.9,
)

# extract the persona from the API response
linkedin_persona = response.choices[0].text.strip()
print(linkedin_persona)
