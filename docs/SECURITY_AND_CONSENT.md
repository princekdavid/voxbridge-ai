# Security, Privacy, and Voice Consent

## Media handling
- Accept only configured media formats and verify actual file content using a media probe.
- Enforce upload size, duration, codec, and resource limits.
- Generate server-side storage names; never concatenate untrusted filenames into filesystem paths.
- Treat uploaded files as untrusted. Run FFmpeg with argument arrays (not shell interpolation), resource limits, and isolated working directories.
- Keep source assets immutable; store derived artifacts separately.
- Define retention, deletion, and backup policies before public deployment.
- Do not log media content, voice embeddings, credentials, or sensitive transcript content.

## Voice authorization
- Voice profile creation/use requires that the user owns the voice or has explicit permission from the speaker.
- Record consent status, scope, timestamp, and relevant provenance. Do not store unnecessary identity documents.
- Provide profile revocation/deletion and stop future synthesis when consent is withdrawn.
- Never design features for covert impersonation, bypassing consent, or misleading listeners about a real person's participation.
- Clearly label synthetic/dubbed output where appropriate and comply with applicable law and platform requirements.

## Secrets and dependencies
- Use environment variables or secret managers; commit only sanitized .env.example.
- Pin dependencies and scan licenses/security advisories.
- Review model code and checkpoints separately; model weights may have different terms from code.
- Do not add real voice samples, private media, tokens, or passwords to git.

## Threat model to revisit
Malicious media files, decompression/resource exhaustion, path traversal, unauthorized project access, leaked voice profiles, consent fraud, dependency/model supply-chain risk, and generated speech misuse.