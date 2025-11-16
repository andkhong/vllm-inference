FROM python:3.13-slim-bookworm

# Install uv
RUN curl -fsSL https://astral.sh/uv/install.sh | bash

# Install any required Python packages (if you have a requirements.txt)
RUN uv pip install -r requirements.txt

# Get the secret from the secret manager
RUN export HUGGING_FACE_TOKEN=$(uv run python -c "from app.utils.secret_manager import get_secret; get_secret()")

# Set the secret as an environment variable
ENV HUGGING_FACE_TOKEN=$HUGGING_FACE_TOKEN

# Authorize the Hugging Face token
RUN uv run python -c "from huggingface_hub import login; login(token=os.getenv('HUGGING_FACE_TOKEN'))"

# Define the command to run your Python application
CMD ["uv", "run", "server.py"]