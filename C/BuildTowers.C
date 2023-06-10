/* Build Tower
Build a pyramid-shaped tower, as an array/list of strings, given a positive integer number of floors. A tower block is represented with "*" character.

For example, a tower with 3 floors looks like this:

[
  "  *  ",
  " *** ", 
  "*****"
]
And a tower with 6 floors looks like this:

[
  "     *     ", 
  "    ***    ", 
  "   *****   ", 
  "  *******  ", 
  " ********* ", 
  "***********"
]
*/

// SOLUTION:

void build_tower(unsigned n, char tower[n][2 * n - 1])
{
  int i;
  int j;
  int s = 2 * n - 1;
  
	for(i = 0; i < n; i++){
    for(j = 0; j < s; j++){
      tower[i][j] = ' ';
      if(n-1-i <= j && j <= n-1+i){
        tower[i][j] = '*';
      }
    }
  }
}
