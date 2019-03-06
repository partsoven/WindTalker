# WindTalker
This project is a redundant data stream to our local wind talker. It subscribes to the Particle data stream "JL3X"

Prerequisite:
Particle CLI installed: 
https://docs.particle.io/reference/developer-tools/cli/

Then in terminal run (#to do automate in script):
particle subscribe --all JL3X | tee -a Desktop/WindTalker/particledata.txt

