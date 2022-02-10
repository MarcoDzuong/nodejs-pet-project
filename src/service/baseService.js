export default class BaseService {
    constructor(model, validator) {
        this.model = model;
        this.validator = validator;
    }

    makeModel() {
        return this.model;
    }

    getValidator() {
        return this.validator;
    }
}