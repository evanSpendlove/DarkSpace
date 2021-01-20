# Set base image (host OS)
FROM python:3.8

# Set the working directory in the container
WORKDIR /code

# Copy the required files into the working directory
COPY requirements.txt .
COPY timetable.csv .
COPY .env .
COPY darkspace.py .

# Install dependencies
RUN pip install -r requirements.txt

# Run darkspace bot on container start
CMD [ "python", "./darkspace.py" ]
