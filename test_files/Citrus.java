public abstract class Citrus extends Fruit
{
	private double vitaminC;
	private static double total;
	public Citrus(int weight)
	{
		super(weight);
	}
	public void setVitaminc(double vitaminC)
	{
		total=total+vitaminC;
	}
	@Override
	public double getTotal()
	{
		return total;
	}
}
