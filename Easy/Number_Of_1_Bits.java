

public class Number_Of_1_Bits{
    public static void main(String args[]){
        

        String binary = Integer.toBinaryString(Integer.valueOf(args[0]));
        binary = binary.replaceAll("0", "");
       

        System.out.println(binary.length());
    }
}