FROM nginx:alpine

# Copy website files
COPY index.html /usr/share/nginx/html/
COPY logo.jpg /usr/share/nginx/html/
COPY team.jpg /usr/share/nginx/html/
COPY reception.jpg /usr/share/nginx/html/
COPY reception2.jpg /usr/share/nginx/html/
COPY salle-attente.jpg /usr/share/nginx/html/
COPY salle-soins.jpg /usr/share/nginx/html/
COPY nginx.conf /etc/nginx/conf.d/default.conf

EXPOSE 80

HEALTHCHECK --interval=30s --timeout=3s --start-period=5s --retries=3 \
  CMD wget -qO- http://localhost/ || exit 1
