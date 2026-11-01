# Architecture

## Architectural style
Start as a modular monolith with explicit domain boundaries and adapter interfaces. Avoid premature microservices. The API process coordinates work; CPU/GPU-heavy operations execute as background jobs.

## Logical components
- **Frontend:** React + TypeScript; project creation, upload, analysis status, speaker assignment, transcript/translation editor, preview, export.
- **API:** FastAPI; project/media/analysis/transcript/translation/voice-profile/dub/job/export routes.
- **Domain:** projects, media assets, speakers, consent records, transcript segments, translations, voice profiles, jobs, outputs.
- **Orchestration:** typed pipeline stages and persisted job state; retries and idempotency.
- **Storage:** local filesystem adapter for development; object storage adapter later. Store metadata separately from media bytes.
- **Database:** PostgreSQL target; SQLite permitted for isolated local smoke tests if compatible.
- **Media:** FFmpeg/ffprobe for extraction, normalization, mixing, muxing, metadata.
- **AI adapters:** ASR, diarization, source separation, translation, TTS, alignment, quality evaluation.
- **Worker:** background job runner; queue technology selected when implementation needs justify it.

## Pipeline
Ingest → validate/probe → extract/normalize audio → optional dialogue/background separation → diarization + ASR/alignment → transcript review → context-aware translation → speaker/consent assignment → TTS → timing/prosody adjustment → mix dialogue with background → mux into video → quality checks → export.

Stages should persist artifacts and metadata. A failed downstream stage should not force repeating expensive upstream stages if inputs have not changed.

## Important audio distinction
Do not equate “vocals” with “dialogue.” Singing, laughter, gasps, and other vocal sounds may be part of the creative soundtrack. Separation models can introduce artifacts and cannot guarantee clean dialogue stems. Preserve the original and intermediate stems; allow bypass/manual correction and compare output before export.

## API contract (initial target)
- POST /api/v1/projects
- POST /api/v1/media/upload
- POST /api/v1/projects/{project_id}/analyze
- GET /api/v1/projects/{project_id}/speakers
- POST /api/v1/speakers/{speaker_id}/voice-profile
- GET/PUT /api/v1/projects/{project_id}/transcript
- PUT /api/v1/projects/{project_id}/translation
- POST /api/v1/projects/{project_id}/dub
- GET /api/v1/jobs/{job_id}
- GET /api/v1/projects/{project_id}/export

Long-running actions should normally return 202 with a job identifier. API specification is in docs/API_SPECIFICATION.md.

## Data and security
Use generated IDs; validate MIME type and actual media probe; enforce configurable file/duration limits; never trust filenames or paths from clients; isolate per-project storage; avoid logging media or voice samples; define deletion/retention behavior. Voice profiles require explicit authorization evidence/consent state. Secrets belong in environment/configuration, never committed.

## Extensibility
Adapters expose stable input/output contracts and report model name, checkpoint, version, license identifier, device, and processing settings. Domain models must not hard-code a single provider or model. Language and speaker counts are configuration/data, not scattered conditionals.

## Deployment evolution
Local developer setup first. Add containerized worker and queue once async processing is real. Cloud/object storage and multi-tenant security only after the local MVP pipeline is validated.