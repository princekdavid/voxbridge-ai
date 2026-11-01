# Instructions for AI coding agents and ChatGPT

This file is mandatory project guidance. Read it together with README.md, PRD.md, docs/MVP_SPECIFICATION.md, ARCHITECTURE.md, docs/DECISIONS.md, ROADMAP.md, and PROJECT_STATUS.md before making changes.

## Source of truth
The repository is authoritative. Conversation history is not. If a chat is new or temporary, reconstruct context from these documents and git history. Do not ask the user to repeat decisions already recorded here.

## Product invariants
- Build a complete AI dubbing workflow, not a generic text-to-speech demo.
- Audio and video input are both required product directions.
- Speaker voice identity preservation is the main differentiator.
- Preserve original soundtrack/background where possible; retain the original source and intermediate stems.
- Never equate vocals with dialogue.
- Voice cloning/profile creation requires the speaker's ownership or explicit authorization and documented consent state.
- No mandatory paid AI inference API for MVP; prefer local/open-source options subject to licensing and hardware feasibility.
- English-to-Hindi is the first target direction, not a permanent language limitation.
- Keep multiple-speaker support extensible even if first UX is optimized for 1–2 speakers.

## Engineering rules
- Inspect current code and git status before editing.
- Do not overwrite or delete user work without explicit approval.
- Keep modular monolith boundaries and adapter contracts.
- Use typed schemas, clear errors, structured logs, configuration via environment variables, and dependency injection where appropriate.
- Long-running media/AI operations must be asynchronous jobs, not blocking request handlers.
- Validate uploads by content/probe, not filename alone; protect against path traversal, oversized files, malformed media, and unsafe FFmpeg arguments.
- Persist model/checkpoint/version/license metadata for reproducibility.
- Add tests for happy path, invalid input, edge cases, and failure/retry behavior.
- Keep docs, API specs, roadmap, and PROJECT_STATUS.md synchronized with implementation.
- Avoid premature microservices, unnecessary abstractions, paid services, and speculative features.
- Do not add real user media, voice samples, credentials, tokens, or secrets to git.
- Pin dependencies appropriately and check licenses before adopting model checkpoints.

## Definition of done
A feature is done only when implementation, tests, docs, error handling, and observable behavior are complete. Run relevant tests/builds and report exact commands/results. If unable to run them, say so.

## Workflow for each task
1. Read current project status and relevant docs.
2. Inspect existing implementation and tests.
3. State a small plan internally; make focused changes.
4. Implement with tests.
5. Run checks.
6. Update docs and project status.
7. Summarize changed files, behavior, tests, limitations, and next task.

## ChatGPT continuation
For a new ChatGPT project, start with docs/CHATGPT_HANDOFF.md. Do not infer missing implementation. Continue from the next unchecked roadmap task.