# SPDX-License-Identifier: LGPL-3.0-only
{
    "name": "Southbrook Estimating — Website",
    "summary": "The customer-facing one-page kitchen configurator on "
               "southbrookcabinetry.space (Phase 2 + Phase 3 deliverable).",
    "version": "19.0.1.0.0",
    "license": "LGPL-3",
    "author": "Southbrook Cabinetry",
    "website": "https://southbrookcabinetry.space",
    "category": "Website/eCommerce",
    #
    # Independently deployable from southbrook_estimating so:
    #   - The sales-rep backend can run without the public website addon
    #     (useful for early integration testing + dealer terminals).
    #   - Backend load is not bloated by the Three.js asset bundle.
    #
    # See ../../CLAUDE.md §3 "Why two addons, not one" for the rationale.
    #
    "depends": [
        "southbrook_estimating",
        "website_product_configurator",   # OCA — public-facing wizard base
        "portal",                          # /my/... portal layout + auth
    ],
    "data": [
        # Track 2 commit 1 — portal-route view templates.
        "security/ir.model.access.csv",
        "views/portal_template.xml",
        # Phase 2 commit 1 — /kitchen-planner customer route + template.
        "views/kitchen_planner_template.xml",
        # 2026-06-03 — Southbrook Trade Portal landing at /.
        # Replaces the prior consumer-marketing hero with the
        # mobile-first private trade portal shell.
        "views/homepage_template.xml",
        # 2026-06-03 — Trade Portal auth chrome for /web/login,
        # /web/signup, /web/reset_password. Mobile-first single
        # column; embeds the stock Odoo form inside the shell via
        # web.login_layout's t-out="0" hook (form semantics
        # preserved, CSRF + redirect + signup behavior intact).
        "views/auth_template.xml",
        # 2026-06-02 — fix 500 on /shop/<slug> caused by upstream
        # OCA website_product_configurator chaining .currency_id on a
        # potentially non-singleton pricelist recordset. Override
        # swaps to website.currency_id (singleton, always available).
        "views/shop_configurator_currency_fix.xml",
    ],
    # Dedicated asset bundle (charter Q4 answer) so the OWL portal
    # components only load on the Order Builder route. Other portal
    # pages (/shop, /my, etc.) stay clean.
    #
    # T2C2 adds portal_boot.esm.js — the OWL bootstrap script that
    # finds the mount-point div on the portal page and mounts the
    # <OrderBuilder/> component into it.
    "assets": {
        "web.assets_frontend": [
            # Step 2 (2026-06-01) — shared Signature Series design
            # tokens, loaded FIRST. Cross-addon path because the
            # website depends on the estimating addon (which owns
            # the design spine). See
            # docs/CUSTOMER_TO_MANUFACTURING_FLOW.md §5.
            "southbrook_estimating/static/src/scss/_southbrook_design_tokens.scss",
            # Phase 2.5 — Three.js library back-ported from
            # southbrook_estimating Track 1. Same vendored r160 bundle.
            "southbrook_estimating/static/lib/three/three.min.js",
            "southbrook_estimating/static/lib/three/OrbitControls.js",
            "southbrook_estimating_website/static/src/scss/portal_root.scss",
            # 2026-06-03 — mobile-first Trade Portal shell SCSS
            # (palette, tap targets, card/tile layout). Styles the
            # /web/login / /web/signup / /web/reset_password chrome
            # AND the public / landing page, sharing one stylesheet.
            # Loaded BEFORE homepage.scss so portal styles win on
            # routes the legacy homepage.scss also touches.
            "southbrook_estimating_website/static/src/scss/trade_portal.scss",
            # Legacy homepage hero + features SCSS — kept loaded
            # because portal_root.scss-era classes (.o_sb_btn, etc.)
            # are still referenced from /kitchen-planner and
            # /my/southbrook/order-builder. The 2026-06-03 trade-
            # portal redesign hides every .o_sb_hero/.o_sb_features/
            # .o_sb_cta_strip element by not emitting it.
            "southbrook_estimating_website/static/src/scss/homepage.scss",
            # Phase 2 commit 1 — kitchen-planner three-pane SCSS.
            # Loads AFTER portal_root.scss so the :root tokens defined
            # there are available to .o_kp_* selectors.
            "southbrook_estimating_website/static/src/scss/planner.scss",
            # Order matters: KitchenViewport class is imported by
            # portal_boot, so it must load first.
            "southbrook_estimating_website/static/src/js/kitchen_viewport.esm.js",
            "southbrook_estimating_website/static/src/js/portal_boot.esm.js",
            # Phase 2 commit 2 — OWL <KitchenPlanner/> boot for
            # /kitchen-planner customer route. Independent of
            # portal_boot.esm.js (each bootstrap finds its own
            # mount-point div and returns early if absent on the
            # current page).
            "southbrook_estimating_website/static/src/js/planner_boot.esm.js",
        ],
    },
    "installable": True,
    "application": False,
    "auto_install": False,
}
