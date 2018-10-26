# MaxConsecutiveBPictures

This script will calculate the maximum number of consecutive B Pictures. First, using ffprobe:

ffprobe -show_frames input.ts | grep pict_type > ffprobe_output.txt

With the output file containing all the information we need, a script can be used to perform the calculation.
