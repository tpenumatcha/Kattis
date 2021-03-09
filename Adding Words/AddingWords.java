import java.util.*;
public class Kattis{
public static void main(String[] args){
Scanner in = new Scanner(System.in);
List<String> words = new ArrayList<String>();
List<Integer> values = new ArrayList<Integer>();
List<String> execution = new ArrayList<String>();
List<Integer> finalexecution = new ArrayList<Integer>();
List<String> currentwords = new ArrayList<String>();
int check = 0;
while(in.hasNext()&&check<=2000){
execution.clear();
finalexecution.clear();
currentwords.clear();
check++;
String command = in.next();
if(command.equals("def")){
String word = in.next();
int value = in.nextInt();
boolean repeat = false;
for(int b = 0;b<words.size();b++){
if(words.get(b).equals(word)){
words.set(b,word);
values.set(b,value);
repeat = true;
}
}
if(!repeat){
words.add(word);
values.add(value);
}
}
if(command.equals("calc")){
String statement = in.nextLine();
statement = statement.substring(1);
int i = 0;
boolean available = true;
while(!(statement.substring(i,i+1).equals("="))){
String get = "";
boolean string = false;
while(!(statement.substring(i,i+1).equals(" "))){
string = true;
get += statement.substring(i,i+1);
i++;

}
if(string){
currentwords.add(get);
execution.add(get);
}
i++;
String operation = "";
boolean charac = false;
if((statement.substring(i,i+1).equals("+"))||(statement.substring(i,i+1).equals("-"))){
charac = true;
operation = statement.substring(i,i+1);
i++;
}
if(charac){
execution.add(operation);
}
}
int see = 0;
for(int x = 0;x<currentwords.size();x++){
for(int y = 0;y<words.size();y++){
if(currentwords.get(x).equals(words.get(y))){
see++;
}
}
}
if(!(see==currentwords.size())){
available = false;
}
if(available){
for(int q = 0;q<execution.size();q++){
if(!(execution.get(q).equals("+")||execution.get(q).equals("-"))){
String strnum = Integer.toString(findValue(execution.get(q),words,values));
execution.set(q,strnum);
}
}
int tem = Integer.parseInt(execution.get(0));
int temp = 0;
finalexecution.add(tem);
for(int n = 2;n<execution.size();n+=2){
temp = Integer.parseInt(execution.get(n));
if(execution.get(n-1).equals("-")){
finalexecution.add(temp*-1);
}
else{
finalexecution.add(temp);
}
}
int total = 0;
for(int t = 0;t<finalexecution.size();t++){
total += finalexecution.get(t);
}
int p = 0;
int intindex = 0;
boolean there = false;
while(p<values.size()){
if(values.get(p)==total){
there = true;
intindex = p;
}
p++;
}
if(!there){
System.out.println(statement + " unknown");
}
else{
System.out.println(statement + " " + words.get(intindex));
}
}
else{
System.out.println(statement + " unknown");
}
}//end of if statement
if(command.equals("clear")){
words.clear();
values.clear();
execution.clear();
finalexecution.clear();
}

}
in.close();

}
public static int findValue(String s,List<String> str,List<Integer> num){
int index = 0;
for(int m = 0;m<str.size();m++){
if(str.get(m).equals(s)){
index = m;
}

}
return num.get(index);

}



}
