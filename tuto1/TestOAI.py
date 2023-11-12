# 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
# org-qchiNArWoP8mKklaFUNUkZE9
from openai import OpenAI

# Création du client OpenAI avec l'identifiant de votre organisation
client = OpenAI(
  organization='org-qchiNArWoP8mKklaFUNUkZE9',
)

# Écrivez une invite de votre choix
prompt = "Quelle est la différence entre l'intelligence artificielle et le machine learning ?"

# Utilisation du modèle GPT-3 pour obtenir une réponse à votre invite
response = client.completions.create(
  model="text-davinci-003",
  prompt=prompt,
  max_tokens=100
)

# Afficher la réponse
print(response.choices[0].text.strip())
