
import hydra
from omegaconf import DictConfig
from {{ cookiecutter.project_slug }}.project import Project

@hydra.main(
    version_base="1.3", config_path=Project.configs_dir, config_name="train.yaml"
)
def main(cfg: DictConfig) -> None:
    print(cfg.pretty())
    


if __name__ == "__main__":
    main()