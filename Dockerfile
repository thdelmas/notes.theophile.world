# Stage 1
FROM alpine:latest AS build

# Install the Hugo go app.

RUN apk add --update hugo git npm

# Stage 2
FROM build

# Set workdir to the NGINX default dir.
WORKDIR /srv/Notes

# Copy HTML from previous build into the Workdir.
COPY . .

EXPOSE 1313

ENTRYPOINT ["./run.sh"]
