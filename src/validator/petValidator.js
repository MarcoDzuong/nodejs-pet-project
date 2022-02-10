const Joi = require('@hapi/joi');

const PetValidator = {
    CreateSchema: Joi.object({
        name: Joi.string()
            .min(3)
            .max(50)
            .required(),

        dob: Joi.string()
            .required(),

        gender: Joi.string()
            .required(),

        type: Joi.allow(),

        class: Joi.allow(),

        userId: Joi.required(),

        resource: Joi.allow(),
        images: Joi.string().allow(),
        status: Joi.allow(),
        address: Joi.allow()
    }).options({abortEarly: false}),
    UpdateSchema: Joi.object({
        id: Joi.required(),
        name: Joi.string()
            .min(3)
            .max(50)
            .required(),

        dob: Joi.string()
            .required(),

        gender: Joi.string()
            .required(),

        type: Joi.allow(),

        class: Joi.allow(),

        resource: Joi.allow(),
        images: Joi.string().allow(),
        status: Joi.allow(),
        address: Joi.allow(),
        userId: Joi.required(),
        createdAt: Joi.allow(),
        updatedAt: Joi.allow()
    }).options({abortEarly: false}),
}

export default PetValidator;
