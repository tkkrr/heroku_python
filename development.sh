npm run watch -prefix ./frontend/ & 
gunicorn index:app --log-file - &
wait