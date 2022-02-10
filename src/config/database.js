require('dotenv').config();

module.exports = {
    development : {
        host: process.env.DB_HOST || "112.78.1.79",
        username: process.env.DB_USER || "postgres",
        password: process.env.DB_PASSWORD || "12345",
        port: process.env.DB_PORT || 5432,
        database: process.env.DB_DATABASE || "petory",
        dialect: 'postgres',
    }
  };