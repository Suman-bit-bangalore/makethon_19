FROM python:3.9-slim

# Set the working directory in the container
WORKDIR /app

# Copy the requirements file into the container
COPY backend/requirements.txt .

# Install the dependencies
RUN pip install --no-cache-dir -r requirements.txt

# Copy the backend source code into the container
COPY backend/src ./src

# Expose the port the app runs on
EXPOSE 8080

# Command to run the application
CMD ["python", "src/app.py"]