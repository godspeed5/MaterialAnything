# Material Anything: Generating Materials for Any 3D Object via Diffusion



### [Project Page](https://xhuangcv.github.io/MaterialAnythingF/) |   [Paper]()  | [Video]()

Material Anything:</b> A PBR material generation model for various 3D meshes, including <span style="color: #4E95D9;">texture-less</span>, <span style="color: #F2AA84;">albedo-only</span>, <span style="color: #8ED973;">generated</span>, and <span style="color: #D86ECC;">scanned</span> objects.

## Abstract
>We present <b>Material Anything</b>, a fully-automated, 
unified diffusion framework designed to generate physically-based materials for 3D objects. 
Unlike existing methods that rely on complex pipelines or case-specific optimizations, 
Material Anything offers a robust, end-to-end solution adaptable to objects under diverse lighting conditions. 
Our approach leverages a pre-trained image diffusion model, 
enhanced with a triple-head architecture and rendering loss to improve stability and material quality. 
Additionally, we introduce confidence masks as a dynamic switcher within the diffusion model, 
enabling it to effectively handle both textured and texture-less objects across varying lighting conditions. 
By employing a progressive material generation strategy guided by these confidence masks, 
along with a UV-space material refiner, our method ensures consistent, UV-ready material outputs. 
Extensive experiments demonstrate our approach outperforms existing methods across a wide range of object categories 
and lighting conditions.

## Overview
<div class="half">
    <img src="assets/pipeline.jpg" width="1080">
</div>
<b>Overview of Material Anything.</b> For texture-less objects, 
we first generate coarse textures using image diffusion models. 
For objects with pre-existing textures, we directly process them. 
Next, a material estimator progressively estimates materials for each view from a rendered image, 
normal, and confidence mask. The confidence mask serves as additional guidance for illuminance uncertainty, 
addressing lighting variations in the input image and enhancing consistency across generated multi-view materials. 
These materials are then unwrapped into UV space and refined by a material refiner.


## Citation
If you find this work helpful for your research, please cite:
```
@article{huang2024materialanything,
  author = {Huang, Xin and Wang, Tengfei and Liu, Ziwei and Wang, Qing},
  title = {Material Anything: Generating Materials for Any 3D Object via Diffusion},
  journal = {arXiv},
  year = {2024}
  }
```