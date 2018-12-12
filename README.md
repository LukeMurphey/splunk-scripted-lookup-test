# splunk-scripted-lookup-test
A test of scripted lookups in Splunk



export SPLUNK_HOME=/Users/lmurphey/Splunk/721
export PYTHONPATH=$SPLUNK_HOME/lib/python2.7
export SPLUNK_DB=$SPLUNK_HOME/var/lib
export SPLUNK_ETC=$SPLUNK_HOME/etc

cat $SPLUNK_HOME/etc/apps/lookup_test/lookups/testfile.csv | $SPLUNK_HOME/bin/python $SPLUNK_HOME/etc/apps/lookup_test/bin/test_lookup.py clienthost