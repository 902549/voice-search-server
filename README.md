# Voice Search Server

This project allows you to set up a voice search server, add items to the database along with their speech descriptions, and query the items using voice queries.

If using a Windows machine, you will need to use a Linux terminal to set up the server. The set up for the Windows Subsystem for Linux (WSL) is at the bottom of the README.

## Installation

Follow these steps to set up the voice search server:

1. Create a conda environment:
    ```bash
    conda create -y --name voice-search-server python=3.7
    conda activate voice-search-server
    ```

2. Install required packages:
    ```bash
    conda install -y -c pykaldi pykaldi
    conda install -y -c conda-forge scikit-learn onnx onnxruntime grpcio
    pip3 install click
    ```

   ```bash
   conda install -y -c conda-forge librosa
   ```
## Running the Server

Use the following command to start the voice search server:

```bash
api_port=8080
num_workers=10
model_dir=model
data_dir=data
server.py $api_port $num_workers $model_dir $data_dir
```

## Adding Items to Database

To add a new item to the database along with its speech description, use the following command:

```bash
python3 enroll.py localhost:8080 description.wav label
```

## Querying

To run a query with a new recording, use the following command:

```bash
python3 classify.py localhost:8080 query.wav
```

## Retraining the ranker

To retrain the ranker, use the following command:
```bash
python3 train_classifier.py localhost:8080
```


## Windows Linux Subsystem Setup
The following steps should create a suitable Linux subsystem to follow the installation steps above.

1. Install WSL
To install WSL, use the following command and then restart your machine:
```bash
wsl --install
```

If wsl is already installed, use the following command to create a Ubuntu terminal:
```bash
wsl --install -d Ubuntu
```

This will open a terminal to set up your Linux username and password. For more information about WSL set up, please see https://learn.microsoft.com/en-us/windows/wsl/setup/environment

2. Install Miniconda
To install Miniconda within the Ubuntu terminal, run the following command:
```bash
mkdir -p ~/miniconda3
wget https://repo.anaconda.com/miniconda/Miniconda3-latest-Linux-x86_64.sh -O ~/miniconda3/miniconda.sh
bash ~/miniconda3/miniconda.sh -b -u -p ~/miniconda3
rm -rf ~/miniconda3/miniconda.sh
```

The instructions for installing Miniconda on the command line can also be found here https://docs.anaconda.com/free/miniconda/#quick-command-line-install

3. Initialize Miniconda
To initialize Miniconda within the Ubuntu terminal, run the following command:
```bash
~/miniconda3/bin/conda init bash
~/miniconda3/bin/conda init zsh
```

4. Install pip
To install pip within the Ubuntu terminal, run the following command:
```bash
sudo apt-get install python3-pip
```
