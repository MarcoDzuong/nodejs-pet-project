import sequelize from '../db';
const Sequelize = require('sequelize');

const dbName = 'Users';

const Users = sequelize.define(dbName, {
  name: Sequelize.STRING(150),
  email: Sequelize.STRING(150),
  password: Sequelize.STRING(255),
  phone: Sequelize.STRING(25),
  avatar: Sequelize.STRING(1000),
}, {
  defaultScope: {
    attributes: { exclude: ['password'] },
  }
});

module.exports = Users;