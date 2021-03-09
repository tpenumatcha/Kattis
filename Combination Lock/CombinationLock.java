import java.util.*; 
public class Kattis{ 
public static void main(String[] args){ 
Scanner in = new Scanner(System.in);
List<Integer> outputs = new ArrayList<Integer>();
double position = 0;
double c1 = -1;
double c2 = -1;
double c3 = -1;
int total = 720;
double ogc1 = -1;
double ogc2 = -1;
double ogc3 = -1;
double ogposition = -1;
boolean lever = true;
while(!(ogposition==0&&ogc1==0&&ogc2==0&&ogc3==0)&&lever){
position = in.nextInt();
c1 = in.nextInt();
c2 = in.nextInt();
c3 = in.nextInt();
ogposition = position;
ogc1 = c1;
ogc2 = c2;
ogc3 = c3;
total = 720;
if(position<c1){
total += ((40.0-(c1-position))/40)*360;
}
else{
total += ((position-c1)/40)*360;
}
position = c1;
total += 360;
if(position>c2){
total += ((40.0-Math.abs(c2-position))/40)*360;
}
else{
total += ((c2-position)/40)*360;
}
position = c2;
if(position<c3){
total += ((40.0-(c3-position))/40)*360;
}
else{
total += ((position-c3)/40)*360;
}
outputs.add(total);
}
for(int i = 0;i<outputs.size()-1;i++){
System.out.println(outputs.get(i));
}
}
}
