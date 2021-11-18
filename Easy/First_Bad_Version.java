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