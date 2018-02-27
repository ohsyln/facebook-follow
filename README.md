 # facebook-follow

Non-API script to follow all your friends on Facebook. Uses Selenium with Chromedriver.

### Prerequisites (OS X)

Install [miniconda](https://conda.io/docs/user-guide/install/macos.html).

Install Python3:

```
brew install python3 
```

Check they are properly installed:

```
python --version
conda --version
```

### Installing

Clone to your local directory:

```
git clone https://github.com/ohsyln/facebook-follow
cd facebook-follow
```

Create virtual environment, and activate:

```
conda create --yes --name fb-follow-env
conda activate fb-follow-env
```

Install Selenium and Chromedriver:

```
conda install --yes -c conda-forge selenium
conda install --yes -c clinicalgraphics chromedriver
```

## Run script

Edit `PROFILE_NAME`, `EMAIL`, `PASSW` in `follow.py` with a text editor:

* visit your profile to see `PROFILE_NAME` i.e. `https://facebook.com/PROFILE_NAME`

```
PROFILE_NAME = "profile_name_here"
EMAIL = "your_email@example.com"
PASSW = "your_password"
```

Save changes and run script

```
python follow.py
```

## License

MIT
