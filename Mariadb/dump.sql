CREATE TABLE long_tokens (
    id bigint unsigned NOT NULL AUTO_INCREMENT PRIMARY KEY,
    token TEXT(1024) NOT NULL UNIQUE
);

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

CREATE TABLE expiring_tokens (
    id bigint unsigned NOT NULL AUTO_INCREMENT PRIMARY KEY,
    token VARCHAR(4096) NOT NULL UNIQUE,
    owner_token_id bigint unsigned NOT NULL,
    FOREIGN KEY (owner_token_id) REFERENCES long_tokens (id) ON DELETE CASCADE,
    expire_at DATETIME NOT NULL
);

INSERT INTO long_tokens (token) VALUES ('vPtGkVWfRXfNXyRCmUJtXZkS5CTEfaOjOruVxevqvXGybc1CKi9M9WEwL3LFbecyBRT4gSJrQXUJrKKUxmDpCKI2ntzu3DEjxxwSYYJPmAHqk9ZKLuZ17U1sKKnLdevZdo8JH8VML4IAST9fNEMYHm5wv6hlZj6CLdRQTT1Tx2NLBNFwQfPceyUbpPe587G15n6F4xh6snfvwhRKwPbzsPnW4iKeLPji4ZyYD3Kbd3EhG9UymRCaoUUiRO4q6OENNxg428ZhhaEsDFb9FIqVIGP5B9OVMNhsj9Ds59vQDOR9DTAzoZNhICUGGSMTab8yAC6O8cJQEe1u9lxXqMmSJTW1ZKFm3LVMX8Vs5UUfbSXrrMkBtJnEFQiuZFU1L9bp1q8EalvsXEl8JgSMv27Oy7P19MQsAUC5qikRv7QDLhfTbD77L3aygEktvjfBch268jJbCnoRKCCDTnL4qc4xuNhs2Sb7S3AFs9TijwlFJl7fpWmaBtdeDSY42UsKcj66cp6E1ReyMP4O9SXDVWFv6QnKy8kvAz4tSi7ygsM2wbFz8wjKgTxiNSxjTxrIhS3xsfAFCQHiO6Etdde4hEiCQEot5f8sJu9TuPl797JmlyheCBY2fdqmpbOYHvLUM4QrqOtUa7V2ROWXiIRSExVt7qxQLpTjdUy35qxm22Ff3Va4moGH3SA2Snxs8wjMvt2wd1iWm1UXUg2fqMwYRaANuWZjtyNijn4UdqGxzTQaVREQy8f4hN9sGzG12XJdGAKr1y3tsTtxUAZMklfe4Gic1g2D9jXbhbDDq1f4voZVvBooxFefQ8ZnvR5LKznyw3SvRwnFQR6CqvGBxyYnJY7dMXys2nA7GhaPNvyBVNspgT5yX6UQwGr7cw83hCE4NVGL2g9qUZFvVyINH9U7yUOyUv677PBbcey8Fa6jDdUYOjTxK1uoSsU2Bf5d1PgcPcQCSrtdqbCun3xKmFDsZ94p5cGQxm8TozPvjPXXmdyvMGFsm1pTpbhXE9Ot8vfdRXOp');