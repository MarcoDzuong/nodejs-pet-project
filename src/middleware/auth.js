import BaseController from '../api/v1/baseController';

const jwt = require('jsonwebtoken');
const baseController = new BaseController();

module.exports = (req, res, next) => {
    try {
        const token = req.headers.authorization.split(' ')[1];
        const decodedToken = jwt.verify(token, process.env.JWT_SECRET_KEY || 'cai_gi_no_cung_co_cai_gia_cua_n0');
        if (decodedToken.id) {
            req.headers.userId = decodedToken.id;
            next();
        }
    } catch (error) {
        if (error.name === 'TokenExpiredError') {
            baseController.responseError(res, "Phiên đăng nhập đã hết hạn", 401);
        } else {
            baseController.responseError(res, "Dữ liệu chưa được xác thực", 401);
        }
    }
};