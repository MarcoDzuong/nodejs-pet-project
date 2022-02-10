import sequelize from '../db';
const Sequelize = require('sequelize');

const dbName = 'Pets';

const Pets = sequelize.define(dbName, {
  name: Sequelize.STRING(250),
  dob: Sequelize.DATE(),
  gender: Sequelize.STRING(20),
  type: Sequelize.STRING(250),
  class: Sequelize.STRING(250),
  resource: Sequelize.STRING(250),
  status: Sequelize.STRING(250),
  address: Sequelize.STRING(250),
  userId: Sequelize.NUMBER(),
  images: Sequelize.STRING(4000),
});

module.exports = Pets;