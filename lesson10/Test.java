interface A
{
	default void fun()
	{
		System.out.println("A-fun");
	}
}

interface B
{

	default void fun()
	{
	
		System.out.println("B-fun");
	}

}

public class Test implements A,B
{

	public void fun()
	{
		//System.out.println("Test-fun");
		A.super.fun();
	}

	public static void main(String[] args)
	{
		new Test().fun();
	}
		
}
