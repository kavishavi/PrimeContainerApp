# Use an official Python image as a base
FROM python:3.9

# Copy the Flask app files to the image
COPY . /app

# Install the requirements for the Flask app
RUN pip install -r /app/requirements.txt

# Set the working directory for the image
WORKDIR /app

# Set an environment variable for Flask
ENV FLASK_APP=app.py

# Expose the port for Flask
EXPOSE 5000

# Run the Flask app when the container starts
CMD ["flask", "run", "--host=0.0.0.0"]
