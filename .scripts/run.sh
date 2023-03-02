#docker run -it --rm -e DISPLAY=$DISPLAY -v $PWD:/app jkutkut/travelagency
docker run -it --rm \
	-e DISPLAY=$DISPLAY
	-v $PWD:/app \
	-v /tmp/.X11-unix:/tmp/.X11-unix
	--name travelagency
	jkutkut/travelagency
