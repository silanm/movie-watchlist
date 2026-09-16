# Design — Movie Watchlist

A locked design system for this app. Every page redesign reads this file before
emitting code. Do not regenerate per page — extend or amend this file when the
system needs to grow.

## Genre
editorial

## Macrostructure family
- Marketing pages: n/a (no marketing site)
- App pages: Workbench — small functional heading; the movie table (or form) is the work surface; search sits on the same row as the title; Add is the edge CTA
- Content pages: n/a

## Theme
- `--color-paper`   oklch(97.2% 0.012 142)
- `--color-paper-2` oklch(94.4% 0.018 142)
- `--color-ink`     oklch(38% 0.012 142)
- `--color-ink-2`   oklch(48% 0.01 142)
- `--color-rule`    oklch(78% 0.012 142)
- `--color-accent`  oklch(42% 0.082 142)
- `--color-focus`   oklch(42% 0.082 142)

AIT brand mapped into tokens (do not invent a second green):
- Accent / navbar: AIT Green `#3F6433` → `--color-accent`
- CTA lime: `#A1BE37` → `--color-cta`
- Sage (watched): `#8DB37F` → `--color-sage`
- Ink grey: `#494A4B` → `--color-ink`
- Rule grey: `#B6B6B6` → `--color-rule`

Contrast (list surface):
- Filled stars use `--color-star` (accent), not lime — lime on `--color-paper-2` fails graphics contrast
- Empty stars are stroked `--color-star-empty`
- Watched badge is accent fill + `--color-accent-ink`, not sage + dark ink
- Shared control height `--control-h` (2.5rem) for nav CTA, search field, search button, and row actions

## Typography
- Display: Fraunces, weight 600, style normal
- Body: Source Sans 3, weight 400
- Mono: ui-monospace, weight 400
- Display tracking: 0
- Type scale anchor: `--text-display` = clamp(1.75rem, 2vw + 1rem, 2.25rem)

## Spacing
4-point named scale. The values are in `tokens.css`. Pages must use named
tokens (`var(--space-md)`), never raw values.

## Motion
- Easings: `--ease-out` cubic-bezier(0.16, 1, 0.3, 1)
- Reveal pattern: none
- Reduced-motion fallback: opacity-only, ≤ 150 ms.

## Microinteractions stance
- silent success (no toast on edit/toggle); keep a message only after add or delete
- hover delay 800 ms · focus delay 0 ms
- watch/unwatch POSTs from the row; delete keeps a confirm page

## CTA voice
- Primary CTA: filled lime rectangle, 2px radius, dark ink on lime
- Secondary CTA: hairline rule, accent ink, no fill

## Per-page allowances
- App pages MUST NOT use enrichment — function carries the page.

## What pages MUST share
- The wordmark "Movie Watchlist"
- AIT accent placement (nav bar + ≤ 5% lime CTA)
- Fraunces + Source Sans 3
- CTA voice
- Left-aligned work surface (never a centered floating card)

## What pages MAY differ on
- List is a ledger table; add/edit/delete are a narrow left column on the same paper.

## Exports

See `tokens.css` at the project root and `movies/static/movies/tokens.css`.

## Provenance

UI redesign and AIT theming were produced with AI assistance (Cursor, Hallmark workflow), August 2026. Django backend code is student-authored for the FSAD lab.
