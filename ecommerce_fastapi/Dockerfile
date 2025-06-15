#Use official lightweight Python image
FROM python:3.10-slim

#Set environment variables
ENV PYTHONDONTWRITEBYTECODE 1
ENV PYTHONUNBUFFERED 1

#Set working directory inside the container
WORKDIR /code

#Install dependencies
COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

#Copy the rest of the application code
COPY . .

#Exxpose port for FastAPI
EXPOSE 8000

#Run alembic upgrade head && uvicorn app.main:app --host 0.0.0.0 --port 8000
CMD ["sh", "-c", "alembic upgrade head && uvicorn app.main:app --host 0.0.0.0 --port 8000"]
