from pydantic_settings import BaseSettings, SettingsConfigDict


class Settings(BaseSettings):
    app_name: str = "Cinematic Agents"
    environment: str = "development"
    host: str = "0.0.0.0"
    port: int = 8080
    openai_api_key: str | None = None
    openai_model: str = "gpt-5.6"
    require_api_key: bool = False
    runtime_api_key: str | None = None
    max_scene_seconds: int = 8

    model_config = SettingsConfigDict(env_file=".env", env_prefix="CINEMATIC_", extra="ignore")


settings = Settings()
