# Rating Anchors

Use these anchors to calibrate scores across voices and reviews.
Every council voice should reference the same scale.

## The Scale

| Score | Meaning | Example |
|---|---|---|
| **1-3** | Fundamentally broken. Wrong question, wrong method, or dangerous claims. | Paper claims clinical AI is safe based on a demo with no production data. |
| **4-5** | Real work but major gaps. Claims exceed evidence. Missing key citations or acknowledgments. | System works but paper overstates findings, hides limitations, has citation errors. |
| **6** | Solid engineering, weak paper. System is real but the paper doesn't do it justice. | Good system description, but no external grounding, inflated claims, marketing tone. |
| **7** | Good paper with known gaps. Claims match evidence. Limitations acknowledged. Some missing citations or analyses. | ArXiv-worthy first draft. Reviewers would ask for specific additions. |
| **8** | Strong paper. Claims well-scoped. Evidence honest. Citations verified. Limitations thorough. Ready for venue-appropriate submission. | ArXiv-ready. Clinical journal would want additional validation data. |
| **9** | Excellent. Novel contribution clearly supported. Evidence rigorous. Engages with the right literature. Limitations don't undermine the claims. | Strong enough for top-tier venue. Few reviewer requests would require new experiments. |
| **10** | Rare. Changes how the field thinks about the problem. Evidence is airtight. No reviewer could point to a gap the authors didn't already acknowledge. | Landmark paper. Every subsequent paper in the area will cite this one. |

## How to use

- Rate the paper as it is now, not as it could be after more work
- If your rating is below 7, name the single biggest fix that would raise it
- If your rating is 8+, name what would push it to 9
- Don't inflate: an 8 is a good paper. Most papers are 6-7.
- A score of 10 means "I cannot identify a meaningful weakness." Almost nothing earns this.

## Cross-voice calibration

When voices disagree by more than 2 points, the council meeting section
should explain why. A Shah 6 and a Karpathy 8 on the same paper means
Shah sees a gap (likely data/workflow) that Karpathy doesn't weight as
heavily. Name the gap, don't average away the disagreement.
