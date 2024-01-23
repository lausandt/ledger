from tortoise import BaseDBAsyncClient


async def upgrade(db: BaseDBAsyncClient) -> str:
    return """
        CREATE TABLE IF NOT EXISTS "period" (
    "id" SERIAL NOT NULL PRIMARY KEY,
    "nr" INT NOT NULL,
    "start_date" DATE NOT NULL,
    "end_date" DATE NOT NULL
);
CREATE TABLE IF NOT EXISTS "user" (
    "id" SERIAL NOT NULL PRIMARY KEY,
    "username" VARCHAR(50) NOT NULL UNIQUE,
    "full_name" VARCHAR(50) NOT NULL,
    "password" VARCHAR(128) NOT NULL,
    "superuser" BOOL NOT NULL  DEFAULT False,
    "active" BOOL NOT NULL  DEFAULT True
);
COMMENT ON COLUMN "user"."username" IS 'needs to be email';
CREATE TABLE IF NOT EXISTS "budget" (
    "id" SERIAL NOT NULL PRIMARY KEY,
    "amount" DECIMAL(10,2) NOT NULL,
    "created_at" DATE NOT NULL,
    "author_id" INT NOT NULL REFERENCES "user" ("id") ON DELETE CASCADE,
    "period_id" INT NOT NULL REFERENCES "period" ("id") ON DELETE CASCADE
);
CREATE TABLE IF NOT EXISTS "entry" (
    "id" SERIAL NOT NULL PRIMARY KEY,
    "title" VARCHAR(225) NOT NULL,
    "amount" DECIMAL(10,2) NOT NULL,
    "content" TEXT NOT NULL,
    "created_at" DATE NOT NULL,
    "author_id" INT NOT NULL REFERENCES "user" ("id") ON DELETE CASCADE,
    "period_id" INT NOT NULL REFERENCES "period" ("id") ON DELETE CASCADE
);
CREATE TABLE IF NOT EXISTS "aerich" (
    "id" SERIAL NOT NULL PRIMARY KEY,
    "version" VARCHAR(255) NOT NULL,
    "app" VARCHAR(100) NOT NULL,
    "content" JSONB NOT NULL
);"""


async def downgrade(db: BaseDBAsyncClient) -> str:
    return """
        """
