if [ ! -x /app/data.db ]; then
  cd /app;flask initdb;ls -al; echo "initdb success"
fi
sleep 1s
python3 /app/app.py

