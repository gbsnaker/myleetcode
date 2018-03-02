//
// Initially, there is a Robot at position (0, 0). Given a sequence of its moves, judge if this robot makes a circle, which means it moves back to the original place. 
//
//
//
// The move sequence is represented by a string. And each move is represent by a character. The valid robot moves are R (Right), L (Left), U (Up) and D (down). The output should be true or false representing whether the robot makes a circle.
//
//
// Example 1:
//
// Input: "UD"
// Output: true
//
//
//
// Example 2:
//
// Input: "LL"
// Output: false
//
//


/**
 * @param {string} moves
 * @return {boolean}
 */
var judgeCircle = function(moves) {
    let v = 0, h = 0;
    for(let count=0; count<moves.length; count++) {
        switch(moves[count]) {
            case "U": 
                v++;
                break;
            case "D":
                v--;
                break;
            case "R":
                h++;
                break;
            case "L":
                h--;
                break;
            default:
                break;
        }
    }
    return (v === 0 && h === 0);
};
