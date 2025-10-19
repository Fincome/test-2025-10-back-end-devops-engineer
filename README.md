# Test technique Fincome x API

Bienvenue à ce test technique. Nous vous invitons à explorer et améliorer notre projet en répondant à l'ensemble des issues présentes.


## Instructions
- Forkez le repo et travaillez par issues/PRs.
- Repondez dans l’ordre des issues.

---

## Issues

- **[Issue #1](https://github.com/coton-d3v/20251019-fincome-software-back-end-devops-pierrick-haumesser/issues/1) :** [BUG] Démarrage Docker/Flask défaillant (diagnostic & correctifs minimaux)
- **[Issue #2](https://github.com/coton-d3v/20251019-fincome-software-back-end-devops-pierrick-haumesser/issues/2) :** [PERF] Réduire le temps de réponse de `/stats` (optimisation SQL)
- **[Issue #3](https://github.com/coton-d3v/20251019-fincome-software-back-end-devops-pierrick-haumesser/issues/3) :** [CI] Ajouter une intégration continue (build, tests, lint, image)
- **[Issue #4](https://github.com/coton-d3v/20251019-fincome-software-back-end-devops-pierrick-haumesser/issues/4) :** [QUESTION] Choisir un cloud provider et expliquer le déploiement & le scaling Kubernetes

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
