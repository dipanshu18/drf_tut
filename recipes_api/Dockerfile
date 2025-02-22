FROM python:3.10-alpine
LABEL maintainer="github.com/dipanshu18"

ENV PYTHONBUFFERED=1

# Install uv package manager
RUN apk add curl ca-certificates
ADD https://astral.sh/uv/install.sh /uv-installer.sh
RUN sh /uv-installer.sh && rm /uv-installer.sh
ENV PATH="/root/.local/bin/:$PATH"

ARG DEV=false
WORKDIR /app

# Create virtual env
RUN uv venv /app/.venv
ENV PATH="/app/.venv/bin:$PATH"

COPY ./pyproject.toml /app/pyproject.toml
COPY . .
EXPOSE 8000

RUN uv sync --no-dev && \
if [$DEV = "true"]; \
then uv add --dev ruff; \
fi

CMD ["uv", "run", "python", "manage.py", "runserver", "0.0.0.0:8000"]
