public class Tarbooz extends Melon
{
	private double antioxidants;
	public Tarbooz(int weight)
	{
		super(weight);
		antioxidants=0.00008*super.getWeight();
		super.setTotal(antioxidants);
	}
	@Override
	public double getTotal()
	{
		return super.getTotal();
	}
}