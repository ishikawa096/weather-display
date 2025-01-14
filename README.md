## Weather Display☁️
## Official Documentation
- Unsplash API (https://unsplash.com/developers)
- OpenWeatherMap API (https://openweathermap.org/api)
- Inky (https://github.com/pimoroni/inky)

## In Raspberry Pi
Activate python virtual environment
```bash
source ~/.virtualenvs/pimoroni/bin/activate
```

Run the script
```bash
python3 weather_display.py
```

Set the script to run every 10 minutes
```bash
crontab -e
```

Add the following line to the crontab file
```bash
*/10 * * * * /home/pi/.virtualenvs/pimoroni/bin/python3 /home/pi/weather_display/weather_display.py >> /var/log/cron.log 2>&1
```

Create a log file
```bash
sudo touch /var/log/cron.log
sudo chown pi:pi /var/log/cron.log
```
