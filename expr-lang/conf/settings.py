from pydantic_settings import BaseSettings


class Settings(BaseSettings):
    project_name: str = "expr-lang"
    debug: bool = False
