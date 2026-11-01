# Roadmap

Status meanings: **Planned** = not implemented; **In progress** = actively being implemented; **Done** = implemented and verified by tests/review. Never mark work done based only on a design or stub.

## Phase 0 — Product and repository foundation
- [x] Define product vision and initial MVP boundaries.
- [x] Establish architecture direction and replaceable adapter strategy.
- [x] Record licensing, consent, quality, and safety constraints.
- [ ] Import and verify the starter application foundation from the supplied project archive. **Blocked:** the archive was not found in the repository paths inspected or in the current working context; do not assume the existing scaffold is that archive.
- [ ] Establish reproducible backend/frontend setup and CI. **In progress:** backend pytest workflow exists and frontend TypeScript/Vite build job has been added on `chore/restore-prd-and-verify-ci`; hosted CI result is pending and frontend `package-lock.json` is not yet present. Use `npm ci` once the lockfile is committed.

## Phase 1 — Media ingest (next implementation milestone after Phase 0)
- [ ] Project CRUD and persistence.
- [ ] Secure upload for MP3/WAV/MP4/MOV.
- [ ] File size, extension, MIME, and ffprobe validation.
- [ ] Asset metadata and local storage adapter.
- [ ] FFmpeg audio extraction and normalized intermediate format.
- [ ] Background job lifecycle and progress.
- [ ] Unit/API/integration tests with small licensed/generated fixtures.

## Phase 2 — Speech understanding
- [ ] ASR adapter and English transcript.
- [ ] Timestamped segments and editable transcript.
- [ ] Speaker diarization adapter.
- [ ] Speaker review/merge/split UI.
- [ ] Confidence and failure handling.

## Phase 3 — Translation
- [ ] English-to-Hindi translation adapter.
- [ ] Context-aware chunking and terminology/glossary support.
- [ ] Editable target text.
- [ ] Human evaluation dataset and translation QA.

## Phase 4 — Voice identity and synthesis
- [ ] Consent-backed voice profile lifecycle.
- [ ] TTS adapter benchmark.
- [ ] Per-speaker synthesis.
- [ ] Duration fit, prosody controls, preview and regeneration.
- [ ] Speaker similarity and intelligibility evaluation.

## Phase 5 — Audio finishing and export
- [ ] Dialogue/background workflow with original audio fallback.
- [ ] Mixing, loudness and clipping checks.
- [ ] WAV/MP3 export.
- [ ] MP4 mux/export and synchronization validation.
- [ ] End-to-end project workflow.

## Later / explicitly out of MVP
- Lip-sync and face animation.
- Real-time/streaming dubbing.
- Large-scale cloud deployment and collaboration.
- Broad language matrix and batch enterprise workflows.
- Advanced studio editing and fine-grained sound design.

## Release gates
Each phase requires tests, documented known limitations, model/license review, and an update to PROJECT_STATUS.md. Do not advance by simply checking boxes.
