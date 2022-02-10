const Joi = require('@hapi/joi');


const UserValidator = {
    LoginSchema: Joi.object({
        email: Joi.string()
            .email()
            .required(),
        password: Joi.string()
            .required()
            .pattern(new RegExp('^[a-zA-Z0-9]{3,30}$')),
    }).options({ abortEarly: false }),
    RegisterSchema: Joi.object({
        name: Joi.string()
            .min(3)
            .max(50)
            .required(),

        phone: Joi.string()
            .pattern(new RegExp('^[0-9]{9,11}$'))
            .required(),

        email: Joi.string()
            .email()
            .required(),

        password: Joi.string()
            .required()
            .pattern(new RegExp('^[a-zA-Z0-9]{3,30}$')),

        repeatPassword: Joi.any().valid(Joi.ref('password')).required(),
        avatar: Joi.string().allow()
    }).options({ abortEarly: false }),
}

export default UserValidator;