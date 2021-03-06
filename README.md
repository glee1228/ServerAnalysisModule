# ServerAnalysisModule

#### 설치 설명
* python 3.6
* torch 1.5
* torchvision 0.6.0

- Clone the repository  
 ``git clone https://https://github.com/glee1228/ServerAnalysisModule.git``
 
- Install the required packages  
 ```
pip install opencv-python
apt-get install -y libsm6 libxext6 libxrender-dev
pip3 install ffmpeg-python
apt-get install -y ffmpeg
```

 ``pip install -r requirements.txt``
- Weight files are uploaded to the repository(folder `./weights`)
  - For Downloading the official pre-trained weights from 
  [https://github.com/leoxiaobin/deep-high-resolution-net.pytorch](https://github.com/leoxiaobin/deep-high-resolution-net.pytorch)  
    Direct links ([official Drive folder](https://drive.google.com/drive/folders/1hOTihvbyIxsm5ygDpbUuJ7O_tzv4oXjC), [official OneDrive folder](https://1drv.ms/f/s!AhIXJn_J-blW231MH2krnmLq5kkQ)):
    - COCO w48 384x288 (more accurate, but slower) - Used as default in `live_demo.py` and the other scripts  
      [pose_hrnet_w48_384x288.pth](https://drive.google.com/open?id=1UoJhTtjHNByZSm96W3yFTfU5upJnsKiS)
    - COCO w32 256x192 (less accurate, but faster)  
      [pose_hrnet_w32_256x192.pth](https://drive.google.com/open?id=1zYC7go9EV0XaSlSBjMaiyE_4TcHc_S38)
    - MPII w32 256x256 (MPII human joints)  
      [pose_hrnet_w32_256x256.pth](https://drive.google.com/open?id=1_wn2ifmoQprBrFvUCDedjPON4Y6jsN-v)

  Remember to set the parameters of SimpleHRNet accordingly.
- For multi-person support: FasterRCNN (obstacle detection)
    - Install FasterRCNN required packages (Included in above requirements.txt)
    
    - Weight files are uploaded to the repository(folder `./models/detectors/FasterRCNN/checkpoints`)
    
    - Build `Non Maximum Suppression` and `ROI Align` modules (modified from [facebookresearch/maskrcnn-benchmark](https://github.com/facebookresearch/maskrcnn-benchmark))
    
    1. Install(`from folder ./models/detectors/FasterRCNN`)

     ```
     $ python support/setup.py develop
     ```

    2. Uninstall

     ```
     $ python support/setup.py develop --uninstall
     ```

    3. Test

     ```
     $ python test/nms/test_nms.py
     ```

     * Result

       ![](models/detectors/FasterRCNN/images/test_nms.png?raw=true)
       
     * more details
     
     [potterhsu/easy-faster-rcnn.pytorch](https://github.com/potterhsu/easy-faster-rcnn.pytorch)
     
     
- (Optional) Download the [COCO dataset](http://cocodataset.org/#download) and save it in ``./datasets/COCO``
- Your folders should look like:
    ```
    simple-HRNet
    ├── datasets                (datasets - for training only)
    │  └── COCO                 (COCO dataset)
    ├── losses                  (loss functions)
    ├── misc                    (misc)
    │  └── nms                  (CUDA nms module - for training only)
    ├── models                  (pytorch models)
    │  └── detectors            (people detectors)
    |    └── FasterRCNN         (FasterRCNN repository)
    │      ├── ...
    │      └── checkpoints          (FasterRCNN weights)
    │    └── yolo               (PyTorch-YOLOv3 repository)
    │      ├── ...
    │      └── weights          (YOLOv3 weights)
    ├── scripts                 (scripts)
    ├── testing                 (testing code)
    ├── training                (training code)
    └── weights                 (HRnet weights)
    ```
- If you want to run the training script on COCO `scripts/train_coco.py`, you have to build the `nms` module first.  
  Please note that a linux machine with CUDA is currently required. 
  Built it with either: 
  - `cd misc; make` or
  - `cd misc/nms; python setup_linux.py build_ext --inplace`  


#### 클래스 사용방법

```
import cv2
from SimpleHRNet import SimpleHRNet

model = SimpleHRNet(48, 17, "./weights/pose_hrnet_w48_384x288.pth")
image = cv2.imread("image.png", cv2.IMREAD_COLOR)

joints = model.predict(image)
```

#### live demo 실행

From a connected camera:
```
python scripts/live_demo.py --camera_id 0
```
From a saved video:
```
python scripts/live_demo.py --filename clip1_1.avi
```


#### 학습 script 실행

```
python scripts/train_coco.py
```

For help:
```
python scripts/train_coco.py --help
```
    
#### CCTV Module을 위한 Object Detection, Pose Estimation, Feature Extraction 전체 코드 실행

```
python infer.py --filename clip1_1.avi
```
