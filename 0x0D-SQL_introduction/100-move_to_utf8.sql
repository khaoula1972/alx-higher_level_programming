-- Go to UTF8

-- Converts hbtn_0c_0 database to UTF8 (utf8mb4, collate utf8mb4_unicode_ci)
ALTER DATABASE hbtn_0c_0
    CHARACTER SET utf8mb4
    COLLATE utf8mb4_unicode_ci;

-- Next, convert the table character set and collation
ALTER TABLE hbtn_0c_0.first_table
    CONVERT TO CHARACTER SET utf8mb4
    COLLATE utf8mb4_unicode_ci;

-- Finally, convert the field (name) character set and collation within the first_table
ALTER TABLE hbtn_0c_0.first_table
    MODIFY name VARCHAR(256) CHARACTER SET utf8mb4 COLLATE utf8mb4_unicode_ci;
