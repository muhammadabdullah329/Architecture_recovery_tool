public class FruitTest
{
	public static void main (String[] args)
	{
		if (args.length!=4)
		{
			System.out.println("please enter only 4 numbers");
		}
		else
		{
			int[] array;
			array = new int[4];
			Fruit[] myFruit;
			myFruit = new Fruit[4];
			for (int count1=0;count1<args.length;count1++)
			{
				array[count1]=Integer.parseInt(args[count1]);
			}
			Kinu myKinu=new Kinu(array[0]);
			Malta myMalta=new Malta(array[1]);
			Kharbooza myKharbooza=new Kharbooza(array[2]);
			Tarbooz myTarbooz=new Tarbooz(array[3]);
			myFruit[0]=myKinu;
			myFruit[1]=myMalta;
			myFruit[2]=myKharbooza;
			myFruit[3]=myTarbooz;
			for (Fruit checkFruit :myFruit)
			{
				if (checkFruit instanceof Kinu)
				{
					System.out.printf("You will get %.2f of Vitamin C\n", checkFruit.getTotal());
				}
				else if (checkFruit instanceof Kharbooza)
				{
					System.out.printf("You will get %.3f of Antioxidants", checkFruit.getTotal());
				}
			}
		}
	}
}