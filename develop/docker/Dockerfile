ARG python_ver=3.10
FROM python:${python_ver}
ARG netbox_ver=master
ENV PYTHONUNBUFFERED 1

RUN apt update && apt install -y gdal-bin
# -------------------------------------------------------------------------------------
# Install NetBox
# -------------------------------------------------------------------------------------
RUN mkdir -p /opt
RUN pip install -U pip setuptools wheel
RUN git clone --single-branch --branch ${netbox_ver} https://github.com/netbox-community/netbox.git /opt/netbox/ && \
    pip install -r /opt/netbox/requirements.txt

# Work around https://github.com/rq/django-rq/issues/421
RUN pip install django-rq==2.3.2 psycopg2

# -------------------------------------------------------------------------------------
# Netbox Bug Fixes
# -------------------------------------------------------------------------------------
RUN pip install pytz==2022.1

# -------------------------------------------------------------------------------------
# Move configuration.py
# -------------------------------------------------------------------------------------
COPY develop/etc/configuration.py /opt/netbox/netbox/netbox
COPY develop/etc/settings.py /opt/netbox/netbox/netbox

# -------------------------------------------------------------------------------------
# Install Netbox Plugin
# -------------------------------------------------------------------------------------
RUN mkdir -p /opt/netbox_geo
COPY . /opt/netbox_geo
WORKDIR /opt/netbox_geo/
RUN python setup.py develop

WORKDIR /opt/netbox/netbox/
RUN pip install -r /opt/netbox/requirements.txt -U
