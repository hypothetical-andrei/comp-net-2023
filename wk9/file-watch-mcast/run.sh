dir=`pwd`

function runserver() {
  source "/home/null/.virtualenvs/p3net/bin/activate"
  python sync-server.py
}

function runclient() {
  source "/home/null/.virtualenvs/p3net/bin/activate"
  python sync-multicast-client.py
}

export -f runserver
export -f runclient

gnome-terminal --working-directory="$dir" --tab --title="SRV" -- bash -ci "runserver; exec bash;"
gnome-terminal --working-directory="$dir" --tab --title="CL" -- bash -ci "runclient; exec bash;"
