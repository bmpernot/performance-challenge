docker build -t performance-challenge/generator:1 ./generate
docker run --volume ./generate/data:/data performance-challenge/generator:1