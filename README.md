# CALLBOARD: SUBTITLE STAGE

**Company:** IDAK2  
**Network:** StudioNet  
**Call:** Adapt one dramatic cue at a time without surrendering the final script to a single editor.

## House notes

A stage manager freezes the audience, tone, glossary, and ordered source cues. Each wallet may translate once. A jury-approved line raises the next cue; three rejected lines stop the show. Completing every cue produces `CURTAIN_CALL`.

## Cue book

`call_rehearsal` creates the immutable prompt book. `rehearse_cue` judges the active source only. `get_show`, `get_reviews_page`, `get_shows_page`, and `get_summary` give the static frontend batched state without a private database.

## Jury booth

Validators independently compare meaning, dramatic intention, required terminology, audience register, and speakability. Deterministic code rejects duplicate IDs, repeated translators, inactive shows, thin drafts, terminal replay, glossary failures, and issue-bearing outcomes. GenLayer consensus is essential because good localization is contextual, yet the accepted rehearsal script must be shared canonical state.

## Rehearsal call

```text
genvm-lint lint contracts/contract.py
python -m pytest tests/test_surface.py -q
node scripts/no-emoji.js
node scripts/no-emdash.js
cd frontend
npm install
npm run typecheck
npm run build
```

The frontend is a static Next.js proscenium. ProsceniumStage, CueLamp, SubtitleRail, OrchestraPit, FlyTower, and Callboard use curtain, spotlight, cue, rail, blackout, and bow motion to expose actual lifecycle state.

## Strike notes

**Contract:** `0x83B4544bDE255E25249F0b43dA9E606c493f43ec`  
**Deployment:** `0xf78585458b19472f899aee2f066d4915fc7ac3b7ecca9f016ec8b93cd11d66de`  
**Repository:** https://github.com/IDAK2/subtitle-stage  
**Public stage:** https://subtitle-stage.pages.dev/

This rehearsal does not certify a professional translation, cultural adequacy, legal localization, accessibility compliance, or performance rights. The StudioNet deployment finalized with `MAJORITY_AGREE` and leader execution `SUCCESS`.
