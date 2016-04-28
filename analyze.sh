#!/bin/bash

#Get current directory
SCRIPT=$(readlink -f "$0")
SCRIPTPATH=$(dirname "$SCRIPT")

#empty database
mysql --user=root --password=123 icc -e "DROP DATABASE icc" 
mysql --user=root --password=123 -e "CREATE DATABASE icc" 
mysql --user=root --password=123 icc < schema

#run ic3
#cd $SCRIPTPATH/soot-infoflow-android-iccta-master/iccProvider/ic3
#echo "Running IC3"
#apkFiles=""
#for apk_file in $SCRIPTPATH/covert_dist/app_repo/bundle/*.apk
#do
#    echo $apk_file
#	 apkFiles+="$apk_file "
    #./runIC3.sh $apk_file
#done

#run apKCombiner
#cd $SCRIPTPATH/soot-infoflow-android-iccta-master/release
#./runApkCombiner.sh $apkFiles

#runIccTA
#java -Xmx3g -jar IccTA.jar -apkPath org.cert.echoer-ac-org.cert.sendsms-ac--ac-org.cert.WriteFile.apk -androidJars ../android-platforms -iccProvider ic3 -enableDB -intentMatchLevel 3
#./runFlowdroidIccTA.sh org.cert.sendsms-ac-org.cert.echoer-ac-org.cert.WriteFile.apk

#run covert
#echo "Running Covert"
#cd $SCRIPTPATH/covert_dist
#./covert.sh bundle

#run didfail
#echo "Running didfail"
#cd $SCRIPTPATH/didfail/cert
#./run-didfail.sh $SCRIPTPATH/didfail/output $SCRIPTPATH/covert_dist/app_repo/bundle/*.apk

#run scripts
cd $SCRIPTPATH/post_analysis
echo "Running parser..."
python parser.py
echo "Finding links"
python links.py
echo "Creating architectural models..."
python architectural_model.py
#mv data.json $SCRIPTPATH/

echo "Done"

#umask u=,g=,o=rwx
