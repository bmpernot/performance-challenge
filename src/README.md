# Your Code goes in this directory :)

## Useful commands:
### All command are run from base directory

``` docker build --tag performance-challenge/your_name:version_number ./src```

``` docker run -v ./generate/data:/data performance-challenge/your_name:version_number```

```./generate/generate.sh``` - this is required for benchmark - depending on how good your application is we can increase the size of the file

```./benchmark/timer.sh``` - you will need to update the timer script to run your docker image - this will be used to get an accurate time of how long it takes your program to process the file

```./test/test.sh``` - you will need to update the test script to run your docker image - used to verify your program works

## Notes:

Please make notes of any techniques that you make use of in your program as we hope to present anything to the group as a learning exercise while we test the code as it will take a while (probably) :)
