# BatchGrain

BatchGrain is a Python script that adds a grain effect to images in a batch. It uses the Python Imaging Library (PIL) and numpy to manipulate the images and add the grain effect.

## Requirements

- Python 3
- PIL
- numpy
- tqdm

You can install the required packages using pip:

```bash
pip install -r requirements.txt
```

## Usage

You can run the script from the command line with the following arguments:

- `-g` or `--grain`: Amount of grain (default: 0.01)
- `-i` or `--input`: Input directory path (default: current directory)
- `-o` or `--output`: Output directory path (default: ./output/)

Example:

```bash
python batchgrain.py -g 0.05 -i ./input_images/ -o ./output_images/
```

This will process all .jpg and .png images in the `input_images` directory, add a grain effect, and save the processed images in the `output_images` directory.

## Making the Script Executable and Globally Accessible

To make your Python script executable and callable from anywhere on the console in macOS, you can use the `chmod` command to change the file permissions and make it executable. Then, you can move it to the `/usr/local/bin` directory, which is included in the system's PATH by default.

Here are the steps:

1. Change the file permissions to make it executable:

```bash
chmod +x batchgrain.py
```

2. Move the script to the `/usr/local/bin` directory:

```bash
mv batchgrain.py /usr/local/bin/batchgrain
```

Now, you can call `batchgrain` from anywhere on the console. Note that you need to use the `.py` extension when running the script. If you want to run the script without the `.py` extension, you can rename the file when moving it:

```bash
mv batchgrain.py /usr/local/bin/batchgrain
```

This way, you can call the script with `batchgrain` from anywhere on the console.