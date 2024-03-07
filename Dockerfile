# Use a lightweight Python image
FROM python:3.9-slim
EXPOSE 80
EXPOSE 443

# Set a working directory
WORKDIR /app

# Copy requirements.txt and install dependencies
COPY requirements.txt .
RUN pip install -r requirements.txt

# Copy your Flask app
COPY . .

# Set the command to run the app
CMD ["gunicorn", "app:app"]
