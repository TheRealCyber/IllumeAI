# Use an official Python runtime as a parent image
FROM python:3.12

# Set the working directory in the container
WORKDIR /app

# Copy the current directory contents into the container at /app
COPY . .

# Install system dependencies 
RUN chmod +x ./build.sh && ./build.sh

# Install python dependencies

RUN pip3 install -r requirements.txt

# Expose port (your app's port)
EXPOSE 8000
EXPOSE 5000

# Command to run your app
CMD ["gunicorn", "app:app", "--log-level", "debug"]
#or
#CMD ["python", "app.py"]