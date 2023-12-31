/* You are given an array (which will have a length of at least 3, but could be very large) containing integers. The array is either entirely comprised of odd integers or entirely comprised of even integers except for a single integer N. Write a method that takes the array as an argument and returns this "outlier" N.

Examples
[2, 4, 0, 100, 4, 11, 2602, 36]
Should return: 11 (the only odd number)

[160, 3, 1719, 19, 11, 13, -21]
Should return: 160 (the only even number) */

// SOLUTION:

public class FindOutlier{
  static int find(int[] integers){
    int evencount = 0, oddcount = 0, evennum = 0, oddnum = 0;
    
    for(int i = 0; i < integers.length; i++){
      if(integers[i] % 2 == 0){
        evencount += 1;
        evennum = integers[i];
      }else{
        oddcount += 1;
        oddnum = integers[i];
      }
    }
    
    if(evencount == 1){
      return evennum;
    }else if(oddcount == 1){
      return oddnum;
    }
    
  return 0;
}}
