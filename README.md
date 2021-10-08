# Banker

Everythings are going to run automatically.

## HOW TO RUN

there are two options to run:
1. run Django locally - without Celery and Redis 2. Full Run

### Option 1 - run locally

SO to run project in `development mode` just run:

```bash
chmod  777 drop_db.sh 
./drop_db.sh
```

### Option 2 - Full Run

to run project in `development mode` just run:

```bash
chmod  777 run.sh 
./run.sh development
```

Also `run.sh` could take options:

```bash
./run.sh [options]

	-options are:
		deafult: production
		production
		development
		testing
```

## HOW TO USE
just import `./APIs.json` to the `postman` appllication, this shows you the way...

## Any Docker Problem
this could depends on many things... but let's check this:

```bash
sudo docker rm -f $(sudo docker ps -aq)
./run.sh development
```