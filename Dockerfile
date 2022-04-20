FROM python:3.10


ENV LC_ALL=C.UTF-8
ENV LANG=C.UTF-8

RUN mkdir -p /root/.streamlit
RUN bash -c 'echo -e "\
    [general]\n\
    email = \"\"\n\
    " > /root/.streamlit/credentials.toml'

RUN bash -c 'echo -e "\
    [server]\n\
    enableCORS = false\n\
    " > /root/.streamlit/config.toml'

WORKDIR /csicskavok4

COPY requirements.txt ./requirements.txt

# install dependencies
RUN pip3 install -r requirements.txt

EXPOSE 8501

# copy all files over
COPY . .

CMD streamlit run --server.port $PORT app.py

