filename = "H264_Parsing.log"
 
GOP_list = [] #List of GOP structure as seen in log e.g I,P,B,I,P,B
B_Pictures_Positions = []
with open(filename) as file_object:
    for each_line in file_object:
        # print(f"\'{each_line.rstrip()}\',")
        if "FrameType[I]" in each_line:
            GOP_list.append("I")
            # print(f"\'{each_line.rstrip()}\',")
        elif "FrameType[P]" in each_line:
            GOP_list.append("P")
        elif "FrameType[B]" in each_line:
            if "Structure[TopField]" in each_line:
                GOP_list.append("B-TopField")
            elif "Structure[BottomField]" in each_line:
                GOP_list.append("B-BottomField")
            else:
                GOP_list.append("B")
#GOP row by row - This is purely for printing to the terminal so it can be viewed
GOP_in_rows = []
single_GOP = [] #stores a single GOP, which is then appended to the GOP_in_rows list
for i in range(len(GOP_list)):
    if i != (len(GOP_list) - 1):
        #Check if next Frame is I Frame or not
        if GOP_list[i+1] != "I":
            single_GOP.append(GOP_list[i])
        else:
            GOP_in_rows.append(single_GOP)
            single_GOP = []
    else:
        GOP_in_rows.append(single_GOP)
for i in range(len(GOP_in_rows)):
    print(f"GOP {i+1}: {GOP_in_rows[i]}")
B_frames = [] #indexes of all B frames
B_frames_fields = [] #indexes of all B-TopFields and B-BottomFields
 
for i in range(len(GOP_list)):
    if GOP_list[i] == "B":
        B_frames.append(i)
    if GOP_list[i] == "B-TopField" or GOP_list[i] == "B-BottomField":
        B_frames_fields.append(i)
#Count consecutive B Pictures (streak)
count_regular = 1
results_regular = []
for i in range(len(B_frames)):
    if i != (len(B_frames)-1):
        difference = B_frames[i+1] - B_frames[i]
        if difference == 1:
            count_regular += 1
        else:
            results_regular.append(count_regular)
            count_regular = 1
            # reset the count to 1
    else:
        results_regular.append(count_regular)
count_interlaced = 1
results_interlaced = [] #list of consecutive streaks
for i in range(len(B_frames_fields)):
    if i != (len(B_frames_fields)-1):
        diff = B_frames_fields[i+1] - B_frames_fields[i]
        if diff == 1:
            count_interlaced += 1
        else:
            results_interlaced.append(count_interlaced)
            count_interlaced = 1
            # reset the count to 1
    else:
        results_interlaced.append(count_interlaced)
if not results_interlaced:
    results_interlaced.append(0)
 
#divide by two since two fields make up one frame
###
results_interlaced_factor_2 = []
for i in range(len(results_interlaced)):
    results_interlaced_factor_2.append(int(results_interlaced[i]/2))
 
max_B = max(results_regular)
max_B_fields = max(results_interlaced_factor_2)
 
print(f"### The max number of consecutive B pictures is: {max(max_B, max_B_fields)} ###")
print("This results takes into account B Frames from both progressive and interlaced video")
