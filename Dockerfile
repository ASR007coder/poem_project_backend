# Start from an official Python image
FROM python:3.11-slim

# Set the working directory inside the container
WORKDIR /app

# Copy the requirements file first and install libraries
# (Docker is smart and will cache this step)
COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

# Now copy the rest of your backend code into the container
COPY . .

# Tell Docker your app runs on port 8000
EXPOSE 8000

# The command to run your app when the container starts
CMD ["uvicorn", "main:app", "--host", "0.0.0.0", "--port", "8000"]