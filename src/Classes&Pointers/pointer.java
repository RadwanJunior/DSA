import java.util.HashMap;

public class pointer {
    public static void main(String[] args) {
        
        int num1 = 11;
        int num2 = num1;

        //This will change the value of num2 to point to num1 only at the beginning, but this can be changed if num1 is set to something else
        num1 = 22;

        System.out.println("num1: "+num1);
        System.out.println("num2: "+num2);


        HashMap<String, Integer> map1 = new HashMap<>();
        HashMap<String, Integer> map2 = new HashMap<>();

        map1.put("one", 1);
        //This will make both map1 and map2 point to the same object, even if map1 is changed, map2 will also be changed
        map2 = map1;

        map1.put("two", 2);

        System.out.println(map1);
        System.out.println(map2);
    }
}
