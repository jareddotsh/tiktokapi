# Use an official Python runtime as a parent image
#FROM python:3.9
FROM mcr.microsoft.com/playwright:v1.40.0-jammy

#FROM mcr.microsoft.com/playwright:focal

# Set the working directory to /app
WORKDIR /app

# Copy the current directory contents into the container at /app
COPY . /app

RUN apt-get update && apt-get install -y python3-pip
# Install any needed packages specified in requirements.txt
RUN pip install --no-cache-dir -r requirements.txt
RUN python3 -m playwright install

# Make port 5000 available to the world outside this container
EXPOSE 5000

# Define environment variable
ENV FLASK_APP=app.py

# Use Gunicorn to run the application
CMD ["gunicorn", "-w", "4", "-b", "0.0.0.0:5000", "app:app"]
