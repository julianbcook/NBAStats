SELECT TEAM.t_name, CONFERENCE.c_name FROM TEAM INNER JOIN CONFERENCE ON (CONFERENCE.c_id = TEAM.t_confid) ORDER BY CONFERENCE.c_name;

SELECT t_name, MAX(t_wins) FROM TEAM;

SELECT t_name, MIN(t_wins) FROM TEAM;

SELECT t_name FROM TEAM WHERE t_ratio >= 50.0;

SELECT t_name, t_wins, t_loss, d_name FROM TEAM INNER JOIN DIVISION ON d_id = t_divisionid ORDER BY d_name, t_wins DESC;

SELECT t_name, t_wins, t_loss, d_name FROM TEAM INNER JOIN DIVISION ON d_id = t_divisionid GROUP BY d_name HAVING MAX(t_wins);

SELECT TEAM.t_name, TEAM.t_wins, CONFERENCE.c_name FROM TEAM INNER JOIN CONFERENCE ON (CONFERENCE.c_id = TEAM.t_confid) ORDER BY CONFERENCE.c_name, TEAM.t_wins DESC;

SELECT table1.teamName, table1.wins, table1.conf FROM (SELECT TEAM.t_name AS teamName, TEAM.t_wins AS wins, CONFERENCE.c_name AS conf FROM TEAM INNER JOIN CONFERENCE ON (CONFERENCE.c_id = TEAM.t_confid) ORDER BY CONFERENCE.c_name, TEAM.t_wins DESC) AS table1 WHERE table1.teamName IN (SELECT t_name FROM TEAM WHERE t_id IN(SELECT po_teamID FROM PLAYOFFS));

SELECT t_name, po_wins, po_loss FROM PLAYOFFS INNER JOIN TEAM ON po_teamID = t_id ORDER BY po_wins DESC;

SELECT t_name FROM TEAM WHERE t_id IN (SELECT po_teamID FROM PLAYOFFS WHERE po_wonChampionship = 'TRUE');

SELECT * FROM PLAYER INNER JOIN (SELECT t_abr FROM TEAM WHERE t_name = 'Golden State Warriors') AS table2 ON p_abr = table2.t_abr ORDER BY p_pname;

SELECT table1.p_pname, table2.t_name FROM (SELECT p_pname, p_abr FROM PLAYER) AS table1 INNER JOIN (SELECT t_name, t_abr FROM TEAM) AS table2 ON table1.p_abr = table2.t_abr ORDER BY table2.t_name;

SELECT p_pname, p_rebounds FROM PLAYER ORDER BY p_rebounds DESC LIMIT 10;

SELECT p_pname, p_points FROM PLAYER ORDER BY p_points DESC LIMIT 10;

SELECT AVG(p_age) FROM PLAYER;

SELECT AVG(table1.p_age), table2.t_name FROM (SELECT p_pname, p_age,p_abr FROM PLAYER) AS table1 INNER JOIN (SELECT t_name, t_abr FROM TEAM) AS table2 ON table1.p_abr = table2.t_abr GROUP BY table2.t_name ORDER BY table2.t_name;

SELECT table1.p_pname,MAX(table1.p_age), table2.t_name FROM (SELECT p_pname, p_age,p_abr FROM PLAYER) AS table1 INNER JOIN (SELECT t_name, t_abr FROM TEAM) AS table2 ON table1.p_abr = table2.t_abr GROUP BY table2.t_name ORDER BY table2.t_name;

SELECT TEAM.t_name, LOCATIONS.state, TEAMLOCATIONS.fromYear, TEAMLOCATIONS.toYear FROM TEAM JOIN TEAMLOCATIONS ON TEAM.t_id = TEAMLOCATIONS.t_id JOIN LOCATIONS ON TEAMLOCATIONS.loc_id = LOCATIONS.l_id ORDER BY TEAM.t_name;

SELECT TEAM.t_name, LOCATIONS.state, TEAMLOCATIONS.fromYear, TEAMLOCATIONS.toYear FROM TEAM JOIN TEAMLOCATIONS ON TEAM.t_id = TEAMLOCATIONS.t_id JOIN LOCATIONS ON TEAMLOCATIONS.loc_id = LOCATIONS.l_id ORDER BY LOCATIONS.state;
