### Execution

```
./duf_app.py -i ./input_folder_xlsx/ -o ./output_afa_files/ -e raven.neo@gmail.com
```

## Installation


### Compile Muscle

```
wget https://www.drive5.com/muscle/muscle_src_3.8.1551.tar.gz
mkdir muscle
tar -zxvf muscle_src_3.8.1551.tar.gz --directory ./muscle/
cd muscle
make -j`nproc`
sudo cp muscle /usr/local/bin/muscle
```

### Install deb packages

```
sudo apt-get update
sudo apt-get install -y \
  python3 python3-pip \
  rename \
  gnumeric
```

### Install python packages

```
python3 -m pip install -r /build/requirements.txt
```
