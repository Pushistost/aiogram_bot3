from dataclasses import dataclass
from environs import Env


@dataclass
class TgBot:
    token: str
    users: list[int] = None
    error_chat_id: int = None

    @classmethod
    def from_env(cls, env: Env) -> "TgBot":
        token = env.str("BOT_TOKEN")
        users = env.list("USERS", subcast=int)
        error_chat_id = env.int("ERROR_CHAT_ID")
        return cls(token=token, users=users, error_chat_id=error_chat_id)


@dataclass
class Config:
    tg_bot: TgBot


def load_config(path: str = ".env") -> Config:

    env = Env()
    env.read_env(path)

    return Config(
        tg_bot=TgBot.from_env(env)
    )

