from abc import ABC, abstractmethod
from app.core.contracts import ModelMetadata


class BaseModelAdapter(ABC):
    metadata: ModelMetadata

    @abstractmethod
    def is_available(self) -> bool:
        """Return whether the configured model/checkpoint can be used."""
