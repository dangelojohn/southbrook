# southbrook — QNAP demo

Stock Odoo 19 CE demo on the QNAP (192.168.68.108), fronted by Cloudflare Tunnel.

## Public URL
See `qnap_demo_stacks` reference for the live URL.

## Local QNAP path
`/share/CACHEDEV3_DATA/Container/southbrook/`

## What's in this repo
- `docker-compose.yml` — the site's compose stack
- `config/odoo.conf` — Odoo config (secrets redacted; see `admin-creds.txt` and `.env` on the QNAP host)
- `addons/` — custom Odoo modules (currently empty for stock demos)

## What's NOT in this repo
- `postgres-data/` — DB files (use `pg_dump` to back up)
- `odoo-data/` — Odoo filestore (binary attachments, multi-GB)
- `.env`, `config/admin-creds.txt` — secrets, mode 600 on host
- `logs/`, `backups/`

## Snapshot date
2026-05-26 — initial push from a one-shot alpine/git container.
