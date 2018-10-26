#This reads output of ffprobe
filename = "ffprobe_output.txt"  # manually edit the filename here to the correct ffprobe output file
 
GOP_list = []  # List of GOP structure as seen in log e.g I,P,B,I,P,B
 
with open(filename) as file_object:
    for each_line in file_object:
        if "=I" in each_line:
            GOP_list.append("I")
        elif "=P" in each_line:
            GOP_list.append("P")
        elif "=B" in each_line:
            GOP_list.append("B")
 
B_frame_positions = []
 
for i in range(len(GOP_list)):
    if GOP_list[i] == "B":
        B_frame_positions.append(i)
 
streak_count = []
counter = 1
for i in range(len(B_frame_positions)):
    if i != (len(B_frame_positions) - 1):
        diff = B_frame_positions[i+1] - B_frame_positions[i]
        if diff == 1:
            counter += 1
        else:
            streak_count.append(counter)
            counter = 1
    else:
        streak_count.append(counter)
 
print(f"Max number of B pictures: {max(streak_count)}")
