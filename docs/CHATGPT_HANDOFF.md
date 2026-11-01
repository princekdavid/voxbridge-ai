# ChatGPT Project Handoff — VoxBridge AI

Use this document to start a fresh ChatGPT project/chat. The repository is the canonical record; this note is the compact entry point.

## First instruction for the new chat
“Continue development of VoxBridge AI using https://github.com/princekdavid/voxbridge-ai as the source of truth. First inspect README.md, AGENTS.md, PROJECT_STATUS.md, PRD.md, docs/MVP_SPECIFICATION.md, ARCHITECTURE.md, docs/DECISIONS.md, ROADMAP.md, and the current repository tree. Do not assume prior chat context. Verify what is actually implemented, then continue with the next unchecked roadmap item. Make focused changes, add tests, run checks, and update PROJECT_STATUS.md and relevant docs. Do not claim work is done unless verified.”

## Product summary
VoxBridge AI is a complete AI dubbing platform. Users upload audio/video, transcribe and diarize speech, translate it, generate target-language speech while preserving an authorized speaker's vocal identity, align it to timing, retain music/ambience/effects where possible, and export dubbed audio/video.

## Decisions already made
- Both audio and video inputs.
- Main differentiator is voice identity preservation.
- Local-first/open-source direction; avoid mandatory paid AI APIs for MVP.
- Initial language pair English → Hindi.
- Initial formats MP3/WAV/MP4/MOV.
- Initial UX optimized for 1–2 speakers, extensible to multiple speakers.
- Editable transcript and translation.
- Voice profiles require explicit speaker ownership/authorization and consent tracking.
- WAV/MP3/MP4 output.
- No lip-sync, real-time dubbing, broad language coverage, or cloud deployment in MVP.

## Pipeline concept
Ingest → probe/validate → extract/normalize → optional dialogue/background separation → ASR + diarization + timestamps → editable transcript → contextual translation → authorized voice profile assignment → TTS → timing/prosody fit → mix with background → mux video → quality checks → export.

## Critical technical cautions
- Preserve voice identity features (timbre, pitch range/movement, formants, cadence, prosody, emotion); do not claim literal waveform preservation across languages.
- Separation is imperfect. Vocals are not synonymous with dialogue; laughter/singing may need preservation.
- Keep source and intermediate stems; provide manual review and fallback.
- Model language support and licensing vary by exact checkpoint. Verify commercial terms before adoption.
- Candidate research only: faster-whisper/Whisper for ASR; pyannote.audio for diarization (gated access/license); Demucs as a baseline only (upstream archived; assess alternatives); SeamlessM4T or NLLB for translation; XTTS-v2, Qwen3-TTS, and Chatterbox as TTS candidates requiring checkpoint/language/license verification. These are not final selections.
- Benchmark intelligibility, WER, diarization, translation adequacy, speaker similarity, naturalness, timing, background retention, runtime, and compute.

## Repository implementation checkpoint
Committed scaffold currently includes:
- FastAPI app with root, health, and capabilities endpoints.
- Pydantic settings configuration.
- Initial ASR/translation/TTS protocol contracts and base adapter abstraction.
- One pytest health/capabilities test module.
- React + TypeScript + Vite landing screen and frontend configuration.
- Backend GitHub Actions test workflow.
- Product/architecture/quality/security/handoff documentation.

This is only a starter scaffold. Upload, database persistence, FFmpeg processing, async jobs, actual model integrations, transcript/translation editing, consent-backed voice profiles, mixing, and export are not implemented. Backend tests and frontend build have not yet been run/verified at the time of this checkpoint.

## Next steps
1. Run backend tests and frontend production build; fix any issues and verify CI.
2. Implement Phase 1 media ingest: project/media persistence, secure upload, ffprobe validation, local storage abstraction, FFmpeg extraction, background job state, and tests.
3. Continue in roadmap order and update PROJECT_STATUS.md after each milestone.

## Working style
User prefers practical incremental implementation, clear status, and repository documentation that prevents assumptions. Do not ask the user to restate decisions captured here. Be candid about limitations and costs; prefer free/local options.