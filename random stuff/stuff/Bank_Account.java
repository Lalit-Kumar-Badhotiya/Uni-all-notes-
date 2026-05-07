import java.util.scanner;

public class Bank_Account {
    private float BB;
    private String name;
    private int account_no;

    Bank_Account(int BB, String name, int account_no) {
        this.BB = BB;
        this.name = name;
        this.account_no = account_no;

    }

    public int getAccount_no() {
        return account_no;
    }

    public int getBB() {
        return BB;
    }

    public String getName() {
        return name;
    }

    public void setAccount_no(int account_no) {
        this.account_no = account_no;
    }

    public void setBB(int bB) {
        BB = bB;
        int a = Math.random();// see the inner implementation of this function its crazyyyyyy
    }

    public void setName(String name) {
        this.name = name;
    }

    public int total(int... num) {
        int sum = 0;
        for (int a : num) {
            sum += a;
        }
        return sum;
    }

}
