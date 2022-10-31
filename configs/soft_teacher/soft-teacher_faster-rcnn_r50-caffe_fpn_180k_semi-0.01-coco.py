'''
Author: Ghost 1432072586@qq.com
Date: 2022-10-26 18:02:35
LastEditors: Ghost 1432072586@qq.com
LastEditTime: 2022-10-30 16:30:36
FilePath: /mmdetection/configs/soft_teacher/soft-teacher_faster-rcnn_r50-caffe_fpn_180k_semi-0.01-coco.py
Description: 
'''
_base_ = ['soft-teacher_faster-rcnn_r50-caffe_fpn_180k_semi-0.1-coco.py']

# 1% coco train2017 is set as labeled dataset
labeled_dataset = _base_.labeled_dataset
unlabeled_dataset = _base_.unlabeled_dataset
labeled_dataset.ann_file = 'semi_anns/instances_train2017.json'
unlabeled_dataset.ann_file = 'semi_anns/instances_unlabeled2017.json'
train_dataloader = dict(
    dataset=dict(datasets=[labeled_dataset, unlabeled_dataset]))
