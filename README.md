# southbrook — QNAP production stack

Odoo 19 CE production stack on the QNAP (192.168.68.108), fronted by
Caddy (`:9444`, southbrookcabinetry.local) and Cloudflare Tunnel
(southbrookcabinetry.space). No longer a stock demo — runs the
Southbrook custom addons listed below.

## Public URL
- Local: <https://southbrookcabinetry.local:9444>
- Public: <https://southbrookcabinetry.space>
- See `qnap_demo_stacks` reference for cross-site context.

## Local QNAP path
`/share/CACHEDEV3_DATA/Container/southbrook/`

## What's in this repo
- `docker-compose.yml` — site's compose stack (Postgres 16 + Odoo 19).
- `config/odoo.conf` — Odoo config (secrets redacted; see
  `admin-creds.txt` and `.env` on the QNAP host).
- `addons/` — Southbrook custom Odoo modules:
  - `southbrook_estimating_website/` — public customer surfaces:
    Trade Portal auth chrome (mobile-first /web/login + /),
    kitchen planner, order-builder portal, OWL bootstrap for the
    Three.js viewport.
  - `southbrook_mrp_pm/` — shop-floor PM: workcenter KPI Dashboard,
    cabinet family throughput, ECO tracker, floor kiosk, production
    approval, workcenter / equipment / routing seed data.

  Not tracked here yet (live on the QNAP): `southbrook_estimating`,
  `southbrook_plm`, `southbrook_configurator_ux`, plus the OCA
  Product Configurator suite and OpenValue MRP costing suite.

## What's NOT in this repo
- `postgres-data/` — DB files (use `pg_dump` to back up).
- `odoo-data/` — Odoo filestore (binary attachments, multi-GB).
- `.env`, `config/admin-creds.txt` — secrets, mode 600 on host.
- `logs/`, `backups/`.

## History
- 2026-05-26 — initial site-config snapshot from a one-shot alpine/git container.
- 2026-06-07 — imported `southbrook_estimating_website` and
  `southbrook_mrp_pm` addons; landed the Trade Portal redesign +
  Kanban `<header>` fix (see commits).
