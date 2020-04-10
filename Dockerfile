# Use the official image as parent image
FROM python:3

# Set working directory
WORKDIR .

# Add requirements.txt to working directory
COPY requirements.txt .

# Install dependencies
RUN pip install -r requirements.txt

# Inform Docker that the container is listening on the specified port at runtime.
EXPOSE 8080

# Copy the rest of your app's source code from your host to your image filesystem.
COPY . .

# Start up server
CMD python3 manage.py runserver 0.0.0.0:8000