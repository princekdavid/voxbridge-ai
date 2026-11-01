from pydantic_settings import BaseSettings, SettingsConfigDict


class Settings(BaseSettings):
    app_name: str = "VoxBridge AI"
    app_env: str = "development"
    storage_root: str = "./storage"
    max_upload_bytes: int = 524_288_000
    max_media_duration_seconds: int = 1800
    ffmpeg_binary: str = "ffmpeg"
    ffprobe_binary: str = "ffprobe"

    model_config = SettingsConfigDict(env_file=".env", extra="ignore")


settings = Settings()
