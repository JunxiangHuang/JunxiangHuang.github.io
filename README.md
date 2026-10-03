# Junxiang Huang — Academic Website

This is an English-first academic website built with [HugoBlox Academic CV](https://github.com/HugoBlox/hugo-theme-academic-cv) and deployed with GitHub Pages.

## Local preview

Install Hugo Extended 0.162.1, then run:

```bash
hugo server
```

## Publish

Create a public repository named `JunxiangHuang.github.io`, push this directory to its `main` branch, and enable GitHub Pages with **GitHub Actions** as the source. The included workflow builds Hugo Extended 0.162.1 and deploys the generated site automatically.

The site is configured for `https://junxianghuang.github.io/`.

## Updating content

Publication records live in `content/publications/`. Use `status: published` or
`status: preprint`, ordered full author names, and `me` for Junxiang Huang.
`equal_contributors` contains only authors whose equal contribution is confirmed
in the paper. The shared author partial adds bold styling without changing metadata.
Homepage selections use those same publication records; keep existing URLs stable.
Experience, teaching, awards, talks and service are in `content/experience.md`.

After building, run `python3 scripts/check_site.py public` to check internal links,
author highlighting, required sections, the CV update-page links, and CV download
**deployment integrity**. The PDF byte comparison only verifies that Hugo copied
the repository asset correctly; it does not verify agreement with current metadata.

The CV entry points lead to `content/cv.md`, which records confirmed updates to the
19 September PDF snapshot and links to the unchanged download. No editable CV
source is tracked. Preserve the original PDF layout until its source is available;
keep the update page in sync when confirmed website metadata changes. See
[the CV audit](docs/cv-audit.md) for the checked fields and limits.

Metadata checked on 19 September 2026 against the CV, Google Scholar and primary
sources: arXiv 2609.10965, 2607.23574, 2607.16116, 2606.14204, 2604.07909,
2212.10421; APS DOI 10.1103/lx3w-w6jx, 10.1103/rzhg-szgj,
10.1103/PhysRevA.108.052407; Nature DOI 10.1038/s41567-026-03179-6.
Scholar lists eight of the nine records; the surface-code framework is also in
the CV and on arXiv. Equal-contribution notes were checked against the articles.
