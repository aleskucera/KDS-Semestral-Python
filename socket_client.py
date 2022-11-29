import logging

import hydra
from omegaconf import DictConfig

from client import Client

log = logging.getLogger(__name__)


@hydra.main(version_base=None, config_path="conf", config_name="config")
def client_program(cfg: DictConfig):
    client = Client()
    client.connect(cfg.server.host, cfg.server.port)
    client.send(b'Hello, world')
    client.close()


if __name__ == '__main__':
    client_program()
