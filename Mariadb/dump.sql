CREATE TABLE records (
    id bigint unsigned NOT NULL AUTO_INCREMENT PRIMARY KEY,
    note VARCHAR(4096) NOT NULL,
    creation_date DATETIME DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP NOT NULL,
    root_id bigint unsigned DEFAULT NULL,
    record_type ENUM('crate', 'archive', 'note', 'await', 'later', 'calendar', 'project', 'done') NOT NULL
);

CREATE TABLE executors (
    id bigint unsigned NOT NULL AUTO_INCREMENT PRIMARY KEY,
    executor_info VARCHAR(4096) NOT NULL,
    root_id bigint unsigned NOT NULL
);

CREATE TABLE deadlines (
    id bigint unsigned NOT NULL AUTO_INCREMENT PRIMARY KEY,
    deadline DATETIME NOT NULL,
    root_id bigint unsigned NOT NULL
);

CREATE TABLE done_criterias (
    id bigint unsigned NOT NULL AUTO_INCREMENT PRIMARY KEY,
    criteria VARCHAR(4096) NOT NULL,
    root_id bigint unsigned NOT NULL
);

CREATE TABLE project_plans (
    id bigint unsigned NOT NULL AUTO_INCREMENT PRIMARY KEY,
    plan VARCHAR(4096) NOT NULL,
    root_id bigint unsigned NOT NULL
);