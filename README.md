# Banker

this is awesome, every things is going to run automatically.

## HOW TO RUN
only thing which you have to do is run the `run.sh` file with `a right parameter`. the parameter is depends on environment which you are on `Development` | `production` | `testing`.

it, First makes right `docker-compose.yml` config by running below commands:

```bash
./run.sh [options]

	-options are:
		deafult: production
		production
		development
		testing
```

### Finally
SO to run project in `development mode` just run:
```bash
chmod  777 run.sh 
./run.sh development
```

