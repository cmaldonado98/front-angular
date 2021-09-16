FROM node:14.17 as builder

ARG WORK_DIR=/Front-Angular
ENV PATH ${WORK_DIR}/node_modules/.bin:$PATH

RUN mkdir ${WORK_DIR}
WORKDIR ${WORK_DIR}

COPY package.json ${WORK_DIR}
COPY package-lock.json ${WORK_DIR}

RUN npm install -g @angular/cli@12.2.4
RUN npm install
RUN npm install @angular/animations --save
RUN npm install primeng --save
RUN npm install chart.js --save
RUN npm install --save @types/chart.js

COPY . ${WORK_DIR}

EXPOSE 4200

CMD ng serve
