FROM python:3.11

WORKDIR /workspaces/tutorial-github-codespaces-poetry

# install python package
COPY ./pyproject.toml ./poetry.lock* ./
RUN pip install poetry \
    && poetry config virtualenvs.create false
RUN apt-get update && apt-get install -y lsof

COPY . /workspaces/tutorial-github-codespaces-poetry

RUN poetry install --no-root
CMD ["sleep", "infinity"]