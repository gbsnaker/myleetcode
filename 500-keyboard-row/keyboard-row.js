// Given a List of words, return the words that can be typed using letters of alphabet on only one row's of American keyboard like the image below. 
//
//
//
//
//
//
//
// Example 1:
//
// Input: ["Hello", "Alaska", "Dad", "Peace"]
// Output: ["Alaska", "Dad"]
//
//
//
// Note:
//
// You may use one character in the keyboard more than once.
// You may assume the input string will only contain letters of alphabet.
//
//


/**
 * @param {string[]} words
 * @return {string[]}
 */
var findWords = function(words) {
    outArr = [];
    let re1 = /^[qwertyuiop]+$/;
    let re2 = /^[asdfghjkl]+$/;
    let re3 = /^[zxcvbnm]+$/;
    for(let word of words) {
        let lower = word.toLowerCase();
        if (re1.test(lower)) {
            outArr.push(word);
            continue;
        }
        if (re2.test(lower)) {
            outArr.push(word);
            continue;
        }
        if (re3.test(lower)) {
            outArr.push(word);
            continue;
        }
    }
    return outArr;
};
