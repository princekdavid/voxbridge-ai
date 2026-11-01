# MVP Specification (v0.1)

## Outcome
A user can upload an English audio/video clip, review detected speakers and transcript, edit Hindi translation, assign authorized voice profiles, generate dubbed speech, retain background soundtrack as far as feasible, and export the result.

## Inputs and limits
- Audio: MP3, WAV.
- Video: MP4, MOV.
- Source language: English initially.
- Target language: Hindi initially.
- Speakers: optimize initial experience for 1–2; data model and orchestration must support more.
- File size and duration limits must be configurable, not hard-coded across the codebase.

## User-visible workflow
1. New project.
2. Upload and show filename, duration, sample rate, channels, media type, and validation status.
3. Analyze; show job progress and errors.
4. Review speakers and timestamped transcript; edit text and segment boundaries.
5. Review/edit Hindi translation with source context.
6. Create/select a voice profile for each speaker only after authorization/consent confirmation.
7. Generate a preview per segment/speaker; regenerate selected segments.
8. Review full mix and compare to original.
9. Export WAV/MP3 audio or MP4 video.

## Required capabilities
- Resumable/retryable job states where practical.
- Store immutable source asset and generated intermediates separately.
- Keep segment IDs stable across transcript edits where possible.
- Store source and translated text, timing, speaker assignment, confidence, and provenance.
- Record selected ASR/translation/TTS/separation checkpoints and configuration.
- Provide fallback if separation or synthesis fails; do not silently discard original audio.
- Preview and export must use the same persisted job artifacts.

## Acceptance criteria
- Reject unsupported, empty, malformed, and over-limit uploads with clear errors.
- Correctly probe supported sample files and extract audio from video.
- Analysis returns timestamped segments and speaker assignments, with uncertainty represented.
- User can edit transcript and translation before synthesis.
- Voice profile workflow blocks use until consent/authorization is recorded.
- Generated target speech is associated with correct speaker and segment.
- Mix/export retains source video and background audio as configured, with known limitations communicated.
- Job status survives API process restart.
- Automated tests cover validation, state transitions, storage, and core orchestration.
- No feature is declared complete without reproducible test evidence.

## Not required for v0.1
Lip-sync, voice marketplace, social collaboration, live calls, mobile apps, cloud multi-tenancy, custom model training, arbitrary language pairs, and automatic perfection of source separation.