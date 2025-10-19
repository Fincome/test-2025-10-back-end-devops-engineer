# scripts/populate_db.py
import random
from datetime import datetime, timedelta
from itertools import islice

from src.app import app
from src.models import db, URLS, AccessLog
from sqlalchemy import insert


def chunked(iterable, size):
    it = iter(iterable)
    while True:
        block = list(islice(it, size))
        if not block:
            break
        yield block


def biased_datetimes(n, recent_ratio=0.7, recent_days=60, days_back=540):
    """
    Génère n timestamps, dont une majorité dans les 60 derniers jours,
    le reste réparti jusqu’à 18 mois en arrière (~540 jours).
    """
    now = datetime.utcnow()
    for _ in range(n):
        if random.random() < recent_ratio:
            delta = timedelta(seconds=random.randint(0, recent_days * 24 * 3600))
        else:
            delta = timedelta(seconds=random.randint(0, days_back * 24 * 3600))
        yield now - delta


def ensure_urls(target_count: int):
    """
    Crée des URLs factices si besoin et retourne la liste des id existants.
    """
    existing = URLS.query.count()
    to_create = max(0, target_count - existing)
    if to_create > 0:
        print(f"Creating {to_create} new URLs...")
        urls = [
            URLS(short=f"u{existing + i + 1}", original=f"https://example.com/page/{existing + i + 1}")
            for i in range(to_create)
        ]
        db.session.bulk_save_objects(urls)
        db.session.commit()
    return [u.id for u in URLS.query.with_entities(URLS.id).all()]


def populate(
    num_urls=400,
    logs_per_url=3000,
    batch_size=8000,
    recent_ratio=0.7,
    recent_days=60,
    days_back=540,
    seed=42,
):
    """
    Crée environ 1,2M de lignes (400 * 3000) dans access_logs.
    """
    random.seed(seed)
    with app.app_context():
        print("Ensuring tables exist...")
        db.create_all()

        print(f"Preparing {num_urls} URLs...")
        url_ids = ensure_urls(num_urls)
        total = len(url_ids) * logs_per_url
        print(f"Planned inserts: ~{total:,} access_logs")

        def gen_logs():
            for url_id in url_ids:
                for ts in biased_datetimes(logs_per_url, recent_ratio, recent_days, days_back):
                    yield {"url_id": url_id, "created_at": ts}

        inserted = 0
        for block in chunked(gen_logs(), batch_size):
            db.session.execute(insert(AccessLog), block)
            db.session.commit()
            inserted += len(block)
            if inserted % (batch_size * 10) == 0:
                print(f"Inserted {inserted:,}/{total:,}...")

        print(f"✅ Done. Inserted {inserted:,} access_logs.")


if __name__ == "__main__":
    populate()
