import java.util.*;
class Average
{
	public static void main(String args[])
	{
		int a,b,c;
		Scanner s=new Scanner(System.in);
		System.out.println("Enter a:");
		a=s.nextInt();
		System.out.println("Enter b:");
		b=s.nextInt();
		System.out.println("Enter c:");
		c=s.nextInt();
		double sum=a+b+c;
		double average=sum/3;
		System.out.println("Sum:"+sum);
		System.out.println("Average:"+average);
	}
}
		