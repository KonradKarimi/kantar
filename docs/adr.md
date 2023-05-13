# Architecture Decision Record

- Although text/plain would be efficient in therms of data transfer and storage, I've decided to use application/json as
  the content type for the API responses. This is because it is more readable and easier to parse. Also, it is more
  flexible in terms of future changes.
- As python documentation
  states, [http.server](https://docs.python.org/3.9/library/http.server.html#http.server.HTTPServer) is
  not safe to use in production thus considering to switch to an [Uvicorn](https://www.uvicorn.org/) webserver.
- Decided to expose `GET` and `POST` methods for the endpoints `/sort` and `/reverse`. This is because `GET` is idempotent and
  `POST` is not. Also, `POST` is more flexible in terms of future changes. `POST` has ability to send a body with the
  request.
- There was no need to implement any other methods for the endpoints. `PUT` and `DELETE` are not needed as there is no
  need to update or delete any data. `PATCH` is not needed as well as there is no need to partially update any data.
