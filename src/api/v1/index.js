import { version } from '../../../package.json';
import { Router } from 'express';
import userController from './userController';
import petController from './petController';
import auth from '../../middleware/auth';

export default ({ config }) => {
	let api = Router();

	config.defaultMiddlewares = [auth];

	api.use('/users', userController({ config }));
	api.use('/pets', petController({ config }));

	// perhaps expose some API metadata at the root
	api.get('/', (req, res) => {
		res.json({ version });
	});

	return api;
}