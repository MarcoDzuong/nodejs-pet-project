function ValidatorError(validatedError) {
    this._validatedError =  validatedError;
    this.message = "Requested params is invalid.";
    this.getValidated = () => {
        return this._validatedError;
    }
}

ValidatorError.prototype = new Error();

export default ValidatorError;