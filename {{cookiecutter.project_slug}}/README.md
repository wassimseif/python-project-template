{% set is_open_source = cookiecutter.open_source_license != 'Not open source' -%}

## {{ cookiecutter.project_name }}

## Description
{{ cookiecutter.project_short_description }}

## Getting Started

To set up your local development environment, please use a fresh virtual environment.

Then run:

```python
pip install -r requirements.txt -r requirements-dev.txt
```

