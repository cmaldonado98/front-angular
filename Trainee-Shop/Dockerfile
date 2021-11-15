FROM node:14.18.1 as builder
WORKDIR /usr/src/app
COPY package.json package-lock.json ./
RUN npm install
RUN npm install --save @types/chart.js
COPY . .
RUN npm run build --prod


FROM nginx:latest
COPY --from=builder /usr/src/app/dist/Trainee-Shop/ /usr/share/nginx/html
