export ORACLE_HOME=$MW_HOME

# ------------------------------------------------------------------------
# -- DISCLAIMER:
# --    This script is provided for educational purposes only. It is NOT
# --    supported by Oracle World Wide Technical Support.
# --    The script has been tested and appears to work as intended.
# --    You should always run new scripts on a test instance initially.
# --
# ------------------------------------------------------------------------


if [ -z `echo $PATH | grep OPatch` ]; then
    export PATH=$MW_HOME/OPatch:$PATH
fi

echo "ORACLE_HOME has been set to point to your MW_HOME: $ORACLE_HOME"
echo "opatch is set in your PATH"

