FROM nvidia/cuda:12.8.0-devel-ubuntu24.04 AS builder
WORKDIR /src
COPY ./main.cu .
RUN nvcc -o main main.cu

# Use a runtime image that has the necessary CUDA runtime libraries.
FROM nvidia/cuda:12.8.0-runtime-ubuntu24.04
WORKDIR /src
COPY --from=builder /src/main .
VOLUME /data
ENTRYPOINT ["/src/main", "/data/test_data_input.txt", "/data/test_data_output.txt"]
