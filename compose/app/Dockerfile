# Base image
FROM node:18

# Create app directory
WORKDIR /app

# Copy app files
COPY . .

# Install dependencies
RUN npm install && npm cache clean --force && npm install -g pnpm
RUN yarn install -g
RUN yarn install

# Expose ports
EXPOSE 3000

# Set environment variables
ENV NODE_ENV=dev

RUN pnpm run build

# Start the app
CMD ["pnpm", "run", "start"]
