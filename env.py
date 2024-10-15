import subprocess

# Define the versions for PyTorch, CUDA, and cuDNN
pytorch_version = '1.11.0'
cuda_version = '11.3'
cudnn_version = '8'  # This is not directly specified in the conda install command, but make sure your CUDA version is compatible with the desired cuDNN version

# Create a Conda environment named 'myenv' (you can choose any name)
env_name = 'codetr'
# subprocess.run(f'conda create -n {env_name} python=3.8', shell=True, check=True)

# # Activate the Conda environment (this might not work directly in a Python script, see note below)
# # subprocess.run(f'conda activate {env_name}', shell=True, check=True)

# # Install PyTorch with CUDA
# subprocess.run(f'conda install -n {env_name} pytorch={pytorch_version} cudatoolkit={cuda_version} -c pytorch', shell=True, check=True)

# Install MMCV
subprocess.run(f'conda run -n {env_name} pip install --no-cache-dir --upgrade pip wheel setuptools', shell=True, check=True)
subprocess.run(f'conda run -n {env_name} pip install --no-cache-dir mmcv-full==1.5.0 -f https://download.openmmlab.com/mmcv/dist/cu113/torch1.11.0/index.html', shell=True, check=True)

# Install MMDetection
subprocess.run(f'conda run -n {env_name} pip install openmim', shell=True, check=True)
subprocess.run(f'conda run -n {env_name} pip install timm', shell=True, check=True)
subprocess.run(f'conda run -n {env_name} mim install mmdet==2.25.3', shell=True, check=True)
