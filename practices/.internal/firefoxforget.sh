# .bashrc

# ------------------------------------------------------------------------
# -- DISCLAIMER:
# --    This script is provided for educational purposes only. It is NOT
# --    supported by Oracle World Wide Technical Support.
# --    The script has been tested and appears to work as intended.
# --    You should always run new scripts on a test instance initially.
# --
# ------------------------------------------------------------------------


#Ensure Firefox doesn't remember passwords the first time this is run (only needed on host01)
cd /home/oracle/.mozilla/firefox/zk4vxh3s.default
mv key3.db key3.db.old >/dev/null 2>&1
mv signons.sqlite signons.sqlite.old >/dev/null 2>&1
cd -


