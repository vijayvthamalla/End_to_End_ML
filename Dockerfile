# Start with a base Python image
FROM python:3.8

# Set the working directory inside the container
WORKDIR /app

# Copy the requirements file into the image
COPY ./requirements.txt /app/requirements.txt

# Install the dependencies
RUN pip install -r requirements.txt

# Copy the Flask application code into the image
COPY . /app

# Set the WSGI entry point file
ENV FLASK_APP=app:app

# Expose the port your Flask application will listen on
EXPOSE 5000

# Start the Flask application using Gunicorn
CMD ["gunicorn", "--bind", "0.0.0.0:5000", "app:app"]