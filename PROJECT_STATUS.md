# Project Status — authoritative checkpoint

Last updated: 2026-11-02

## Current truth
- Public repository: https://github.com/princekdavid/voxbridge-ai
- Default branch: main. Current work is isolated on branch `chore/restore-prd-and-verify-ci`; changes are not yet merged.
- The required `PRD.md` was missing from the default branch (GitHub returned 404). A canonical PRD has now been restored on the working branch using only decisions and requirements already present in README.md, docs/MVP_SPECIFICATION.md, ARCHITECTURE.md, docs/DECISIONS.md, docs/MODEL_EVALUATION.md, and docs/SECURITY_AND_CONSENT.md. No product decisions were intentionally changed.
- Product definition, MVP specification, architecture, decisions, model evaluation, API contract, test strategy, security/consent policy, roadmap, AI contributor instructions, and ChatGPT handoff are committed in the repository.
- A minimal application scaffold exists: FastAPI health/capability endpoints, adapter protocol examples, a pytest health test, React/Vite landing screen, configuration, and backend CI workflow.
- The scaffold is not a working dubbing product. Media upload, persistence, FFmpeg processing, AI model integration, job queue, transcript editor, translation, voice profiles, mixing, and export are not implemented.

## Product decisions already made
- Product: VoxBridge AI, a complete multilingual AI dubbing platform.
- Both audio and video are first-class inputs.
- Primary differentiator: preserve authorized speaker voice identity.
- Local-first/open-source preference; avoid mandatory paid inference APIs in MVP.
- MVP: English to Hindi; MP3/WAV/MP4/MOV; 1–2 speakers initially with extensible architecture; editable transcript and translation; consent-backed voice profiles; WAV/MP3/MP4 exports.
- Exclude lip-sync, real-time dubbing, broad language coverage, and cloud deployment from MVP.

## Work completed in this checkpoint (working branch)
- Restored missing `PRD.md` as a traceable consolidation of existing product decisions and requirements.
- Expanded `.github/workflows/ci.yml` to run backend tests and a frontend TypeScript/Vite production build on pushes and pull requests targeting main.
- Kept Phase 0 incomplete: the supplied starter-application archive referenced in ROADMAP.md was not present in the repository paths inspected or in the current working context; it has not been imported or marked complete.
- Kept reproducible setup/CI incomplete pending successful hosted CI and a committed frontend dependency lockfile.

## Verification evidence and limitations
- Backend health tests: **2 passed** in a temporary verification directory reconstructed from the exact backend source files fetched from GitHub. This is useful evidence for the current scaffold, but it is not a test run from a complete checkout of the repository.
- Frontend production build: **not run successfully**. The execution environment has no network access and the npm cache did not contain the required React/Vite dependencies (`npm install --offline` failed with `ENOTCACHED`).
- GitHub Actions status for the inspected main commit had no reported status checks at inspection time. The new frontend CI job has not yet run; verify the pull request checks before merging.
- A full repository clone was unavailable in this execution environment because outbound DNS/network access to github.com failed.
- Do not claim the project-wide tests/build are passing until the hosted CI workflow succeeds.

## Immediate next steps
1. Open/verify the pull request for `chore/restore-prd-and-verify-ci`; inspect backend and frontend CI results and fix any failures.
2. Add and commit a frontend lockfile generated with a supported Node/npm version, then switch CI to `npm ci` for deterministic dependency installation.
3. Locate/provide the starter application archive referenced in Phase 0, or explicitly decide to retire that roadmap item after confirming it is no longer needed.
4. Complete Phase 0 setup/CI verification before starting Phase 1 media ingest.
5. Implement Phase 1 in small slices: project persistence, secure upload, ffprobe validation, local storage, FFmpeg extraction, background job lifecycle, and tests.

## Verified implementation inventory
- Backend: FastAPI app, root endpoint, health endpoint, capabilities endpoint, pydantic-settings config, basic model adapter protocols.
- Frontend: React/Vite TypeScript starter screen only; no real upload or API workflow.
- Tests: one health/capabilities API test module; temporary reconstructed run passed 2 tests, full checkout/CI verification pending.
- CI: backend test job existed; frontend build job added on the working branch; hosted execution pending.
- Dependency reproducibility: backend uses pyproject.toml; frontend package.json exists but no package-lock.json was found.

## Quality and integrity rules
- Distinguish implemented, stubbed, planned, and experimentally evaluated features.
- Never claim tests passed unless actually executed and results recorded.
- Never claim model quality or language support without checkpoint-specific validation.
- Update this file after every meaningful milestone; add date, changed paths, tests run, and known gaps.
- Preserve user data and never overwrite repository files without inspecting them.
