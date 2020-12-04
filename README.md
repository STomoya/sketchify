
# sketchify

Generating sketch images using XDoG and sketchKeras.

Motivated by the paper,

```
"Tag2Pix: Line Art Colorization Using Text Tag With SECat and Changing Loss",  
Hyunsu Kim, Ho Young Jhoo, Eunhyeok Park, Sungjoo Yoo,  
ICCV 2019
```

## Methods

- XDoG  
    [paper](https://www.sciencedirect.com/science/article/abs/pii/S009784931200043X)

- sketchKeras  
    [code](https://github.com/lllyasviel/sketchKeras) | [pytorch version](https://github.com/higumax/sketchKeras-pytorch)

[sketch simplification](https://github.com/bobbens/sketch_simplification) is not contained due to the LICENSE.

## Usage

- Clone repository and download sketchKeras weights.

    ```console
    git clone https://github.com/STomoya/sketchify.git
    cd sketchify
    sh setup.sh
    ```

- Build docker image.

    ```console
    docker-compose build
    ```

- Add `volumes` to `docker-compose.yml` to mount the images into the container.

- Generate sketch images by

    ```console
    docker-compose run --rm python python sketchify.py path/to/images/in/container
    ```

    The defaults will creat a folder named `data/xdog` and `data/sketchKeras` in the currect directory, which will be used to save XDoG, and sketchKeras images, repsectively.

    If you want to define the path to where the images are saved, then

    ```console
    docker-compose run --rm python python sketchify.py path/to/images/in/container \
        --xdog-folder path/to/xdog \
        --sk-folder path/to/sketchKeras
    ```

## Author

[STomoya](https://github.com/STomoya)
