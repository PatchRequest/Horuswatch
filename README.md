# Horuswatch
An Active Directory Passwort Assessment Solution <br>
Test every password of your Forests against billions of bad ones

## Features
- Easy to use UI
- Fast and easy setup with Docker
- Full transparency with open source
- No Price or Fees



## Preperation
Insert the workstation network ip into the docker-compose file

```bash
...
build: 
        context: ./web_frontv2
        args:
          - VUE_APP_BACKEND=http://<local ip>:8080    <-- HERE
      container_name: adwebinterface
      ports:
...

```

## Usage
```
docker-compose up
```
Then open the ui in your webbrowser at the given local ip
Example:
http://192.168.178.133

## Contributing
Pull requests are welcome. For major changes, please open an issue first to discuss what you would like to change.

Please make sure to update tests as appropriate.

## Container
### Cracker
Hashcat + Flask for receiving cracking Task and reporting the results
### Syncer
Impacket + Flask for DCSync with a Domain Controller
### Datasafe
Flask + SQLite for Storing Statistics + Results
### Webfront
Vue Frontend


## Todos
- Scheduled Assessment
- UI Improvments



## copyright and license notices 
This product includes software developed by SecureAuth Corporation (https://www.secureauth.com/)  
This product includes software developed by Jens Steube (https://hashcat.net/hashcat/)  

