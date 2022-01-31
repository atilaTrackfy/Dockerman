# Dockerman
Learning a bit of Docker and Openshift

Currently, the docker image will run the server.py script, which is nothing more than a Flask web app that receives http POST requests and return the message received back to the client. The client.py script sends a dummy POST message, and python.nix is a basic nix-shell derivation for those whom, like me, use the nix package manager for their reproducibility needs.
