# Heliades
An Active Directory Passwort Assessment Solution
It tests all passwords against billions of variations of know bad passwords

## What is this Ad Necronomicon
AD Necronomicon is a passwort assesment tool for your active directory. 
It compares all user und computer passwords against a list of your choice
You can provide your own local list or own backend or use the official backend

## Features
- Easy to use UI
- Fast and easy setup with Docker
- Full transparency with open source
- No Price or Fees



## Preperation
Insert the workstation local ip at 
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

## Contributing
Pull requests are welcome. For major changes, please open an issue first to discuss what you would like to change.

Please make sure to update tests as appropriate.


## Todos
- Scheduled Assessment
- UI Improvments


## License
[Apache License 2.0](https://choosealicense.com/licenses/apache-2.0/)


## copyright and license notices 
This product includes software developed by SecureAuth Corporation (https://www.secureauth.com/)  
This product includes software developed by Jens Steube (https://hashcat.net/hashcat/)  

