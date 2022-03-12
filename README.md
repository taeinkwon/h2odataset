# H2O Dataset information

## News

**12/Mar./2022**: Visualization code is pusblished. https://github.com/taeinkwon/h2oplayer <br>
**11/Mar./2022**: Updated new labels to the existing files. <br>
**8/Dec./2021**: Please Download new labels "manolabel.tar.gz" in https://h2odataset.ethz.ch for mano parameters. We will also update existing files soon. <br>

# Visualization code (H2OPlayer)
https://github.com/taeinkwon/h2oplayer

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
1 (whether annotate or not, 0: not annotate 1: annotate) + 3 translation values + 48 pose values + 10 shape values + 1 + 3 + 48 + 10 (right hand) <br>
First 59 numbers belong to the left hand. Next 59 numbers belong to the right hand 
### obj_pose
cam_to_obj <br>
1 (object class) + 21 * 3 (x, y, z in order) <br>
21 numbers : 1 center, 8 corners, 12 mid edge point. <br>
0 background (no object) <br>
1 book <br>
2 espresso <br>
3 lotion <br>
4 spray <br>
5 milk <br>
6 cocoa <br>
7 chips <br>
8 capuccino <br>

<img id="image_canv" src="obj_point_order.jpg"/>

### object_pose_RT
1 (object class) + 16 numbers, 4x4 camera matrix

### verb_label
0 background (no verb) <br>
1 grab <br>
2 place <br>
3 open <br>
4 close <br>
5 pour <br>
6 take out <br>
7 put in <br>
8 apply <br>
9 read <br>
10 spray <br>
11 squeeze <br>

### action_label
Combination of noun (object class) and verb (verb label). 

0 background <br>
1 grab book <br>
2 grab espresso <br>
3 grab lotion <br>
4 grab spray <br>
5 grab milk <br>
6 grab cocoa <br>
7 grab chips <br>
8 grab cappuccino <br>
9 place book <br>
10 place espresso <br>
11 place lotion <br>
12 place spray <br>
13 place milk <br>
14 place cocoa <br>
15 place chips <br>
16 place cappuccino <br>
17 open lotion <br>
18 open milk <br>
19 open chips <br>
20 close lotion <br>
21 close milk <br>
22 close chips <br>
23 pour milk <br>
24 take out espresso <br>
25 take out cocoa <br>
26 take out chips <br>
27 take out cappuccino <br>
28 put in espresso <br>
29 put in cocoa <br>
30 put in cappuccino <br>
31 apply lotion <br>
32 apply spray <br>
33 read book <br>
34 read espresso <br>
35 spray spray <br>
36 squeeze lotion <br>

## For Actions
[Train set file](action_labels/action_train.txt) <br>
[Validation set file](action_labels/action_val.txt) <br>
[Test set file](action_labels/action_test.txt) <br>

## For Poses
[Train set file](pose_lists/pose_test.txt) <br>
[Validation set file](pose_lists/pose_train.txt) <br>
[Test set file](pose_lists/pose_test.txt) <br>

### cam_instrinsics.txt
six numbers : fx, fy, cx, cy, width, height

# Citations
If you find any usefulness of this datset, please consider citing:
```
@InProceedings{Kwon_2021_ICCV,
    author    = {Kwon, Taein and Tekin, Bugra and St\"uhmer, Jan and Bogo, Federica and Pollefeys, Marc},
    title     = {H2O: Two Hands Manipulating Objects for First Person Interaction Recognition},
    booktitle = {Proceedings of the IEEE/CVF International Conference on Computer Vision (ICCV)},
    month     = {October},
    year      = {2021},
    pages     = {10138-10148}
}
```
