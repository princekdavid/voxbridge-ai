# Contributing

## Before changing code
Read README.md, AGENTS.md, PROJECT_STATUS.md, and the relevant product/architecture documents. Inspect the current branch and repository tree first.

## Development principles
- Keep changes small, testable, and aligned with the MVP.
- Prefer local/open-source tools, but verify exact model and dependency licenses.
- Keep model providers behind adapters.
- Never commit media, voice samples, credentials, generated large artifacts, or private data.
- Update docs and PROJECT_STATUS.md with every meaningful implementation milestone.

## Quality checklist
- Add tests for new behavior and failure paths.
- Run backend tests and frontend build where applicable.
- Report exact commands and outcomes.
- Document limitations and follow-up work.
- Do not mark roadmap items complete until implementation and verification are done.