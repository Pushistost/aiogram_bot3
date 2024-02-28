from dataclasses import dataclass

from environs import Env


@dataclass
class TgBot:
    token: str

    @classmethod
    def from_env(cls, env: Env) -> "TgBot":
        token = env.str("BOT_TOKEN")
        return cls(token=token)


@dataclass
class Config:
    tg_bot = TgBot


def load_config(path: str = ".env") -> Config:
    env = Env()
    env.read_env(path)

    return Config(
        tg_bot=TgBot.from_env(env)
    )
