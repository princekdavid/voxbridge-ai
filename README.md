# VoxBridge AI

**Universal multilingual AI dubbing platform with speaker voice-identity preservation.**

VoxBridge AI accepts audio and video, transcribes speech, translates it, generates dubbed speech that preserves an authorized speaker's vocal identity, and exports a mixed audio/video result while retaining music, ambience, and sound effects where possible.

> **Project status:** Foundation and product definition stage. The repository is the source of truth for scope, decisions, progress, and handoffs. Do not assume a feature is implemented merely because it appears in the roadmap.

## Start here

1. [Product requirements](PRD.md)
2. [MVP specification](docs/MVP_SPECIFICATION.md)
3. [Architecture](ARCHITECTURE.md)
4. [Technical decisions](docs/DECISIONS.md)
5. [Model evaluation and licensing](docs/MODEL_EVALUATION.md)
6. [Roadmap](ROADMAP.md)
7. [Current project status](PROJECT_STATUS.md)
8. [Instructions for AI contributors](AGENTS.md)
9. [New ChatGPT project handoff](docs/CHATGPT_HANDOFF.md)

## Product principles

- Preserve speaker identity, not merely convert text to speech.
- Support both audio-only and video inputs.
- Separate dialogue from non-dialogue audio where feasible; never assume vocals are always dialogue.
- Make transcripts and translations editable before dubbing.
- Support multiple speakers and per-speaker authorized voice profiles.
- Prefer local-first, open-source components and avoid mandatory paid inference APIs in the MVP.
- Track model/checkpoint licenses, attribution, consent, and commercial-use constraints before adoption.
- Keep components replaceable behind stable interfaces.
- Measure quality; do not claim human-level or perfect preservation.

## Initial MVP

- Input: MP3, WAV, MP4, MOV.
- Initial language direction: English to Hindi.
- Initial speaker range: one or two speakers, with extensible multi-speaker data structures.
- Editable transcript and translation.
- Voice profiles only for voices the user owns or is explicitly authorized to use.
- Dialogue replacement with retained accompaniment/ambience where technically possible.
- Export: WAV, MP3, MP4.
- Excluded initially: lip-sync/face animation, real-time dubbing, production cloud deployment, broad language coverage, and guaranteed perfect source separation.

## Development

The initial technical direction is a modular monolith: FastAPI backend, React + TypeScript frontend, PostgreSQL as the intended persistent database (SQLite may be used for local tests), file storage abstraction, background jobs, FFmpeg media processing, and adapter interfaces for AI models.

See [CONTRIBUTING.md](CONTRIBUTING.md). Every implementation change must update [PROJECT_STATUS.md](PROJECT_STATUS.md) and relevant decision/roadmap docs.