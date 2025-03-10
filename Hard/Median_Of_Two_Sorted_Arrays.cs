public class Solution {
    public double FindMedianSortedArrays(int[] nums1, int[] nums2) {
        int halfIndex = (nums1.Length + nums2.Length) / 2;
        Console.WriteLine(halfIndex);
        if ( (nums1.Length + nums2.Length) % 2 == 0){
            // even (need to find 2 indices)
            if(nums1.Length == 0){
                return ( (nums2[halfIndex-1] + nums2[halfIndex]) / 2.0);
            }
            if(nums2.Length == 0){
                return ( (nums1[halfIndex-1] + nums1[halfIndex]) / 2.0);
            }


            int i = 0;
            int j = 0;
            while (i < nums1.Length && j < nums2.Length && i + j < halfIndex-1){
                if (nums1[i] == nums2[j]){
                    i++;
                }
                else if (nums1[i] < nums2[j]){
                    i++;
                }
                else{
                    j++;
                }
            }

            if(i == nums1.Length){
                while (i+j != halfIndex-1){
                    j++;
                }
                return (nums2[j] + nums2[j+1]) / 2.0;
            }
            if(j == nums2.Length){
                while (i+j != halfIndex-1){
                    i++;
                }
                return (nums1[i] + nums1[i+1]) / 2.0;
            }
            else{
                // next 2 smallest values are the median
                int value1 = 0;
                int value2 = 0;
                if (nums1[i] < nums2[j]){
                    value1 = nums1[i];
                    i++;
                    if (i != nums1.Length && nums1[i] < nums2[j]){
                        value2 = nums1[i];
                    }
                    else{
                        value2 = nums2[j];
                    }
                }
                else{
                    value1 = nums2[j];
                    j++;
                    if ( j != nums2.Length && nums2[j] < nums1[i]){
                        value2 = nums2[j];
                    }
                    else{
                        value2 = nums1[i];
                    }
                }
                return (value1 + value2) / 2.0;
            }
            

            // return -1.0;
        }
        else{
            // odd (just find the middle)
            if(nums1.Length == 0){
                return nums2[halfIndex];
            }
            if(nums2.Length == 0){
                return nums1[halfIndex];
            }



            int i = 0;
            int j = 0;
            while (i < nums1.Length && j < nums2.Length && i + j < halfIndex){
                if (nums1[i] == nums2[j]){
                    i++;
                }
                else if (nums1[i] < nums2[j]){
                    i++;
                }
                else{
                    j++;
                }
            }
            if(i == nums1.Length){
                while (i+j != halfIndex){
                    j++;
                }
                return nums2[j];
            }
            if(j == nums2.Length){
                while (i+j != halfIndex){
                    i++;
                }
                return nums1[i];
            }
            else{
                if (nums1[i] < nums2[j]){
                    return nums1[i];
                }
                else{
                    return nums2[j];
                }
            }
            
        }

        
    }
}