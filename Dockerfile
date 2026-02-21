FROM python:3.12-slim

WORKDIR /app

COPY pyproject.toml uv.lock ./

RUN pip install uv
# RUN pip install uv \
#     && uv sync --frozen

COPY . .

EXPOSE 8000

CMD ["bash"]