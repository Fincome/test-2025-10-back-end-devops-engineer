# Fincome Project

## Introduction

This project is an API that permit to shortening URL.

## Useful commands

- To build and run the project

```
docker compose up
```

## API Endpoints

- Encoding Url

```
POST : http://127.0.0.1:5000/encode
Data:
'{
    "url": "https://www.fincome.co/"
}'
```

=>
```bash
curl -X POST -H "Content-Type: application/json" -d '{"url":"http://example2.com"}' http://localhost:5000/encode
```

- Decoding Url

```
GET : "http://127.0.0.1:5000/decode?short_url=xxxx"
```

=>
```bash
curl -X GET "http://localhost:5000/decode?short_url=http://short.est/1"  
```

### Testing

To run the included tests:

```bash
python -m unittest discover tests
```