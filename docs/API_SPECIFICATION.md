# Initial API Specification

Version prefix: /api/v1. Exact request/response schemas will be refined with implementation and kept synchronized with OpenAPI.

| Method | Route | Purpose |
|---|---|---|
| POST | /projects | Create project |
| POST | /media/upload | Upload media to a project |
| POST | /projects/{project_id}/analyze | Queue media analysis |
| GET | /projects/{project_id}/speakers | List detected speakers |
| POST | /speakers/{speaker_id}/voice-profile | Create/register authorized voice profile |
| GET | /projects/{project_id}/transcript | Fetch transcript segments |
| PUT | /projects/{project_id}/transcript | Update transcript segments |
| PUT | /projects/{project_id}/translation | Update target-language segments |
| POST | /projects/{project_id}/dub | Queue dubbing job |
| GET | /jobs/{job_id} | Read job state/progress/errors |
| GET | /projects/{project_id}/export | List/download export |

## API behavior
- Long-running analyze/dub requests return HTTP 202 and a job ID.
- Use stable IDs for project, asset, speaker, segment, profile, job, and export.
- Validate ownership/authorization and project state at each operation.
- Use structured error responses with stable error codes.
- Upload endpoint must enforce configured limits, inspect content, and use safe generated storage names.
- Do not return local filesystem paths or expose internal model secrets.
- Job status should persist beyond API process lifetime.
- Define pagination for large transcript/speaker/export collections when needed.

## Initial job states
queued → running → succeeded | failed | cancelled
Optional progress percentage and current stage. Retries must be idempotent and preserve prior artifacts.