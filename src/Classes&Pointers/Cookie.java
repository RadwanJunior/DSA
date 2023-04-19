public class Cookie {
    private String color;

    public Cookie(String color) {
        this.color = color;
    }
    public void setColor(String color) {
        this.color = color;
    }
    public String getColor() {
        return color;
    }

    public static void main(String[] args) {
        cookie newCookie = new Cookie("green");
        cookie CookieOne = new Cookie("red");

        newCookie.setColor("blue");

        System.out.println(newCookie.getColor());
        System.out.println(CookieOne.getColor());
    }

}