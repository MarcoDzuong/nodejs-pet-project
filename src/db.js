const { Sequelize } = require('sequelize');
import dbConfig from './config/database';

const { development: db } = dbConfig;
let sequelize = new Sequelize(db.database, db.username, db.password, {
    host: db.host,
    dialect: 'postgres',
    port: db.port
});

export default sequelize;