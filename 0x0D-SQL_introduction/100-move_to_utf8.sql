-- converts hbtn_0c_0 db to UTF8 (utf8mb4, collate utf8mb4_unicode_ci)
ALTER DATABASE hbtn_0c_0 CHARACTER SET utf8mb4 COLLATE utf8mb4_unicode_ci;
-- converts first_table to utf8mb4, collate utf8mb4_unicode_ci
ALTER TABLE hbtn_0c_0.first_table CONVERT TO CHARACTER SET utf8mb4 COLLATE utf8mb4_unicode_ci;
