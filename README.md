# GCE Demo Web App

This is a small demo app that can be containerized and deployed to Google
Compute Engine.

## Run the app locally

Get the repo:

```bash
git clone https://github.com/stew-r/gce-demo-web-app.git`
```

Navigate to the directory:

```bash
cd gce-demo-web-app
```

Run the app:

```bash
sh cmd/run.sh
```

Send a request to the app:

```bash
curl localhost:80
```

## Build and the host image on Docker Hub

Build the image:

```bash
docker build -t gce-demo-web-app-image .
```

Get the image ID:

```bash
docker images
```

Tag the image:

```bash
docker tag <image_id> stewblr/gce-demo-web-app-image:<version>
```

Push the image:

```bash
docker push stewblr/gce-demo-web-app-image:<version>
```

## Create a GCE VM instance from the image

Follow [these instructions](https://cloud.google.com/compute/docs/containers/deploying-containers#deploying_a_container_on_a_new_vm_instance)
and, under Container image, specify `registry.hub.docker.com/stewblr/gce-demo-web-app-image
`.