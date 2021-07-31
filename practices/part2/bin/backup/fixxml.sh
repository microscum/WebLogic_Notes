
#Set default folder
folder=/practices/part2/dev

for file in `find $folder -name "*.xml" -print`
do
    sed -i "s/<\!--  ------------------------------------------------------------------------/<!-- ========================================================================/" $file
    sed -i "s/<\!-- ------------------------------------------------------------------------/<!-- ========================================================================/" $file
    sed -i "s/-- DISCLAIMER:/== DISCLAIMER:/" $file
    sed -i "s/--    This script is provided/==    This script is provided/" $file
    sed -i "s/--    supported by Oracle/==    supported by Oracle/" $file
    sed -i "s/--    The script has been tested/==    The script has been tested/" $file
    sed -i "s/--    You should always run/==    You should always run/" $file
    sed -i "s/  --$/  ==/" $file
    sed -i "s/------------------------------------------------------------------------ -->/======================================================================== -->/" $file
done

#<!-- ------------------------------------------------------------------------
#<!-- ========================================================================     
#  -- DISCLAIMER:
#  --    This script is provided for educational purposes only. It is NOT
#  --    supported by Oracle World Wide Technical Support.
#  --    The script has been tested and appears to work as intended.
#  --    You should always run new scripts on a test instance initially.
#  --
#  ------------------------------------------------------------------------ -->
#  ======================================================================== -->
