
# Money-Detection

A demo using YOLOv8 for detecting 100 EGP & 200 EGP as part of a graduation project.

Contents

- runs/: Contains the results from the detection and training processes.
- config.yaml: Configuration file for the YOLOv8 model.
- test.py: Script to test the trained model.
- test_image.py: Script to test the model on a single image.
- train.py: Script to train the YOLOv8 model.

Requirements

- Python 3.x
- Required libraries: numpy, pandas, matplotlib, sklearn, torch, torchvision, PyYAML

Installation

1. Clone the repository:
    ```bash
    git clone https://github.com/John-Wassef/Money-Detection.git
    ```
2. Navigate to the repository directory:
    ```bash
    cd Money-Detection
    ```
Usage

- Training the Model:
    ```bash
    python train.py
    ```
- Testing the Model:
    ```bash
    python test.py
    ```
- Testing on a Single Image:
    ```bash
    python test_image.py --image path_to_image
    ```

Contributing

Feel free to fork the repository and submit pull requests. Contributions are welcome!
