drop_users = """DROP TABLE IF EXISTS users"""
drop_cache = """DROP TABLE IF EXISTS cache"""
drop_cached_type = """DROP TABLE IF EXISTS cached_type"""
drop_type_ids = """DROP TABLE IF EXISTS place_types"""
drop_favorites = """DROP TABLE IF EXISTS favorites"""

create_users = """
CREATE TABLE users(
    user_id INTEGER PRIMARY KEY,
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

create_cache = """
CREATE TABLE cache(
    cache_id INTEGER PRIMARY KEY,
    cached_stamp DATETIME NOT NULL DEFAULT CURRENT_TIMESTAMP,
    place_id TEXT UNIQUE NOT NULL,
    name TEXT NOT NULL,
    -- place_type TEXT NOT NULL,
    latitude FLOAT NOT NULL,
    longitude FLOAT NOT NULL,
    address TEXT NOT NULL DEFAULT ''
)
"""

create_cached_type = """
CREATE TABLE cached_type(
    -- cached_type_id INTEGER PRIMARY KEY,
    place_id TEXT NOT NULL,
    type_id INTEGER NOT NULL,
    CONSTRAINT fk_cache
        FOREIGN KEY (place_id)
        REFERENCES cache(place_id)
        ON DELETE CASCADE,
    
    CONSTRAINT fk_type
        FOREIGN KEY (type_id)
        REFERENCES types(type_id)
)
"""

create_type_ids = """
CREATE TABLE place_types(
    type_id INTEGER PRIMARY KEY,
    place_type TEXT NOT NULL
)
"""

create_favorites = """
CREATE TABLE favorites(
    user_id INTEGER NOT NULL,
    place_id TEXT NOT NULL,

    CONSTRAINT fk_user
        FOREIGN KEY (user_id)
        REFERENCES users(user_id),

    CONSTRAINT fk_cache
        FOREIGN KEY (place_id)
        REFERENCES cache(place_id)
)
"""

schema = [drop_users, drop_cache, drop_cached_type, drop_type_ids, drop_favorites,
          create_users, create_cache, create_cached_type, create_type_ids, create_favorites]

admin_one = """
INSERT INTO users ( email, email_confirmed, admin,
    first_name, last_name, hash, nonce_timestamp )
    VALUES (
        'admin_one@email.com',
        1,
        1,
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