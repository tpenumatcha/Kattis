import java.util.*; 
public class Kattis{ 
public static void main(String[] args){ 
Scanner in = new Scanner(System.in);
int ability = in.nextInt();
int fall = in.nextInt();
int distance = in.nextInt();
int times = 0;
int location = 0;
while(location<distance){
times++;
location +=ability;
if(!(location>=distance)){
location -= fall;
}
}
System.out.println(times);
}
}
