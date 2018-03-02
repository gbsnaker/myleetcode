// You&#39;re given strings J representing the types of stones that are jewels, and S representing the stones you have.&nbsp; Each character in S is a type of stone you have.&nbsp; You want to know how many of the stones you have are also jewels.
//
// The letters in J are guaranteed distinct, and all characters in J and S are letters. Letters are case sensitive, so &quot;a&quot; is considered a different type of stone from &quot;A&quot;.
//
// Example 1:
//
//
// Input: J = &quot;aA&quot;, S = &quot;aAAbbbb&quot;
// Output: 3
//
//
// Example 2:
//
//
// Input: J = &quot;z&quot;, S = &quot;ZZ&quot;
// Output: 0
//
//
// Note:
//
//
// 	S and J will consist of letters and have length at most 50.
// 	The characters in J are distinct.
//


/**
 * @param {string} J
 * @param {string} S
 * @return {number}
 */
var numJewelsInStones = function(J, S) {
    let jSet = new Set();
    for(let count=0; count<J.length; count++) {
        jSet.add(J[count]);
    }
    let num = 0;
    for(let count=0; count<S.length; count++) {
        if (jSet.has(S[count])) {
            num++;
        }
    }
    return num;
};
