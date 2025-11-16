FROM python:3.13-slim-bookworm

# Set the working directory inside the container
WORKDIR /app

# Copy your application code into the container
COPY . /app

# Install any required Python packages (if you have a requirements.txt)
RUN uv pip install -r requirements.txt

# Define the command to run your Python application
CMD ["python", "server.py"]