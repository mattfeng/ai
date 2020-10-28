FROM nvidia/cuda:10.2-cudnn8-devel-ubuntu18.04

RUN apt-get update && apt-get install -y  \
    build-essential libssl-dev libffi-dev \
    python3-dev python3-pip               \
    python3-virtualenv git                \
    ffmpeg

RUN ln -s $(which python3) /usr/bin/python
RUN ln -s $(which pip3) /usr/bin/pip

RUN pip install                           \
    jupyter numpy scipy matplotlib        \
    scikit-learn sympy                    \
    jupyter_contrib_nbextensions          \
    torch dgl-cu102 wandb

RUN jupyter contrib nbextension install

# install notebook extensions
RUN mkdir -p $(jupyter --data-dir)/nbextensions
RUN git clone https://github.com/lambdalisue/jupyter-vim-binding \
    $(jupyter --data-dir)/nbextensions/vim_binding

# enable notebook extensions
RUN jupyter nbextension enable vim_binding/vim_binding
RUN jupyter nbextension enable freeze/main

RUN mkdir /nb
WORKDIR /nb

ENTRYPOINT ["jupyter", "notebook", "/nb", "--ip", "0.0.0.0", "--port", "8080", "--no-browser", "--allow-root"]
