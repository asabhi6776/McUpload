# ModUpload

<p> This is "ModUpload". By using this repo we can start one application, which can we used to upload minecraft mods in minecraft server.</p>

## Requirements

<p>In order to use this application, first we need to start minecraft server, and we need to mount plugins folder of minecraft server with Modupload container.</p>

## Usage

To run this In container we need to run following commands

```bash
git clone https://github.com/asabhi6776/McUpload.git
cd McUpload
docker network create --subnet=172.32.0.0/16 mine-network
vim .env #customize as per your need
docker-compose up -d
# create a user by running following command
docker exec -it modupload python3 manage.py createsuperuser
```

## Contributing

<p>Pull requests are welcome. For major changes, please open an issue first to discuss what you would like to change.</p>

## License

[MIT](https://mit-license.org/)

## Thanks

<a href="https://www.buymeacoffee.com/asabhi6776"><img src="https://cdn.buymeacoffee.com/buttons/v2/default-yellow.png" width="200" /></a>
