CREATE TABLE records (
    id bigint unsigned NOT NULL AUTO_INCREMENT PRIMARY KEY,
    note TEXT(4096) NOT NULL,
    creation_date DATETIME DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP NOT NULL,
    root_id bigint unsigned DEFAULT NULL,
    record_type ENUM('crate', 'archive', 'note', 'await', 'later', 'calendar', 'project', 'done', 'current') NOT NULL,
    deadline DATETIME DEFAULT NULL,
    executor_info TEXT(4096) DEFAULT NULL,
    done_criteria TEXT(4096) DEFAULT NULL,
    done_plan TEXT(4096) DEFAULT NULL,
    owner_token_id bigint unsigned NOT NULL,
    FOREIGN KEY (owner_token_id) REFERENCES long_tokens (id) ON DELETE CASCADE
);

CREATE TABLE long_tokens (
    id bigint unsigned NOT NULL AUTO_INCREMENT PRIMARY KEY,
    token TEXT(8192) NOT NULL UNIQUE
);

CREATE TABLE expiring_tokens (
    token TEXT(16384) NOT NULL UNIQUE,
    owner_token_id bigint unsigned NOT NULL,
    FOREIGN KEY (owner_token_id) REFERENCES long_tokens (id) ON DELETE CASCADE
) ENGINE=MEMORY;