from dataclasses import dataclass
from typing import Any, Protocol


@dataclass(frozen=True)
class ModelMetadata:
    provider: str
    model_name: str
    checkpoint: str | None = None
    version: str | None = None
    license_id: str | None = None


class ASRAdapter(Protocol):
    metadata: ModelMetadata

    def transcribe(self, audio_path: str, language: str | None = None) -> list[dict[str, Any]]: ...


class TranslationAdapter(Protocol):
    metadata: ModelMetadata

    def translate(self, text: str, source_language: str, target_language: str) -> str: ...


class TTSAdapter(Protocol):
    metadata: ModelMetadata

    def synthesize(self, text: str, language: str, voice_profile_id: str) -> str: ...
