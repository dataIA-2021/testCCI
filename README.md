# testCCI

```bash
 #UVICORN_PORT=3010 uvicorn main:app --host 0.0.0.0

 git pull
 git fetch
 docker build -t testcci .
 docker rm -f goudot
 docker run -d -p 3000:3000 --name goudot --restart always -e UVICORN_PORT=3000 testcci


```