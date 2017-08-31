# temp_http

This is a service which listens on http using Python's SimpleHTTPServer, 
for a set amount of time (configurable via the HTTP_TIMEOUT variable).

After this, it halts the server and just sleeps.

It is meant to be used to emulate a service 'dying' inside a docker container, without its PID-1 dying.
Practical examples of this include GC-looping and certain critical dependencies of the container going down.
It is intended to be used to test your healthchecking setup.
