# Use the Alpine-based Node.js image
FROM node:14-alpine

# Set the working directory in the container
WORKDIR /app

# Copy the entire Docker context (including your Node.js application code) into the container
COPY . /app

# Install application dependencies
RUN npm install

# Define the command to start your Node.js application
CMD ["node", "app.js"]
