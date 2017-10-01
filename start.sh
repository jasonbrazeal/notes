function clean_up () {
    echo "Exiting Flask and Python servers..."
    kill $FLASK_PID $SERVER_PID
    echo "Goodbye!"
    exit
}

trap clean_up SIGHUP SIGINT SIGTERM
cd build
python -m http.server &
SERVER_PID=$!
echo "Python http server serving static files with PID $SERVER_PID"
flask run &
FLASK_PID=$!
echo "Flask dev server serving app with PID $FLASK_PID"
wait $FLASK_PID $SERVER_PID
