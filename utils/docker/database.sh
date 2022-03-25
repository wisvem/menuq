#!/usr/bin/env bash

docker run -d --name postgres -e POSTGRES_PASSWORD=postgres -e POSTGRES_DB=menuqdb -p 5432:5432 postgres
