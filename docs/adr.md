# ADR

- Although text/plain would be efficient in therms of data transfer and storage, I've decided to use application/json as
  the content type for the API responses. This is because it is more readable and easier to parse. Also, it is more
  flexible in terms of future changes.
- As python documentation
  states, [http.server](https://docs.python.org/3.9/library/http.server.html#http.server.HTTPServer) is
  not safe to use in production thus considering to switch to an [Uvicorn](https://www.uvicorn.org/) webserver.