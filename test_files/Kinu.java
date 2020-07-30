public class Kinu extends Citrus
{
	private double vitaminC; 
	public Kinu(int weight)
	{
		super(weight);
		vitaminC=0.03*super.getWeight();
		super.setVitaminc(vitaminC);
	}
	@Override
	public double getTotal()
	{
		return super.getTotal();
	}
}
	