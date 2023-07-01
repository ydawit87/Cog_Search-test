# Use an official Python runtime as a parent image
FROM python:3.10.6-slim-buster

# Set the working directory in the container to /app
WORKDIR /app

# Add the current directory contents into the container at /app
ADD . /app

# Install any needed packages specified in requirements.txt
RUN pip install --no-cache-dir -r requirements.txt

# Make port 5000 available to the world outside this container
EXPOSE 5000

# Set environment variables
#ENV SECRET_KEY=your-secret-key
#ENV COSMOS_DB_ENDPOINT=your-cosmos-db-endpoint
#ENV COSMOS_DB_KEY=your-cosmos-db-key
#ENV COSMOS_DB_DATABASE_NAME=your-cosmos-db-database-name
#ENV COSMOS_DB_CONTAINER_NAME=your-cosmos-db-container-name
ENV OPENAI_API_KEY=

# Run the application when the container launches
CMD ["flask", "run", "--host=0.0.0.0"]
