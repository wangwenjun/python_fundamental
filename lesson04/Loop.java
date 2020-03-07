public class Loop
{

	public static void main(String[] args)
	{

		OUTER:
		for(int i = 0;i<10;i++){
		
			for(int j=0;j<10;j++){
				if(j==5)
					break OUTER;

				System.out.println("OutLoop:"+i+", InnerLoop:"+j);
			}
		}
	
	}

}
