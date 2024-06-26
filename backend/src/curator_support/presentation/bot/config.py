from dataclasses import dataclass

import toml

from curator_support.config import DbConfig, RedisConfig


@dataclass(frozen=True)
class BotConfig:
    token: str
    curator_auth_key: str
    db: DbConfig
    redis: RedisConfig


def load_bot_config(config_path: str) -> BotConfig:
    """Load configuration from a TOML file.

    Returns:
        Config: An instance of the Config class containing the loaded configuration.
    """
    with open(config_path, "r") as config_file:
        data = toml.load(config_file)
    return BotConfig(
        **data["bot"],
        db=DbConfig(**data["db"]),
        redis=RedisConfig(**data["redis"])
    )
