# Refresh Checklist

Use this when updating any council profile.

## When to refresh

- A profile has not been reviewed in 90 days.
- The person's role changed.
- The person's main company, lab, or project focus changed.
- The council is going to rely heavily on that voice for a live decision.
- A new official site, lab page, major talk, or repository changes the public signal.

## Source hierarchy

Use sources in this order:

1. Official personal site
2. Official institutional or company profile
3. Official lab, project, or repository pages
4. First-party talks, essays, course pages, or technical writing
5. Secondary news only if needed for current context not visible elsewhere

## Refresh workflow

1. Re-open the existing profile.
2. Check every canonical source link still resolves.
3. Verify the current role, organization, and active themes.
4. Rewrite `Current signals` before touching the interpretive sections.
5. Update any sections that no longer fit the new public signal.
6. Re-check `Best paired with` and `Tension with other voices` so the council stays structurally distinct.
7. Update `Last reviewed`, `Source count`, and `Status`.
8. Update [`source-index.md`](./source-index.md) if status or review date changed.
9. Refresh generated recent-signal files or confirm the weekly workflow has done so.

## Definition of done

A profile refresh is complete only if:

- `Canonical sources` are explicit
- `Current signals` are tied to those sources
- the profile still reads like a distinct operating voice rather than a biography
- `Last reviewed` is current
- [`source-index.md`](./source-index.md) matches the profile status
- the matching `signals/recent/*.md` file is present or intentionally absent

## Anti-patterns

- Do not bulk-copy a bio.
- Do not treat public reputation as a substitute for source-backed distillation.
- Do not keep old `Current signals` once a role or emphasis has changed.
- Do not add a new voice without also deciding what distinct pressure that voice adds.
