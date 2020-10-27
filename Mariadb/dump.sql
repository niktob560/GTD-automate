CREATE TABLE records (
    id bigint unsigned NOT NULL AUTO_INCREMENT PRIMARY KEY,
    note TEXT(4096) NOT NULL,
    creation_date DATETIME DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP NOT NULL,
    root_id bigint unsigned DEFAULT NULL,
    record_type ENUM('crate', 'archive', 'note', 'await', 'later', 'calendar', 'project', 'done') NOT NULL,
    deadline DATETIME DEFAULT NULL,
    executor_info TEXT(4096) DEFAULT NULL,
    done_criteria TEXT(4096) DEFAULT NULL,
    done_plan TEXT(4096) DEFAULT NULL
);