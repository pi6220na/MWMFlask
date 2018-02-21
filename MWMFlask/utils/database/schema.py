drop_users = """DROP TABLE IF EXISTS users"""
create_users = """
CREATE TABLE users(
    email VARCHAR(120) UNIQUE NOT NULL,
    email_confirmed SMALLINT NOT NULL DEFAULT 0,
    admin SMALLINT NOT NULL DEFAULT 0,
    first_name VARCHAR(120) DEFAULT '',
    last_name VARCHAR(120) DEFAULT '',
    hash VARCHAR(60) NOT NULL,
    nonce VARCHAR(64) DEFAULT '',
    nonce_timestamp DATETIME,
    creation_time DATETIME NOT NULL DEFAULT CURRENT_TIMESTAMP
)
"""

schema = [drop_users, create_users]

admin_one = """
INSERT INTO users ( email, email_confirmed, admin,
    first_name, last_name, hash, nonce_timestamp )
    VALUES (
        'admin_one@email.com',
        1,
        0,
        'Admin',
        'User',
        '$2b$12$GCu5uceKtCaGzfE0i7yJXOUDbPUlGO10eAx228xPPXR.DCDHpiGLe',
        ''
    )
"""


user_one = """
INSERT INTO users ( email, email_confirmed, admin,
    first_name, last_name, hash, nonce_timestamp )
    VALUES (
        'user_one@email.com',
        1,
        0,
        'First',
        'User',
        '$2b$12$7gtrBCGnn7oN1oj6Lxs9qeOv8UUG5qZw22UhM9Ckkrt4O7SrOeJ4i',
        ''
    )
"""


user_two = """
INSERT INTO users ( email, email_confirmed, admin,
    first_name, last_name, hash, nonce_timestamp )
    VALUES (
        'user_two@email.com',
        1,
        0,
        'Second',
        'User',
        '$2b$12$q9k7Tn45jPKS8B7RCOrq2u2UnBKI3uAKHXxuGke0F.CCMUCKcundm',
        ''
    )
"""

test_users = [admin_one, user_one, user_two]