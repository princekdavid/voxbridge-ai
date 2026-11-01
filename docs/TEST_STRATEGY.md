# Test Strategy

## Test layers
- Unit: validation, domain rules, segment timing, state transitions, adapter contracts, path generation.
- API: project lifecycle, uploads, status codes, invalid inputs, authorization boundaries.
- Integration: storage + database + FFmpeg probe/extraction + job persistence.
- Model contract: adapter input/output shape, unavailable model handling, deterministic mocks.
- Evaluation: versioned datasets and offline metrics for ASR, diarization, translation, TTS, separation, and mixing.
- End-to-end: upload → analyze → edit → translate → assign authorized voice → dub → export.

## Required edge cases
Unsupported/empty/malformed files; spoofed MIME; huge duration; mono/stereo and varied sample rates; silent audio; no speech; overlapping speakers; one-word and long segments; non-speech vocalizations; mixed-language speech; translation expansion; TTS duration mismatch; missing model weights; GPU unavailable; worker crash/retry; disk full; interrupted export; consent absent/revoked.

## Test data
Use generated synthetic signals, public-domain/appropriately licensed media, or samples with documented consent. Do not commit user/private media or unlicensed voice recordings.

## Quality gates
Tests and builds must be run and recorded. Model quality thresholds are to be set only after baseline measurements. A successful HTTP response or mocked pipeline does not prove end-to-end dubbing quality.