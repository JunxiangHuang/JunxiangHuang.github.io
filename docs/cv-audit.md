# CV snapshot audit — 3 October 2026

Baseline: `main` at `a8e0ad45dfe788a77070f57bacd1a20ebcd3660c`.
PDF: `static/uploads/resume.pdf`, last updated in
`e2cff08f7bca108c02b257dfa9bde5723b4a8089` (19 September 2026).
Reviewed all three rendered pages, extracted text, and embedded contact links.
Compared only with confirmed repository metadata, not new external claims.

## Confirmed differences and treatment

| PDF | Current repository | Treatment |
| --- | --- | --- |
| No Yuanjie Exploration position | `data/authors/me.yaml`, `content/experience.md`: QEC research intern, September 2026–present | Add to CV companion page |
| Counselor September 2022–present (p. 3) | `content/experience.md`: September 2022–July 2026, corrected in `4bce5098c0368461c3231d20e3e9ba44472999e8` | Correct on companion page |
| Teaching Assistant Scholarship (p. 2) | Removed by the same commit | Explicitly record removal on companion page; do not infer why |
| No ORCID | `data/authors/me.yaml`: 0009-0004-1225-585X, added in current head | Add confirmed link on companion page |
| No GitHub or LinkedIn links | Both are in `data/authors/me.yaml` | Contact coverage difference; existing site contact links remain available |

## Publications — no substantive drift found

Checked titles (ignoring capitalization), displayed abbreviated author prefixes and
order, equal-contribution stars, and publication/preprint status and identifiers.
The PDF abbreviates long author lists with “et al.”; it cannot validate omitted
coauthors. Site records contain full lists. PDF omits DOI links; this is a coverage
difference, not a conflicting identifier.

| PDF entry | Repository record | Result |
| --- | --- | --- |
| 9, surface-code framework | `surface-code-framework` | arXiv:2609.10965; first three equal contributors agree |
| 8, generalized Mermin inequalities | `mermin-inequalities` | arXiv:2607.23574; first four equal contributors agree |
| 7, quantum-classical crossover | `quantum-classical-crossover` | arXiv:2607.16116; first seven equal contributors agree; Huang unstarred |
| 6, partial-transpose moments | `partial-transpose-moments` | arXiv:2606.14204; all four authors agree; no stars |
| 5, VQA review | `variational-algorithms-review` | arXiv:2604.07909; first three equal contributors agree |
| 4, ground-state properties | `ground-state-properties` | Physical Review Applied 25, 054057 (2026); no stars |
| 3, local observables | `local-observables` | Physical Review A 113, 032414 (2026); all three authors agree; no stars |
| 2, cluster states | `cluster-states` | Nature Physics 22, 430–438 (2026); first four equal contributors agree |
| 1, tensor-network VQA | `tensor-network-vqa` | Physical Review A 108, 052407 (2023); first two equal contributors agree |

## Experience and contact — agreements and limits

- PKU education dates, dual bachelor's degrees, expected June 2027 graduation,
  and quantum information/computing description agree. The website additionally
  names the formal PhD field, Computer Software and Theory.
- Yuan group participation since April 2021 agrees. The site separately dates the
  doctoral researcher role from September 2022; the PDF combines group membership
  with a graduate researcher label. Preserve that distinction without inventing
  a new appointment history.
- Imperial visit (July–August 2023), both teaching appointments, Shenzhen invited
  talk (July 2025), journal/conference service, and programming/language descriptions
  agree with `content/experience.md`.
- Email agrees exactly. PDF Scholar link has an additional `hl=en` parameter but
  the same profile ID `jwlDn6kAAAAJ`. PKU/Beijing affiliation agrees; the street
  address/postcode are PDF-only and not independently confirmed by site metadata.
- Challenge Cup wording/date differences are outside this change's scope and remain
  untouched. Projects, patents, older posters, and PDF-only details lack matching
  current site fields; no additions, removals, or factual conclusions are inferred.

## Maintainable handling and check boundary

No `.tex`, `.typ`, `.docx`, or other editable CV source is tracked. The PDF stays
byte-for-byte unchanged, preserving typography, embedded links, photo, and pagination.
`content/cv.md` supplies the confirmed updates; both CV entry points lead there,
and the original download URL remains valid. Obtain the original source before
regenerating a fully synchronized PDF; the companion page is interim, not a claim
that the PDF itself is current.

`scripts/check_site.py` checks the companion links and PDF deployment byte equality.
It does **not** parse the CV or certify semantic consistency. Future metadata
changes require reviewing this audit and the companion page, even when CI passes.
