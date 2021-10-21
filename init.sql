CREATE DATABASE 'feedsofothers';
USE 'feedsofothers'

CREATE TABLE 'user' (
    'user_id' INT(11) PRIMARY KEY AUTO_INCREMENT,
    'created_at' DATETIME DEFAULT CURRENT_TIMESTAMP(),
    'last_sync' DATETIME DEFAULT CURRENT_TIMESTAMP(),
    'last_load' JSON,
);

CREATE TABLE 'tag' (
    'tag_id' INT(11) PRIMARY KEY AUTO_INCREMENT,
    'tag' VARCHAR(20) NOT NULL UNIQUE,
);

CREATE TABLE 'resource' (
    'public_tweet_id' INT(20) PRIMARY KEY,
    'str_public_tweet_id' VARCHAR(20),
);


CREATE TABLE 'user/tag' (
    PRIMARY KEY (user_id, tag_id)
    CONSTRAINT 'usertag_user_fk'
        FOREIGN KEY 'user_fk' (user) REFERENCES 'User' (user_id)
        ON DELETE CASCADE ON UPDATE CASCADE,
    CONSTRAINT 'usertag_tag_fk'
        FOREIGN KEY 'tag_fk' (tag) REFERENCES 'Tag' (tag_id)
        ON DELETE CASCADE ON UPDATE CASCADE,
);

CREATE TABLE 'tag/resource' (
    'tag_res_id' INT(11) PRIMARY KEY AUTO_INCREMENT,
    CONSTRAINT 'tagresource_tag_fk'
        FOREIGN KEY 'tag_fk' (tag) REFERENCES 'Tag' (tag_id)
        ON DELETE CASCADE ON UPDATE CASCADE,
    CONSTRAINT 'usertag_res_fk'
        FOREIGN KEY 'res_fk' (res) REFERENCES 'Resource' (resource_id)
        ON DELETE CASCADE ON UPDATE CASCADE,
);