#Python image
FROM python:3.12

# Node.js and npm installation and building Tainwind css
RUN apt-get update && apt-get install -y nodejs npm && rm -rf /var/lib/apt/lists/*

# working directory
WORKDIR /app

# installing dependencies
COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

# copy rest of project files
COPY . .

# Installing node.js dependencies
RUN npm install && npx tailwindcss -i ./website/static/src/input.css -o ./website/static/dict/css/output.css --minify

# Expose port 5000 for flask
EXPOSE 5000

# Run the flask app
CMD ["python", "index.py"]