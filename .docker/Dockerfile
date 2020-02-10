FROM python:3.6-stretch
RUN apt-get update && apt-get install -y --no-install-recommends binutils gdal-bin libproj-dev

RUN sed -i 's/httpredir.debian.org/mirrors.aliyun.com/g' /etc/apt/sources.list
RUN apt-get update
COPY requirements.txt /app/requirements.txt
WORKDIR /app
RUN pip install --upgrade pip setuptools -i http://pypi.douban.com/simple --trusted-host pypi.douban.com
RUN pip install -r requirements.txt -i http://pypi.uucin.com --trusted-host pypi.uucin.com --trusted-host gitbucket.uucin.com

ADD . /app

EXPOSE 8000
CMD ["gunicorn", "-c", "gunicorn_config.py", "shared_bicycle_platform_server.wsgi:application"]
