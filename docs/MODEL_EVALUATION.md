# Model Evaluation Plan

Model names below are research candidates, not approved production dependencies. Check exact repository, checkpoint, language coverage, license, attribution, watermarking, and commercial-use terms before integration.

## Candidate categories
| Stage | Candidates to investigate | Notes |
|---|---|---|
| ASR | faster-whisper / Whisper | Benchmark English WER, punctuation, timestamps, speed, CPU/GPU. |
| Diarization | pyannote.audio | Check gated model access, license, speaker-count behavior, overlap handling. |
| Separation | Demucs baseline; evaluate maintained alternatives | Upstream Demucs repository is archived; separation can damage dialogue and ambience. |
| Translation | SeamlessM4T, NLLB-200 | Validate English→Hindi quality, context, terminology, and model license. |
| TTS | XTTS-v2, Qwen3-TTS, Chatterbox | Verify Hindi support for exact checkpoint, speaker conditioning, similarity, license, and any watermark obligations. |

## Known cautions
- XTTS-v2's Coqui Public Model License has restrictions; do not assume unrestricted commercial use.
- Qwen3-TTS language coverage may not include Hindi in the exact checkpoint/version being evaluated.
- Chatterbox checkpoint variants and terms must be checked individually.
- pyannote access may require accepting terms or gated access.
- Demucs should be treated as a baseline rather than assumed long-term dependency.
- No model is selected solely because a model card claims multilingual or voice-cloning capability.

## Benchmark protocol
Create a small consented/owned evaluation set with varied speakers, accents, speaking rates, emotion, noise, overlap, and segment lengths. Never use third-party voice samples without authorization.

Measure:
1. ASR: WER/CER, timestamp error, hallucination rate.
2. Diarization: DER, speaker confusion, missed/false speech, overlap handling.
3. Translation: adequacy, fluency, terminology consistency, human reviewer scores.
4. TTS: intelligibility, naturalness, speaker similarity, accent drift, prosody/emotion retention.
5. Timing: duration ratio, pause preservation, synchronization error.
6. Mixing: dialogue clarity, background retention, artifacts, loudness, clipping.
7. Operations: latency per media minute, peak RAM/VRAM, CPU/GPU support, reproducibility.

Record checkpoint hash/version, license URL and review date, hardware, settings, dataset version, metrics, known failure modes, and reviewer notes. Keep human evaluation in the loop; no single automatic speaker-similarity score proves identity preservation.