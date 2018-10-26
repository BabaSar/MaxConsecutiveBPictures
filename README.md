# MaxConsecutiveBPictures

We can make use of A/V's H264 parsing log and a script to read through this log. 
The parsing log includes a lot of very useful information, including the frame type and whether it is a field (top or bottom) 
for interlaced. This script will parse the output data, and determine the Maximum number of consecutive B Pictures by looking through all
GOPs.
