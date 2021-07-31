
 ------------------------------------------------------------------------
 -- DISCLAIMER:
 --    This script is provided for educational purposes only. It is NOT
 --    supported by Oracle World Wide Technical Support.
 --    The script has been tested and appears to work as intended.
 --    You should always run new scripts on a test instance initially.
 --
 ------------------------------------------------------------------------

-- Auction Application Database
-- Create as orcl
-- User name: oracle
-- Password: Welcome1
--

-- Drop existing tables and Constraints
--

--drop trigger imageid_trigger;
drop sequence imageid_sequence;
--drop trigger auctionid_trigger;
drop sequence auctionid_sequence;
--drop trigger bidid_trigger;
drop sequence bidid_sequence;
drop sequence SEQ_GEN_IDENTITY;

DROP TABLE Bid;
DROP TABLE Auction;
DROP TABLE Image;

quit;

