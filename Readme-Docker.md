# HOW-To run with docker

Instructions are for docker-machine for windows

docker volume create bitpoll
docker network create test

## Running postgres
docker run --name bitpoll-postgres  -v bitpoll:/var/lib/postgresql/data -p 5000:5432 -e 'POSTGRES_PASSWORD=postgres' -e 'PGDATA=/var/lib/postgresql/data/pgdata'  -d  --network=test  postgres


# move folder bitpoll-win-settings in your home ~ 
docker-machine does not allow mapping outside ~ (home-dir) without tricks


# let it run 

Attention the slashes //c  - thats an windows-issue!
docker run -d --rm -p 3008:3008 -v '//c/Users/<your-id>/bitpoll-win-settings/settings_local.py://app/bitpoll/settings_local.py' --network=test  mschwehl/bitpoll:0.9.7


# go to browser 

http://192.168.99.101:3008

the ip is available to docker-machine ip <machine>
