#! /bin/sh

# Make the appropriate directory
mkdir -p ../lib/notInGit

# Get the tar file
NAME=snortrules-snapshot-2976.tar.gz
OINKCODE=8265f22bc489d835fc499d7fa987656d45fb63c0
wget -O ../lib/notInGit/$NAME https://www.snort.org/rules/$NAME?oinkcode=$OINKCODE

# Process the rules file
cd ../lib/notInGit

# Clean up from a previous installation
rm -rf etc preproc_rules rules so_rules

# Extract the rules file
tar xzf $NAME

# Need to make some changes for this installation
# Get rid of the reputation manager stuff
sed -e "s/var WHITE_LIST_PATH/# var WHITE_LIST_PATH/" -i etc/snort.conf 
sed -e "s/var BLACK_LIST_PATH/# var BLACK_LIST_PATH/" -i etc/snort.conf 

sed -e "s/preprocessor reputation:/# preprocessor reputation:/" -i etc/snort.conf 
sed -e "s/   memcap 500/#    memcap 500/" -i etc/snort.conf 
sed -e "s/   priority whitelist/#    priority whitelist/" -i etc/snort.conf 
sed -e "s/   nested_ip inner,/#    nested_ip inner,/" -i etc/snort.conf 
sed -e "s/   whitelist/#    whitelist/" -i etc/snort.conf 
sed -e "s/   blacklist/#    blacklist/" -i etc/snort.conf 

# My snort is installed in /usr/lib instead in /usr/local/lib
sed -e "s/local\/lib/lib/" -i etc/snort.conf 

# Add in the csv output plugin
echo 'output alert_csv: snort.csv' >> etc/snort.conf
# Add in the unified2 output plugin
echo 'output unified2: filename unified2.log' >> etc/snort.conf

# That is all I need for detection!
cp etc/snort.conf etc/snort_just_detect.conf

# To make the unified2 files have all of the packets in them I
# need to add alerts for whatever packet types I want to keep.
echo 'alert tcp  any any -> any any (sid:1000001; rev:1; msg:"TCP";)' >> etc/snort.conf
echo 'alert udp  any any -> any any (sid:1000002; rev:1; msg:"UDP";)' >> etc/snort.conf

# Uncomment all of the rules
for x in rules/*.rules; do sed "s/# alert/alert/" -i $x; done


