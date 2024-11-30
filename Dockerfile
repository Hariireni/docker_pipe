# Use the official Python image as the base
FROM python:3.10-slim

# Set the working directory in the container
WORKDIR /app

# Copy the application files into the container
COPY calculator.py /app

# Install Flask
RUN pip install flask

# Expose the application port
EXPOSE 5000

# Run the application
CMD ["python", "calculator.py"]
