import os

from fastai.vision.all import *
import joblib
from fastdownload import download_url
import warnings

warnings.filterwarnings("ignore")

if __name__ == '__main__':
    data_dir  = "C:/Users/manoj/OneDrive/Desktop/Garbage Classification/Garbage Classification"
    
    classes = os.listdir(data_dir)
    print(classes)
    
    path = os.path.join("C:/Users/manoj/OneDrive/Desktop/Garbage Classification/Garbage Classification")
    labels = ['glass', 'metal', 'paper', 'plastic', 'trash']
    
    histogram_labels = []
    for label in labels:
        directory = os.path.join(path, label)
        print(f"Class: {label} — {len(os.listdir(directory))} samples")
        
    dls = DataBlock(
        blocks=(ImageBlock, CategoryBlock), 
        get_items=get_image_files, 
        splitter=RandomSplitter(valid_pct=0.2, seed=0),
        get_y=parent_label,
        item_tfms=[Resize(192, method='squish'),  ]
    ).dataloaders(path, bs=32)
    
    
    avg = 'macro'
    learner_fl = vision_learner(
        dls, resnet50, normalize=True, n_out=len(labels), lr=0.003, loss_func=FocalLossFlat()
    )
    
    learner_fl.fine_tune(30, base_lr=0.001)
    
    dest = 'download.jpg'
    
    im = Image.open(dest)
    
    label, _, probs = learner_fl.predict(PILImage.create('download.jpg'))
    
    print(f'The prediction of the type of garbage: {label}')
    print(f'The probabilities of belonging to the classes: {probs}')
    
    joblib.dump(learner_fl,"C:/Users/manoj/OneDrive/Desktop/Dump/Model2.sav")