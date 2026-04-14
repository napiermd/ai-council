# Grounding Protocol

Every council review must meet three requirements beyond the base response rubric.

## 1. Ground each voice in actual publications

Before a voice speaks, retrieve 2-3 of their actual published works relevant to
the question at hand. Use web search to find real papers, blog posts, or books —
not training-data impressions of what they "would say."

Each voice entry in the Independent Scorecard must include:

```
**Sourced evidence driving this rating:**
[Specific paper/post title, venue, year] argues that [specific claim].
This [supports/contradicts/is missing from] the work under review because [reason].

**Persona inference (not sourced):**
[Any additional perspective that is inferred from their general positions
but not directly tied to a specific publication. Label it clearly.]
```

If you cannot find relevant publications for a voice, say so — and consider
whether that voice should be active.

## 2. Cross-reference claims against literature

When the work under review cites published literature, verify the citations:

- Does the cited paper actually say what the work claims it says?
- Are the numbers (kappa, correlation, sample sizes) accurately reported?
- Does the cited paper exist in searchable databases (PubMed, Google Scholar)?

Report verification results in a dedicated **Literature Verification** section
between the Independent Scorecard and the Council Meeting. Use a table:

| Claim | Cited source | Actual finding | Verdict |
|-------|-------------|----------------|---------|
| ... | ... | ... | Accurate / Mischaracterized / Misattributed / Unverifiable |

Flag any citation that cannot be verified as a submission-blocking issue.

## 3. Separate persona intuition from evidence

Every council voice has two types of input:

- **Sourced**: grounded in a specific publication, with title and finding cited
- **Inferred**: based on the person's known positions and research trajectory

Both are valuable. The problem is when they are blended — a persona claim
gets the authority of a sourced claim. Always label which is which.

In the Council Meeting section, voices should reference their publications
when making arguments:

```
**Shah:** In my Nature Medicine 2023 paper, I argued that one-time external
validation is insufficient. Your regression gate implements exactly this.
But [inferred] I'd also push on the absence of utilization metrics.
```

Not:

```
**Shah:** Your regression gate is good but you need utilization metrics.
```

The first version is verifiable. The second is generic advice with a name
attached.

## When to apply

Apply this protocol to all council reviews in rating mode or draft review mode.
For quick product decisions or architecture gut-checks, the base rubric is
sufficient — but even quick reviews benefit from at least one sourced reference
per voice.
