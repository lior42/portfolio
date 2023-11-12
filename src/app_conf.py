from pydantic_settings import BaseSettings, SettingsConfigDict
from pydantic import MongoDsn


class __AppConf(BaseSettings):
    model_config = SettingsConfigDict(
        env_file=".env", env_file_encoding="uft-8", env_prefix="LP"
    )

    db_url: MongoDsn = "mongodb://localhost:27017"
    db_name: str = "lior_portfolio"

    bind_ip: str = "127.0.0.1"
    port: int = 8000


app_conf = __AppConf()
