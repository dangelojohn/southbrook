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
- `addons/` — all Southbrook-owned custom Odoo modules:
  - `southbrook_estimating/` — Order Builder backend, 11 configurator
    attributes, 6-channel pricelist engine, parametric panel-cut math,
    QWeb reports (Signature Spec Sheet, Shop Copy, Door Order),
    Signature Series design tokens consumed by the rest of the stack.
  - `southbrook_estimating_website/` — public customer surfaces:
    Trade Portal auth chrome (mobile-first /web/login + /),
    kitchen planner, order-builder portal, OWL bootstrap for the
    Three.js viewport.
  - `southbrook_configurator_ux/` — two-pane responsive UX redesign
    of /shop/<cabinet-slug>; chip selectors, sticky preview, bulk
    template/import tooling.
  - `southbrook_plm/` — ECO workflow, parametric cut-spec authority,
    engineering document trail.
  - `southbrook_mrp_pm/` — shop-floor PM: workcenter KPI Dashboard,
    cabinet family throughput, ECO tracker, floor kiosk, production
    approval, workcenter / equipment / routing seed data.
  - `southbrook_plm_productgraph/` — PLM ↔ ProductGraph bridge.
    Wires `southbrook.eco.action_apply` → `pg.release.action_execute_release`
    (one-way; ProductGraph never imports southbrook symbols).

## Sibling addons NOT in this repo

Live alongside the southbrook addons on the QNAP but have their own
canonical upstream repos, so tracking them here would just diverge:

- OCA Product Configurator suite — `product_configurator`,
  `product_configurator_mrp`, `product_configurator_sale`,
  `website_product_configurator` (<https://github.com/OCA/product-configurator>).
- OpenValue MRP costing suite — `mrp_product_costing`,
  `mrp_shop_floor_control` (<https://github.com/dangelojohn/openvalue>).
- ProductGraph (engineering catalog + release-to-MRP gate) —
  `product_graph_base`, `_revision`, `_ebom`, `_release`, `_api`
  tracked in `qnap/productgraph-v19` on this Forgejo.

## What's NOT in this repo (data)
- `postgres-data/` — DB files (use `pg_dump` to back up).
- `odoo-data/` — Odoo filestore (binary attachments, multi-GB).
- `.env`, `config/admin-creds.txt` — secrets, mode 600 on host.
- `logs/`, `backups/`.

## History
- 2026-05-26 — initial site-config snapshot from a one-shot alpine/git container.
- 2026-06-07 — imported `southbrook_estimating_website` and
  `southbrook_mrp_pm` addons; landed the Trade Portal redesign +
  Kanban `<header>` fix.
- 2026-06-09 — imported `southbrook_plm_productgraph` (bridge) after
  installing ProductGraph in the southbrook DB. Then imported the
  remaining southbrook-owned addons (`southbrook_estimating`,
  `southbrook_configurator_ux`, `southbrook_plm`) so the repo finally
  mirrors all custom code running on the QNAP.
