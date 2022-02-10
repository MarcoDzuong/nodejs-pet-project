Array.prototype.with = function (arr) {
    if (!Array.isArray(arr)) {
        return this;
    }

    return this.concat(arr);
};

Array.prototype.without = function (arr) {
    if (!Array.isArray(arr)) {
        return this;
    }

    const resultArr = [...this];

    arr.forEach(item => {
        const position = resultArr.indexOf(item);
        
        if (position > -1) {
            resultArr.splice(position, 1);
        }
    });

    return resultArr;
};