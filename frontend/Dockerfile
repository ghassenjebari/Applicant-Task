FROM node:16-alpine

WORKDIR /usr/src/app
ENV PATH /usr/src/app/node_modules/.bin:$PATH

# Copy installation files before hand to improve docker caching
COPY package.json /usr/src/app/package.json
COPY yarn.lock /usr/src/app/yarn.lock
RUN yarn install --immutable

# Copy the rest of the files
COPY . /usr/src/app/
RUN yarn build

ENV NEXT_TELEMETRY_DISABLED=1
EXPOSE 3000

# Run the dev server
CMD [ "yarn", "dev" ]