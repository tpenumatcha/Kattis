import java.util.*; 
public class Kattis{ 
public static void main(String[] args){ 
Scanner in = new Scanner(System.in);
while(in.hasNext()){
double num1 = in.nextDouble();
double num2 = in.nextDouble();
double ans = Math.abs(num1-num2);
String strans = String.format ("%.2f", ans);
strans = strans.substring(0,strans.length()-3);
System.out.println(strans);
}
in.close();
}
}
