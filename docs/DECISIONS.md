# Architecture Decision Record (initial)

## ADR-001: Modular monolith first
**Decision:** Use FastAPI modular monolith with clear service and adapter boundaries.
**Reason:** Faster MVP iteration and simpler local deployment; split workers/services only when operational needs justify it.

## ADR-002: Local-first and cost-conscious
**Decision:** No mandatory paid hosted inference APIs for MVP.
**Reason:** User wants to avoid recurring paid API costs. Local compute constraints must be measured; optional providers can be adapters later.

## ADR-003: Both audio and video are first-class inputs
**Decision:** Support MP3/WAV and MP4/MOV in initial scope.
**Reason:** Product is a complete dubbing workflow, not only audio transcription.

## ADR-004: Voice identity is the core differentiator
**Decision:** Evaluate TTS on speaker similarity and expressive delivery, not just intelligibility.
**Clarification:** Preserve perceptual identity traits, not the original waveform.

## ADR-005: English-to-Hindi first
**Decision:** Optimize MVP for English source and Hindi target.
**Reason:** Narrow first language pair to reduce evaluation and UX complexity while keeping architecture language-agnostic.

## ADR-006: Human review before expensive synthesis
**Decision:** Transcript and translation are editable before dubbing.
**Reason:** Prevent upstream ASR/translation errors from contaminating generated output.

## ADR-007: Consent-backed voice profiles
**Decision:** Store explicit authorization/consent state and block unauthorized voice profile use.
**Reason:** Voice cloning can enable impersonation and requires ethical/legal safeguards.

## ADR-008: Preserve original audio and intermediate stems
**Decision:** Never destructively replace the source; keep source and derived stems separate.
**Reason:** Separation quality is imperfect and users need fallback/recovery.

## ADR-009: Model choices remain provisional
**Decision:** Use adapters and benchmark candidates before locking checkpoints.
**Reason:** Licensing, language coverage, hardware needs, and quality are checkpoint-specific.