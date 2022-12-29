from dynaconf import Dynaconf


def read_secrets_from_config():
    return Dynaconf(envvar_prefix="", settings_files=["config/app/config.yaml"])
