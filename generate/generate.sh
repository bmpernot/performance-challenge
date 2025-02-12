docker build -t proformance-challange/generator:1 ./generate
docker run --volume ./data:/data proformance-challange/generator:1