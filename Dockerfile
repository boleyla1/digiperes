# syntax=docker/dockerfile:1

FROM node:18-alpine
WORKDIR /app
COPY . .
#RUN pip install --no-cache-dir -r requirements.txt
ENV PYTHONUNBUFFERED 1
CMD ["python", "manage.py", "runserver", "0.0.0.0:3000"]
EXPOSE 3000