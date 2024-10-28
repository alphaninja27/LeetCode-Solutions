/**
 * @param {Array} arr
 * @param {number} size
 * @return {Array}
 */
var chunk = function(arr, size) {
    let ans = []
    let i = 0
    while(i < arr.length){
        ans.push(arr.slice(i,i + size))
        i += size
    }
    return ans
};
