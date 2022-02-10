import BaseService from './baseService';
import Users from '../model/users';
import UserValidator from '../validator/userValidator';
import {ValidationError} from '@hapi/joi';
import MD5 from 'crypto-js/md5';

const jwt = require('jsonwebtoken');

const request = require('request')

export default class UserService extends BaseService {
    constructor() {
        super(Users, UserValidator);
    }



    getAll = async () => {
        const { model } = this;
        return await model.findAll();
    }

    getById = async (id) => {
        const { model } = this;
        return await model.findByPk(id);
    }

    update = async (user) => {
        const { model } = this;
        const oldUser = await this.getById(user.id)
        oldUser.name = user.name ? user.name : oldUser.name
        oldUser.phone = user.phone ? user.phone : oldUser.phone
        oldUser.email = user.email ? user.email : oldUser.email
        oldUser.avatar = user.avatar ? user.avatar : oldUser.avatar
        if (user.newPassword && user.repeatPassword){
            console.log(new RegExp('^[a-zA-Z0-9]{3,30}$').test(user.newPassword))
            if (user.newPassword !== user.repeatPassword || !new RegExp('^[a-zA-Z0-9]{3,30}$').test(user.newPassword)) {
                const error = new Error("Mật khẩu không trùng nhau hoặc không đúng định dạng");
                error.status = 400;
                throw error;
            }
            oldUser.password = this.passwordToHash(user.newPassword);
        }
        return await model.update(oldUser.dataValues, {
            where: {
                id: user.id
            }
        });
    }

    login = async (loginData) => {
        const { model, validator } = this;
        const validated = validator.LoginSchema.validate(loginData);

        if (validated.error) {
            throw new ValidationError('Dữ liệu gửi lên không chính xác', validated.error);
        }
        const { value: validatedData } = validated;

        validatedData.password = this.passwordToHash(validatedData.password);

        const users = await model.findAll({
            where: validatedData
        });

        if (!users[0]) {
            throw new ValidationError('Sai tài khoản hoặc mật khẩu');
        }

        return users[0];
    };

    register = async (registerData) => {
        const { model, validator } = this;
        const validated = validator.RegisterSchema.validate(registerData);

        if (validated.error) {
            throw new ValidationError('Dữ liệu gửi lên không chính xác', validated.error);
        }
        const { value: validatedData } = validated;

        const foundByEmail = await model.findAll({
            where: {
                email: validatedData.email
            }
        });

        if (foundByEmail && foundByEmail.length > 0) {
            throw new ValidationError('Email đã tồn tại');
        }

        validatedData.password = this.passwordToHash(validatedData.password);

        return model.create(validatedData);
    };

    deleteAll = async () => {
        const { model } = this;
        return await model.destroy({
            truncate: true,
        });
    }

    passwordToHash = (password) => {
        return MD5(password).toString();
    };

    generateToken = (payload) => {
        return jwt.sign(payload, process.env.JWT_SECRET_KEY || 'cai_gi_no_cung_co_cai_gia_cua_n0', { expiresIn: '8h' });
    }


}
