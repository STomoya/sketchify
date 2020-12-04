
import os
import glob

from XDoG.XDoG import gen_xdog_image
from sketchKeras.sketchKeras import gen_sketchkeras_image
from tqdm import tqdm

def get_args():
    import argparse
    parser = argparse.ArgumentParser()

    parser.add_argument('--dataset', '-d', required=True, type=str, help='The path to the images')
    parser.add_argument('--xdog-folder', default='data/xdog', type=str, help='Folder for saving XDoG images')
    parser.add_argument('--sk-folder', default='data/sketchKeras', type=str, help='Folder for saving sketchKeras images')

    return parser.parse_args()

def gen_sketch_single(filename, args):
    xdog_dst = os.path.join(args.xdog_folder, os.path.basename(filename))
    sk_dst   = os.path.join(args.sk_folder, os.path.basename(filename))
    gen_xdog_image(filename, xdog_dst)
    gen_sketchkeras_image(filename, sk_dst)

def gen_sketch(args):
    if not os.path.exists(args.xdog_folder):
        os.makedirs(args.xdog_folder)
    if not os.path.exists(args.sk_folder):
        os.makedirs(args.sk_folder)

    suffixes = ('*.png', '*.jpg', '*.JPEG', '*.jpeg')
    images = []
    for suffix in suffixes:
        images.extend(glob.glob(os.path.join(args.dataset, suffix)))
        images.extend(glob.glob(os.path.join(args.dataset, '**', suffix)))
    for image in tqdm(images):
        gen_sketch_single(image, args)

if __name__ == "__main__":
    args = get_args()
    gen_sketch(args)