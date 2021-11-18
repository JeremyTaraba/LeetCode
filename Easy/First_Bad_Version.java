/*
Prompt:
You are a product manager and currently leading a team to develop a new product. Unfortunately, the latest version of your product fails the quality check. Since each version is developed based on the previous version, all the versions after a bad version are also bad.

Suppose you have n versions [1, 2, ..., n] and you want to find out the first bad one, which causes all the following ones to be bad.

You are given an API bool isBadVersion(version) which returns whether version is bad. Implement a function to find the first bad version. You should minimize the number of calls to the API.


*/






/* The isBadVersion API is defined in the parent class VersionControl.
      boolean isBadVersion(int version); */

public class Solution extends VersionControl {
    
    public int FindBadVersion(int beg, int end){
        //System.out.print("beg = " + beg + " end = " + end);
        if(beg <= end){
            int mid = beg + (end - beg)/2;
            if(isBadVersion(mid)){
                if(!isBadVersion(mid-1)){
                    return mid;
                }
                return FindBadVersion(beg, mid);
            }
            return FindBadVersion(mid, end);
        }
        return -1;
    }
    
    public int firstBadVersion(int n) {
        if(isBadVersion(n)){        //edge case where the last one is the first bad version
            if(!isBadVersion(n-1)){
                return n;
            }
        }
        int firstBad = FindBadVersion(0, n);
        return firstBad;
    }
}

/*
Notes:
We check to see if the current version is bad, if it is we check the previous version, if it isnt
we move to the version in the middle of beggining and end.

Constraints:
1 <= bad <= n <= 231 - 1

*/