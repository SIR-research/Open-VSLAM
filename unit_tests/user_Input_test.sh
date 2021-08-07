## trap ctrl-c and call ctrl_c()

trap ctrl_c INT

function ctrl_c() {

echo "** Trapped CTRL-C"

exit
}

read -p "Press any key to continue... " -n1 -s 