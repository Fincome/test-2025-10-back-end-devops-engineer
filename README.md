# Test technique Fincome - Backend / DevOps Engineer

Bienvenue sur ce test technique pour le poste de Backend / DevOps Engineer chez Fincome. Nous vous invitons à explorer et améliorer notre projet en répondant à l'ensemble des issues présentes.


## Instructions
- Forkez le repo
- Repondez aux différentes issues
- N'hésitez pas à prendre des initiatives et à montrer toutes les bonnes pratiques que vous maitrisez
- L'historique des commits/PRs et la qualité de la documentation (y compris ce document) comptent dans l'évaluation
- Quand vous avez terminé, invitez lucas@fincome.co sur votre fork

---

# Fincome Project

## Introduction
Cette API permet de raccourcir et décoder des URL.

## Useful commands

### Run

docker compose up --build

### Populate (jeu de données volumineux pour tester `/stats`)
docker compose run --rm api python scripts/populate_db.py


## API Endpoints

### Encode URL

POST http://127.0.0.1:5000/encode
Body:
{
  "url": "https://www.fincome.co/"
}
# Exemple:
curl -X POST -H "Content-Type: application/json" -d '{"url":"http://example.com"}' http://localhost:5000/encode

### Decode URL

GET "http://127.0.0.1:5000/decode?short_url=http://short.est/xxxx"
# Exemple:
curl -X GET "http://localhost:5000/decode?short_url=http://short.est/abc"

### Stats (à compléter si besoin)

GET http://127.0.0.1:5000/stats

## Testing

python -m unittest discover tests

---

Nous attendons avec impatience vos contributions et vos commentaires. Bonne chance !
