import splitfolders
import os

root_dir = '.'
input_path = root_dir
output_path = root_dir

splitfolders.ratio(input_path, output= output_path, seed=1337, ratio = (0.8, 0.1, 0.1))
