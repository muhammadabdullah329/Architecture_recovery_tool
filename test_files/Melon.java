public abstract class Melon extends Fruit
{
	private double antioxidants;
	private static double total;
	public Melon(int weight)
	{
		super(weight);
	}
	public void setTotal(double antioxidants)
	{
		total=total+antioxidants;
	}
	@Override
	public double getTotal()
	{
		return total;
	}
}