
import hydra
from omegaconf import DictConfig
from {{ cookiecutter.project_slug }}.project import Project
from {{ cookiecutter.project_slug }}.util import get_logger

logger = get_logger()

@hydra.main(
    version_base="1.3", config_path=str(Project.configs_dir), config_name="train.yaml"
)
def main(cfg: DictConfig) -> None:
    logger.info("Hello World!")
    print(cfg)
    


if __name__ == "__main__":
    main()