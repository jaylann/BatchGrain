#!/usr/bin/env python3
import argparse
import os
import logging
from PIL import Image
import numpy as np
from tqdm import tqdm

def add_grain(image_path, output_path, grain_level):
    """
    Adds grain effect to an image and saves it to the specified output path.
    :param image_path: Path to the input image.
    :param output_path: Path to save the grain-added image.
    :param grain_level: Level of grain to add to the image.
    """
    image = Image.open(image_path)
    image_array = np.array(image)

    # Adding noise
    noise = np.random.normal(loc=0, scale=grain_level * 255, size=image_array.shape)
    grainy_image_array = np.clip(image_array + noise, 0, 255).astype(np.uint8)

    # Convert array back to image
    grainy_image = Image.fromarray(grainy_image_array)
    grainy_image.save(output_path)


def setup_logging():
    """
    Sets up the logging configuration.
    """
    logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s')

def main():
    parser = argparse.ArgumentParser(description='Add grain effect to images in a batch.')
    parser.add_argument('-g', '--grain', type=float, default=0.01, help='Amount of grain (default: 0.01)')
    parser.add_argument('-i', '--input', type=str, default='./', help='Input directory path (default: current directory)')
    parser.add_argument('-o', '--output', type=str, default='./output/', help='Output directory path (default: ./output/)')

    args = parser.parse_args()
    setup_logging()

    logging.info(f"Starting batchgrain with input: {args.input}, output: {args.output}, grain: {args.grain}")

    if not os.path.exists(args.output):
        os.makedirs(args.output)

    image_files = [f for f in os.listdir(args.input) if f.endswith(('.jpg', '.png'))]
    for file_name in tqdm(image_files, desc="Processing images"):
        file_path = os.path.join(args.input, file_name)
        output_path = os.path.join(args.output, file_name)
        add_grain(file_path, output_path, args.grain)
    logging.info(f"Processed and saved {len(image_files)} images to {args.output}")

if __name__ == '__main__':
    main()
