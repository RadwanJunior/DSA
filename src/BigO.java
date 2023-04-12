//Section 2.6
//What is the O(n) of the following code?
public class BigO {
    //We are given a number n and we want to print all the numbers from 0 to n
    public static void printItems(int n){
        //We perform n operations from 0 to n
        //Therefore the O(n) is O(n)
        for (int i = 0; i < n; i++) {
            System.out.println(i);
        }
    }

    public static void main(String[] args) {
        printItems(10);
    }
}
