//Section 2.6
//What is the O(n) of the following code?
public class BigO {
    //We are given a number n and we want to print all the numbers from 0 to n
    public static void printItems(int n, int m){
        //We perform n operations from 0 to n
        //Therefore the O(n) is O(n)
        for (int i = 0; i < n; i++) {
            System.out.println(i);
        }

        //O(n^2)
        //We perform n operations from 0 to n
        for (int j = 0; j < n; j++) {
            System.out.println(j);
            //We perform n operations from 0 to n
            for (int k = 0; k < n; k++) {
                System.out.println(j+" "+k);
            }
        }

        //Drop non-dominant terms
        //O(n^2)
        //We perform n operations from 0 to n
        for (int j = 0; j < n; j++) {
            System.out.println(j);
            //We perform n operations from 0 to n
            for (int k = 0; k < n; k++) {
                System.out.println(j+" "+k);
            }
        }

        //O(n)
        for(int l = 0; l < n; l++) {
            System.out.println();
        }

        //O(n)
        //We perform n operations from 0 to n
        for (int j = 0; j < n; j++) {
            System.out.println(j);
        }
        //O(m)
        //We perform n operations from 0 to m
        for (int k = 0; k < m; k++) {
                System.out.println(j+" "+k);
        }
        
    }

    //O(1)
    //The number of operations this method performs will always stay as 1
    public static int addItems(int n){
        return n+n+n+n+n+n+n+n+n+n;
    }



    public static void main(String[] args) {
        printItems(10);
    }
}
