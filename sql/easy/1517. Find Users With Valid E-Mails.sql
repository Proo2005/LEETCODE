SELECT *
FROM Users
WHERE LOWER(mail) REGEXP '^[a-z][a-z0-9._-]*@leetcode\\.com$';
