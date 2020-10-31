# Downloading and installation
1. Download anaconda from https://www.anaconda.com/products/individual
2. Open anaconda prompt, CD to directory to spleeter
3. Create virtual environment using "conda create -n venv-name python=3.7 conda=4.6
4. Activate virtual environment using "conda activate venv-name"
5. Install spleeter using "conda install -c conda-forge spleeter"
6. pip install pytube3
7. Update pytube to resolve KeyError: 'asset' issue "python -m pip install git+https://github.com/nficano/pytube"
8. pip install moviepy
10. pip install pydub
11. Run "python downloader.py" enter youtube URL