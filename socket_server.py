import logging

import hydra
from omegaconf import DictConfig

from server import Server

log = logging.getLogger(__name__)


@hydra.main(version_base=None, config_path="conf", config_name="config")
def server_program(cfg: DictConfig):
    server = Server(cfg.server.host, cfg.server.port)
    server.start()
    server.close()


if __name__ == '__main__':
    server_program()
