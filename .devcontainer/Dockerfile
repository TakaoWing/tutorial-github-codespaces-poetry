FROM python:3.11

WORKDIR /workspaces/tutorial-github-codespaces-poetry

# install python package
COPY ./pyproject.toml ./poetry.lock* ./
RUN pip install poetry \
    && poetry config virtualenvs.create false
RUN poetry install --no-root
CMD ["sleep", "infinity"]