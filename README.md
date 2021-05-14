# H2OVerification
## Dataset Structure 

<pre>
.
├── h1
│   ├── 0
│   │   │── cam0
│   │   │   ├── rgb
│   │   │   ├── depth
│   │   │   ├── cam_pose
│   │   │   ├── hand_pose
│   │   │   ├── hand_pose_MANO
│   │   │   ├── obj_pose
│   │   │   ├── obj_pose_RT
│   │   │   ├── action_label (only in cam4)
│   │   │   ├── rgb256 (only in cam4)
│   │   │   ├── verb_label
│   │   │   └── cam_intrinsics.txt
│   │   ├── cam1
│   │   ├── cam2
│   │   ├── cam3
│   │   └── cam4
│   ├── 1
│   ├── 2
│   ├── 3
│   └── ...
├── h2
├── k1
├── k2
└── ...
</pre>

cam0 ~ cam3 are fixed cameras. cam4 is an head-mounted camera (egocentric view). <br>
train_sequences = ['subject1/h1', 'subject1/h2', 'subject1/k1', 'subject1/k2', 'subject1/o1', 'subject1/o2', 'subject2/h1', 'subject2/h2', 'subject2/k1', 
'subject2/k2', 'subject2/o1', 'subject2/o2', 'subject3/h1', 'subject3/h2', 'subject3/k1'] (subject 1,2,3) <br>
val_sequences = ['subject3/k2', 'subject3/o1', 'subject3/o2'] (subject 3)<br>
test_sequences  = ['subject4/h1', 'subject4/h2', 'subject4/k1', 'subject4/k2', 'subject4/o1', 'subject4/o2'] (subject4)<br>


### rgb
1280 * 720 resolution rgb images

### rgb256
455 * 256 resolution resized rgb images

### depth
1280 * 720 resolution depth images

### cam_pose
cam_to_world rotion matrix <br>

16 numbers, 4x4 camera matrix
### hand_pose
cam_to_hand <br>
1 (whether annotate or not, 0: not annotate 1: annotate) + 21 * 3 (x, y, z in order) + 1 + 21 * 3 (right hand) <br>
First 64 numbers belong to the left hand. Next 64 numbers belong to the right hand 
### hand_pose_MANO
1 (whether annotate or not, 0: not annotate 1: annotate) + 48 pose values + 10 shape values + 1 + 48 + 10 (right hand) <br>
First 59 numbers belong to the left hand. Next 59 numbers belong to the right hand 
### obj_pose
cam_to_obj <br>
1 (object class) + 21 * 3 (x, y, z in order) <br>
21 numbers : 1 center, 8 corners, 12 mid edge point. <br>
00. background (no object), 01. book, 02. espresso, 03. lotion, 04. spray, 05. milk, 06. cocoa, 07. chips, 08. capuccino

<img id="image_canv" src="obj_point_order.jpg" style="transform: rotate(270deg);"/>

### object_pose_RT
1 (object class) + 16 numbers, 4x4 camera matrix

### verb_label
00. background (no verb), 01. grab, 02. place, 03. open, 04. close, 05. pour, 06. take out, 07. put in, 08. apply, 09. read, 10. spray, 11. squeeze

### action_label
Combination of noun (object class) and verb (verb label). 
00. no verb + no object, 01. grab + no object, 02. place + no object, 03. open + no object, 04. close + no object, 05. pour, 06. take out + no object, 07. put in + no object, 08. apply + no object, 09. read + no object, 10. spray + no object, 11. squeeze + no object, 12. grab + book, 13. place + book, 14. open + book, ...

0 background
1 grab book
2 grab espresso
3 grab lotion
4 grab spray
5 grab milk
6 grab cocoa
7 grab chips
8 grab cappuccino
9 place book
10 place espresso
11 place lotion
12 place spray
13 place milk
14 place cocoa
15 place chips
16 place cappuccino
17 open lotion
18 open milk
19 open chips
20 close lotion
21 close milk
22 close chips
23 pour milk
24 take out espresso
25 take out cocoa
26 take out chips
27 take out cappuccino
28 put in espresso
29 put in cocoa
30 put in cappuccino
31 apply lotion
32 apply spray
33 read book
34 read espresso
35 spray spray
36 squeeze lotion

### cam_instrinsics.txt
six numbers : fx, fy, cx, cy, width, height