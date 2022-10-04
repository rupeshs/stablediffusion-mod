from setuptools import setup, find_packages

setup(
    name='k-diffusion',
    version='0.0.1',
    description='k-diffusion sampler',
    packages=find_packages(),
    install_requires=[
        'accelerate',
        'clean-fid',
        'einops',
        'jsonmerge',
        'kornia',
        'Pillow',
        'resize-right',
        'scikit-image',
        'scipy',
        'torch',
        'torchdiffeq',
        'torchvision',
        'tqdm',
        'wandb',
        'clip==1.0',
    ],
    dependency_links=[
        'git+https://github.com/openai/CLIP.git@main#egg=clip-1.0'
    ]
)
