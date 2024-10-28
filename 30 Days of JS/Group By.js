/**
 * @param {Function} fn
 * @return {Object}
 */
Array.prototype.groupBy = function(fn) {
    const ans = {}
    for(const i of this){
        if(!ans[fn(i)]){
            ans[fn(i)] = [];
        }
        ans[fn(i)].push(i)
    }
    return ans
};

/**
 * [1,2,3].groupBy(String) // {"1":[1],"2":[2],"3":[3]}
 */
