FROM registry.dci.bt.com/mirror/golang:1.23 AS builder

WORKDIR /src

COPY go.mod ./
RUN go mod download

COPY . .

RUN CGO_ENABLED=0 go build -o app .

FROM scratch

WORKDIR /src

COPY --from=builder /src/app /src/app

# number can change depending on who well each of the programs do
ENTRYPOINT ["/src/app", "50000", "/data/test_data_input.txt"]