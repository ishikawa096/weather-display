## Weather Display☁️

<img src="https://github.com/user-attachments/assets/5d67477e-079c-45b0-88bb-e0beda03ff2b" alt="Weather display example photo" width="300" style="border-radius: 10px;text-align: center;">

## Dependencies Official Documentation

- Unsplash API (https://unsplash.com/developers)
- OpenWeatherMap API (https://openweathermap.org/api)
- Inky (https://github.com/pimoroni/inky)

## Development Environment

Open in devcontainer in Visual Studio Code

Clone and install the inky library
https://github.com/pimoroni/inky

Install the required libraries

```bash
pip install -r requirements.txt
```

Copy the .env.example file and rename it to .env

```bash
cp .env.example .env
```

Change the .env file to the actual values

```bash
UNSPLASH_ACCESS_KEY=your_access_key
OPENWEATHERMAP_API_KEY=your_api_key
```

Run the script then check the image.png file

```bash
python weather_display/main.py
```

## In Raspberry Pi

Copy the weather_display folder, requirements.txt and .env to the Raspberry Pi

Off the MOCK_MODE in the .env file

```bash
MOCK_MODE=False
```

Clone and install the inky library
https://github.com/pimoroni/inky

Activate python virtual environment

```bash
source ~/.virtualenvs/pimoroni/bin/activate
```

Install the required libraries

```bash
pip install -r weather_display/requirements.txt
```

Set the script to run every 10 minutes

```bash
crontab -e
```

Add the following line to the crontab file

```bash
*/10 * * * * /home/pi/.virtualenvs/pimoroni/bin/python3 /home/pi/weather_display/main.py >> /var/log/cron.log 2>&1
```

Create a log file

```bash
sudo touch /var/log/cron.log
sudo chown pi:pi /var/log/cron.log
```

### Setting Up Inky Button Press Monitoring (Optional)

```bash
sudo vi /etc/systemd/system/inky-buttons.service
```

Add the following lines to the inky-buttons.service file

```bash
[Unit]
Description=Inky Buttons Service
After=multi-user.target

[Service]
Type=simple
ExecStart=/home/pi/.virtualenvs/pimoroni/bin/python3 /home/pi/weather_display/buttons.py
Restart=on-failure
User=pi

[Install]
WantedBy=multi-user.target
```

Enable the service

```bash
sudo systemctl daemon-reload
sudo systemctl enable inky-buttons.service
sudo systemctl start inky-buttons.service
sudo systemctl status inky-buttons.service
```

## Acknowledgements

This project utilizes the following third-party resources:

- Better VCR Font
  - Creator: artdzyk
  - Source: https://www.dafont.com/better-vcr.font
  - Usage: Display font
