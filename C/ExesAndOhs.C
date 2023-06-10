/* Check to see if a string has the same amount of 'x's and 'o's. The method must return a boolean and be case insensitive. The string can contain any char.

Examples input/output:

XO("ooxx") => true
XO("xooxx") => false
XO("ooxXm") => true
XO("zpzpzpp") => true // when no 'x' and 'o' is present should return true
XO("zzoo") => false */

// SOLUTION:

#include <stdbool.h>
#include <string.h>
bool xo (const char* str)
{
  int xcount = 0;
  int ocount = 0;
  int i;
  for(i = 0; i < strlen(str); i++){
    if(tolower(str[i]) == 'x'){
      xcount++;
    }else if(tolower(str[i]) == 'o'){
      ocount++;
    }
  }
  if(xcount == ocount){
    return true;
  }
  return false;
}
