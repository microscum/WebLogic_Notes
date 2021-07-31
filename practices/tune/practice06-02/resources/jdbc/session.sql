
 ------------------------------------------------------------------------
 -- DISCLAIMER:
 --    This script is provided for educational purposes only. It is NOT
 --    supported by Oracle World Wide Technical Support.
 --    The script has been tested and appears to work as intended.
 --    You should always run new scripts on a test instance initially.
 --
 ------------------------------------------------------------------------

-- wl_servlet_sessions Database Table for HTTP Sessions
-- Create as orcl
-- User name: oracle
-- Password: Welcome1
--

-- Drop existing tables and Constraints
--

DROP TABLE wl_servlet_sessions;

CREATE TABLE wl_servlet_sessions (
	wl_id VARCHAR2(100)  NOT NULL, 
	wl_context_path VARCHAR2(100) NOT NULL, 
	wl_is_new CHAR(1), 
	wl_create_time NUMBER(20), 
	wl_is_valid CHAR(1), 
	wl_session_values LONG RAW, 
	wl_access_time NUMBER(20) NOT NULL, 
	wl_max_inactive_interval INTEGER,
	PRIMARY KEY (wl_id, wl_context_path)
);

quit;
